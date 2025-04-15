```markdown
# Final Assembled Crew Configuration: Persuasive Copy Crew

This document contains the final, approved configuration files for the Persuasive Copy Crew project, assembled according to the verification report.

---

## 1. `pyproject.toml` (Boilerplate)

```toml
[tool.poetry]
name = "persuasive-copy-crew"
version = "0.1.0"
description = "CrewAI project for generating persuasive marketing copy."
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{include = "persuasive_copy_crew"}] # Assuming your main code might live in a folder

[tool.poetry.dependencies]
python = "^3.10"
crewai = "^0.30.0" # Use the relevant version
crewai-tools = "^0.2.0" # Use the relevant version
python-dotenv = "^1.0.0"
# Add the library for the custom tool if implementing fully
# textstat = "^0.7.0" # Example for ReadabilityAnalysisTool

[tool.poetry.group.dev.dependencies]
pytest = "^7.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## 2. `config/agents.yaml` (Verified)

```yaml
# ./config/agents.yaml
Strategy Architect:
  role: Senior Marketing Strategist & Audience Analyst
  goal: Define the core message, target audience, professional/sophisticated/persuasive tone, and key objectives, synthesizing them into a comprehensive Creative Brief document to guide copy creation.
  backstory: >
    You are a meticulous Senior Marketing Strategist with over 15 years of experience dissecting complex client requirements and translating them into actionable creative roadmaps.
    You possess an almost intuitive grasp of audience psychology across diverse demographics and industries. Your expertise lies in identifying the *why* behind the *what*,
    ensuring every piece of communication is laser-focused on achieving specific outcomes. You excel at defining precise tone parameters – professional, sophisticated, persuasive –
    and articulating the subtle nuances required. You approach each project with rigorous analytical thinking. If initial information is insufficient for deep audience or market understanding,
    you are authorized to use the `SerperDevTool` for targeted research. **To use the search tool, provide a concise, specific search query string like `"target audience demographics for luxury electric vehicles"`
    or `"competitor messaging analysis sustainable fashion brands"`**. Your final output *must* be a detailed Creative Brief document detailing Target Audience Profile, Tone Specification, Core Message, Key Objectives, and suggested Persuasive Angles/Hooks.
  tools:
    - SerperDevTool # Tool instance passed in crew.py
  allow_delegation: false
  verbose: true

Persuasive Copywriter:
  role: Master Persuasive Copywriter
  goal: Generate a compelling, engaging, and highly persuasive first draft of the copy, strictly adhering to the strategic direction, tone, and core message defined in the Creative Brief.
  backstory: >
    You are a highly sought-after Master Persuasive Copywriter, renowned for your ability to blend creativity with strategic intent. You don't just write words; you craft narratives
    that captivate, convince, and convert. With a background in both creative writing and behavioral psychology, you understand how to structure arguments, evoke emotion, and use language
    that resonates deeply with the target audience defined in the Creative Brief. You excel at transforming strategic guidelines into flowing, impactful prose that maintains a sophisticated
    and professional tone. You meticulously follow the Creative Brief provided by the Strategy Architect, ensuring your draft embodies the core message and persuasive angles identified.
    Your focus is on generating a powerful, well-structured first version, laying the foundation for the final polished piece.
  allow_delegation: false
  verbose: true

Quality Maestro:
  role: Elite Quality Assurance Editor & Style Purist
  goal: Meticulously refine the draft copy, ensuring grammatical perfection, stylistic consistency, adherence to the Creative Brief (especially regarding tone, sophistication, and persuasiveness), and overall exceptional quality.
  backstory: >
    You are an Elite Quality Assurance Editor, the final guardian of linguistic excellence and strategic alignment. Your standards are uncompromisingly high; you possess an encyclopedic
    knowledge of grammar, syntax, and sophisticated vocabulary. You approach text like a forensic scientist, scrutinizing every word and phrase for clarity, precision, impact, and flow.
    Your primary mandate is to elevate the draft copy to meet the "exceptionally professional, sophisticated, and persuasive" standard defined in the Creative Brief, ensuring flawless execution
    and perfect alignment with the target audience and objectives. You will rigorously check the draft against *all* points in the Creative Brief. You are also equipped with a `Readability Analysis Tool`.
    **Use this tool by providing the *full text* of the draft as input to assess its readability scores (e.g., Flesch-Kincaid). Use these scores to inform your edits, ensuring you balance sophistication
    with appropriate accessibility for the target audience.** Your final output must be a polished, error-free masterpiece ready for delivery.
  tools:
    - Readability Analysis Tool # Tool instance passed in crew.py
  allow_delegation: false
  verbose: true
```

---

## 3. `config/tasks.yaml` (Corrected: `tools` key removed)

```yaml
# ./config/tasks.yaml
analyze_and_brief:
  description: >
    **Objective:** Analyze user requirements and develop a comprehensive Creative Brief.

    **Steps:**
    1.  **Receive and Parse:** Carefully read the user-provided descriptions and objectives (e.g., from the '{full_user_request}' input). Identify all explicit and implicit requirements.
    2.  **Audience Definition:** Define the target audience profile. Consider demographics, psychographics, pain points, and motivations relevant to the objectives.
    3.  **Tone Specification:** Determine the precise tone required: professional, sophisticated, and persuasive. Define specific nuances or keywords that embody this tone (e.g., authoritative, elegant, benefit-driven).
    4.  **Core Message & Objectives:** Synthesize the user's input into a clear, concise core message. List the key communication objectives the copy must achieve (e.g., drive sign-ups, explain a complex concept, build brand authority).
    5.  **Research (if needed):** If context is lacking regarding the topic, industry standards, competitors, or audience, use the `SerperDevTool`.
        *   **Tool Input:** Formulate specific search queries relevant to your information needs (e.g., "communication style of top SaaS companies", "target audience pain points for [product category]", "persuasive language for [industry]"). Provide the tool with a string containing your search query.
    6.  **Angle Identification:** Brainstorm potential persuasive angles, hooks, or narrative approaches that align with the core message, audience, and tone.
    7.  **Constraint Listing:** Note any specific constraints, keywords to include/exclude, length limitations, or formatting requirements mentioned by the user.
    8.  **Synthesize Brief:** Compile all findings (Steps 2-7) into a structured Creative Brief document. Use clear headings for each section.

  agent: Strategy Architect
  # Removed 'tools:' key - Tools are associated with the agent in crew.py
  expected_output: >
    A structured markdown document titled "Creative Brief" containing the following sections:
    - **Target Audience Profile:** Detailed description of the intended audience.
    - **Tone Specification:** Definition of the required professional, sophisticated, and persuasive tone, including specific adjectives or style notes.
    - **Core Message:** A concise statement of the central idea to be communicated.
    - **Key Objectives:** Bulleted list of measurable goals for the copy.
    - **Persuasive Angles/Hooks:** Suggested narrative or persuasive strategies.
    - **Constraints & Keywords:** List of any limitations, mandatory inclusions/exclusions.

draft_copy:
  description: >
    **Objective:** Generate a compelling first draft of the copy based on the Creative Brief.

    **Steps:**
    1.  **Understand the Brief:** Thoroughly review the Creative Brief provided by the Strategy Architect (received as context from the previous task). Internalize the target audience, tone, core message, objectives, and suggested angles.
    2.  **Brainstorm Concepts:** Based on the brief, ideate specific creative concepts, headlines, opening lines, and structural flows for the copy.
    3.  **Drafting - Persuasion Focus:** Begin writing the initial draft. Prioritize crafting persuasive language that resonates with the target audience defined in the brief. Weave in the core message and address the key objectives.
    4.  **Tone Adherence:** Continuously check that the language and style align with the specified professional, sophisticated, and persuasive tone.
    5.  **Structure and Flow:** Organize the content logically. Ensure smooth transitions between paragraphs and ideas, creating an engaging narrative.
    6.  **Angle Implementation:** Actively incorporate the persuasive angles or hooks suggested in the Creative Brief, or develop alternatives if more effective ones emerge during writing, ensuring they align with the strategy.
    7.  **Initial Review:** Perform a quick self-review for obvious errors or major deviations from the brief before passing it on.

  agent: Persuasive Copywriter
  expected_output: >
    A single block of text representing the first draft of the required copy. The draft should be well-structured (e.g., with paragraphs) and make a clear attempt to implement all key aspects of the Creative Brief (tone, message, objectives, persuasive angles).

refine_and_polish:
  description: >
    **Objective:** Transform the draft copy into a final, flawless piece meeting all quality and strategic standards.

    **Steps:**
    1.  **Cross-Reference Brief and Draft:** Meticulously compare the draft copy (received as context from the 'draft_copy' task) against the original Creative Brief (received as context from the 'analyze_and_brief' task).
    2.  **Clarity & Conciseness:** Edit the text for maximum clarity and impact. Eliminate jargon (unless appropriate for the audience), redundancy, and unnecessary words. Ensure sentences are well-constructed.
    3.  **Grammar & Mechanics:** Proofread rigorously for errors in grammar, spelling, punctuation, and syntax. Correct all mistakes.
    4.  **Style & Tone Enhancement:** Refine the language to elevate its sophistication and professionalism. Ensure the persuasive elements are sharp and effective, perfectly matching the tone defined in the brief. Check for consistency in style throughout the piece.
    5.  **Objective Verification:** Confirm that the copy directly addresses and fulfills all Key Objectives outlined in the Creative Brief.
    6.  **Readability Check (if tool available):** Use the `Readability Analysis Tool`.
        *   **Tool Input:** Provide the *entire text content* of the current version of the copy as a single string input to the tool.
        *   **Evaluation:** Evaluate the score against the target audience profile in the Creative Brief. Make adjustments to sentence structure or vocabulary if needed to improve alignment, *without sacrificing sophistication*.
    7.  **Final Polish:** Read the copy aloud or use text-to-speech to catch awkward phrasing or rhythm issues. Ensure the final output flows naturally and leaves a strong, professional impression.
    8.  **Quality Assurance:** Perform a final check to guarantee the copy is exceptionally professional, sophisticated, persuasive, error-free, and perfectly aligned with all requirements in the Creative Brief.

  agent: Quality Maestro
  # Removed 'tools:' key - Tools are associated with the agent in crew.py
  expected_output: >
    The final, polished version of the copy as a single block of text. It must be free of grammatical errors, typos, and awkward phrasing. The language must be demonstrably professional, sophisticated, and persuasive, precisely matching the tone and audience requirements specified in the Creative Brief, and fulfilling all stated objectives.
```

---

## 4. `crew.py` (Verified - Confirmed Correct File Loading)

```python
# ./crew.py
import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import BaseTool, SerperDevTool

# Placeholder for custom tool: Readability Analysis Tool
class ReadabilityAnalysisTool(BaseTool):
    name: str = "Readability Analysis Tool"
    description: str = ("Analyzes the readability of a given text using a standard metric "
                        "like Flesch-Kincaid Grade Level. Input must be the full text content.")

    def _run(self, text: str) -> str:
        """
        Runs the readability analysis.
        In a real implementation, this would use a library like 'textstat'.
        Example:
        try:
            import textstat
            score = textstat.flesch_kincaid_grade(text)
            return f"Readability Score (Flesch-Kincaid Grade): {score}"
        except ImportError:
            return "Readability Analysis Tool: 'textstat' library not found. Cannot calculate score."
        except Exception as e:
            return f"Readability Analysis Tool: Error calculating score - {e}"
        """
        # Simple placeholder calculation if textstat is not available
        words = text.split()
        word_count = len(words)
        sentence_count = text.count('.') + text.count('!') + text.count('?') + text.count('\n')
        if sentence_count == 0: sentence_count = 1 # Avoid division by zero
        if word_count == 0: return "Readability Score: N/A (No text provided)"

        try:
            # Basic Flesch-Kincaid Grade formula approximation
            avg_sentence_length = word_count / sentence_count
            # Syllable count approximation (very rough - based on longer words)
            syllable_like_words = sum(1 for word in words if len(word) > 6) # Count words longer than 6 chars
            syllables_per_word = (syllable_like_words * 2.5) / word_count if word_count > 0 else 0 # Very rough estimate
            score = (0.39 * avg_sentence_length) + (11.8 * syllables_per_word) - 15.59
            return (f"Placeholder Readability Score (Flesch-Kincaid Grade approximation): {score:.2f}\n"
                    f"(Note: This uses a simplified placeholder calculation. Install 'textstat' for accurate results.)")
        except Exception as e:
            return f"Readability Analysis Tool: Error during placeholder calculation - {e}"

@CrewBase
class PersuasiveCopyCrew():
    """PersuasiveCopyCrew class defining the agents, tasks, and crew setup."""
    # CORRECT: Loading configuration from files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # Instantiate tools potentially requiring API keys or setup here
        # Check for Serper API key
        serper_api_key = os.getenv("SERPER_API_KEY")
        if not serper_api_key:
            print("Warning: SERPER_API_KEY environment variable not set. "
                  "The Strategy Architect's search tool may not function.")
            # Consider raising an error or using a mock if the key is essential
        self.serper_tool = SerperDevTool()
        self.readability_tool = ReadabilityAnalysisTool()

    @agent
    def strategy_architect(self) -> Agent:
        return Agent(
            # CORRECT: Using config loaded from file path
            config=self.agents_config['Strategy Architect'],
            tools=[self.serper_tool], # Pass instantiated tool
            verbose=True,
            allow_delegation=False
        )

    @agent
    def persuasive_copywriter(self) -> Agent:
        return Agent(
            # CORRECT: Using config loaded from file path
            config=self.agents_config['Persuasive Copywriter'],
            # No tools assigned to this agent explicitly
            verbose=True,
            allow_delegation=False
        )

    @agent
    def quality_maestro(self) -> Agent:
        return Agent(
            # CORRECT: Using config loaded from file path
            config=self.agents_config['Quality Maestro'],
            tools=[self.readability_tool], # Pass instantiated tool
            verbose=True,
            allow_delegation=False
        )

    @task
    def analyze_and_brief(self) -> Task:
        return Task(
            # CORRECT: Using config loaded from file path
            config=self.tasks_config['analyze_and_brief'],
            agent=self.strategy_architect()
            # Output is implicitly passed to the next task in sequential process
            # Context could be added if needed: context=[some_previous_task_output_if_any]
        )

    @task
    def draft_copy(self) -> Task:
        return Task(
            # CORRECT: Using config loaded from file path
            config=self.tasks_config['draft_copy'],
            agent=self.persuasive_copywriter(),
            # This task relies on the output of analyze_and_brief implicitly via sequence.
            # Explicit context if needed: context=[self.analyze_and_brief()]
        )

    @task
    def refine_and_polish(self) -> Task:
        return Task(
            # CORRECT: Using config loaded from file path
            config=self.tasks_config['refine_and_polish'],
            agent=self.quality_maestro(),
            # This task implicitly uses outputs from previous tasks.
            # Explicit context can ensure both brief and draft are available if needed:
            # context=[self.analyze_and_brief(), self.draft_copy()],
            output_file="final_persuasive_copy.md" # Saving the final output
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Persuasive Copy Crew"""
        return Crew(
            agents=[
                self.strategy_architect(),
                self.persuasive_copywriter(),
                self.quality_maestro()
            ],
            tasks=[
                self.analyze_and_brief(),
                self.draft_copy(),
                self.refine_and_polish()
            ],
            process=Process.sequential,
            verbose=True
            # Optional: Memory, Cache, etc. can be configured here
            # memory=True,
            # cache=True,
        )
```

---

## 5. `main.py` (Verified)

```python
# ./main.py
import os
# Ensure the 'crew' module (crew.py) is accessible in the Python path.
# If main.py and crew.py are in the same directory, this works directly.
from crew import PersuasiveCopyCrew

# Optional: Load .env file if you're using one to store API keys
# from dotenv import load_dotenv
# load_dotenv()

def run():
    """
    Sets up and runs the PersuasiveCopyCrew.
    """
    # Define the inputs for the crew run.
    # The key 'full_user_request' should ideally match a placeholder in the
    # first task's description if you want it automatically interpolated.
    # Otherwise, the first agent needs to be prompted to use this input structure.
    inputs = {
        'full_user_request': """
        We need website copy for the main landing page of our new product.
        Product: An AI-powered platform creating personalized learning plans in STEM (Science, Tech, Engineering, Math) for high school students.
        Target Audience: Primarily tech-savvy high school students (ages 14-18). Secondary audience: Their parents who are concerned about college readiness and academic performance.
        Desired Tone: The copy must be professional and sophisticated, but also persuasive and slightly futuristic/innovative to appeal to the students. It should feel empowering.
        Core Message to Convey: Our AI platform creates truly personalized learning paths that adapt to each student, leading to improved understanding, better grades in STEM subjects, and enhanced college application prospects.
        Key Communication Objectives:
        1. Clearly explain what the platform does (AI-personalized STEM learning plans).
        2. Highlight the key benefits (personalization, grade improvement, college readiness).
        3. Persuade visitors to sign up for a free trial or request a demo.
        4. Emphasize ease of use and the platform's adaptive capabilities.
        Specific Constraints/Notes:
        - Avoid overly complex technical jargon. Focus on benefits over features.
        - Briefly mention that the platform offers affordable plans.
        - The main headline for the page should be concise (ideally under 10 words).
        - The overall output should be suitable for a website landing page.
        """
    }

    # Ensure an output directory exists if tasks save files there.
    # The current 'refine_and_polish' task saves to the root directory.
    # If output_file was 'output/final_copy.md', this line would be necessary.
    # os.makedirs('output', exist_ok=True) # Uncomment if saving to a subdirectory

    # Instantiate the crew class
    persuasive_copy_crew = PersuasiveCopyCrew()

    # Kick off the crew's process
    print("-----------------------------------------")
    print("## Kicking off the Persuasive Copy Crew...")
    print("   (Ensure config/*.yaml exists and environment variables like SERPER_API_KEY are set)")
    print("-----------------------------------------")
    # Pass the inputs dictionary to the kickoff method
    result = persuasive_copy_crew.crew().kickoff(inputs=inputs)

    # Print the final result from the crew's execution
    print("\n\n########################")
    print("## Crew Execution Result:")
    print("########################")
    print(result)
    print("\n------------------------\n")
    print(f"Note: The final polished copy should also be saved to 'final_persuasive_copy.md' "
          f"in the directory where this script was run, as defined in the 'refine_and_polish' task.")

if __name__ == "__main__":
    print("=========================================")
    print("   Starting Persuasive Copy Crew Run")
    print("=========================================")
    run()
    print("\n=========================================")
    print("   Crew Execution Finished")
    print("=========================================")

```
```