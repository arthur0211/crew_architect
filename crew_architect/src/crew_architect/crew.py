# src/crew_forge/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewForgeCrew():
    """CrewForgeCrew uses AI agents to generate CrewAI configuration files."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def requirements_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['requirements_analyst'],
            verbose=True
            # Add tools=[Tool()] if this agent needs specific tools
        )

    @agent
    def crew_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['crew_architect'],
            verbose=True
        )

    @agent
    def agent_definer(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_definer'],
            verbose=True
        )

    @agent
    def task_definer(self) -> Agent:
        return Agent(
            config=self.agents_config['task_definer'],
            verbose=True
        )

    @agent
    def code_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['code_generator'],
            verbose=True
        )

    @agent
    def configuration_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['configuration_reviewer'],
            # tools=[] # Tool removed
            verbose=True
        )

    @task
    def analyze_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_requirements_task'],
            agent=self.requirements_analyst()
        )

    @task
    def design_crew_architecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_crew_architecture_task'],
            agent=self.crew_architect(),
            context=[self.analyze_requirements_task()] # Explicitly pass context if needed
        )

    @task
    def define_agents_yaml_task(self) -> Task:
        return Task(
            config=self.tasks_config['define_agents_yaml_task'],
            agent=self.agent_definer(),
            context=[self.design_crew_architecture_task()]
        )

    @task
    def define_tasks_yaml_task(self) -> Task:
        return Task(
            config=self.tasks_config['define_tasks_yaml_task'],
            agent=self.task_definer(),
            context=[self.design_crew_architecture_task()]
        )

    @task
    def generate_crew_py_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_crew_py_task'],
            agent=self.code_generator(),
            # Context tasks provide necessary info implicitly or explicitly
            context=[self.define_agents_yaml_task(), self.define_tasks_yaml_task(), self.design_crew_architecture_task()]
        )

    @task
    def generate_main_py_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_main_py_task'],
            agent=self.code_generator(),
            context=[self.generate_crew_py_task(), self.design_crew_architecture_task()]
        )

    @task
    def review_configuration_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_configuration_task'],
            agent=self.configuration_reviewer(),
            context=[
                self.define_agents_yaml_task(),
                self.define_tasks_yaml_task(),
                self.generate_crew_py_task(),
                self.generate_main_py_task()
            ]
        )

    @task
    def assemble_output_task(self) -> Task:
        return Task(
            config=self.tasks_config['assemble_output_task'],
            agent=self.configuration_reviewer(),
            context=[
                self.review_configuration_task(),
                self.define_agents_yaml_task(),
                self.define_tasks_yaml_task(),
                self.generate_crew_py_task(),
                self.generate_main_py_task()
            ],
            output_file=self.tasks_config['assemble_output_task']['output_file']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewForgeCrew"""
        return Crew(
            agents=self.agents,
            tasks=[
                self.analyze_requirements_task(),
                self.design_crew_architecture_task(),
                self.define_agents_yaml_task(),
                self.define_tasks_yaml_task(),
                self.generate_crew_py_task(),
                self.generate_main_py_task(),
                self.review_configuration_task(),
                self.assemble_output_task()
            ],
            process=Process.sequential,
            verbose=True
        )
