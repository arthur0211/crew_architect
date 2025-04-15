#!/usr/bin/env python
# src/crew_architect/main.py
import os # Import the os module
from crew_architect.crew import CrewForgeCrew

def run():
    """
    Run the CrewForge crew to generate configuration for a new crew.
    """
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)

    # Define the user's request for the new crew here
    inputs = {
        'user_crew_description': """
        An expert crew of communication strategists and copywriters specializing in transforming user descriptions and objectives into exceptionally professional, sophisticated, and persuasive copy. This crew meticulously deconstructs user requirements, ideates compelling creative approaches, and rigorously refines the final deliverable to ensure optimal quality, clarity, and impact, achieving precise alignment with the target audience and intended tone..
        """
    }
    CrewForgeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
