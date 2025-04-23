# CrewArchitect Crew

Welcome to the CrewArchitect project. This crew is designed to **generate the configuration files (agents.yaml, tasks.yaml, crew.py, main.py, and a pyproject.toml template) for a new CrewAI project based on a user-provided description.** Our goal is to automate the initial setup of new crews, allowing you to focus on refining the generated prompts and logic.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Setting Up

**Add your `OPENAI_API_KEY` (or other LLM provider key) into the `.env` file.** This is used by the agents within CrewArchitect to generate the configuration files.

-   **Provide Input:** Modify the `user_crew_description` variable within `src/crew_architect/main.py` to describe the crew you want to generate.
-   _(Optional)_ Customize CrewArchitect Agents: You can further customize the agents that build your crew by modifying `src/crew_architect/config/agents.yaml`.
-   _(Optional)_ Customize CrewArchitect Tasks: You can adjust the process CrewArchitect follows by modifying `src/crew_architect/config/tasks.yaml`.

## Running the Project

To kickstart the CrewArchitect crew and generate the configuration for your desired crew, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the CrewArchitect Crew. The agents will:
1. Analyze your description in `main.py`.
2. Design the architecture for the new crew.
3. Generate the content for `agents.yaml`, `tasks.yaml`, `crew.py`, and `main.py`.
4. Generate a boilerplate `pyproject.toml` template.
5. Review the generated content.
6. Assemble all generated content into a single Markdown file located at `output/generated_crew_files.md`.

**Output:** The result is **NOT** a directly runnable crew from this project, but rather a Markdown file (`output/generated_crew_files.md`) containing the necessary code and configuration for you to copy into a *new* CrewAI project.

## Understanding Your CrewArchitect Crew

The CrewArchitect Crew itself is composed of multiple AI agents designed for meta-programming:

-   **Requirements Analyst:** Analyzes the user description.
-   **Crew Architect:** Designs the structure, tasks, and tool needs of the target crew.
-   **Agent/Task Definers:** Write the specific YAML configurations based on the architecture.
-   **Code Generator:** Writes the `crew.py` and `main.py` code, incorporating tool assignments and best practices.
-   **Configuration Reviewer & Assembler:** Reviews all generated components for correctness and consistency, then assembles the final Markdown output.

These agents collaborate sequentially to transform your high-level description into a structured starting point for your new crew.

## Support

For support, questions, or feedback regarding the CrewArchitect Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
