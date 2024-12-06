from crewai import Agent, Task, Crew, Process
import os
import json
def config():
    os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
    os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  # Adjust based on available model
    os.environ["OPENAI_API_KEY"] = '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'  # Adjust based on your OpenAI API key
    GROQ_API_KEY = ""

animations = ["SpongeBob", "Tom and Jerry", "Mickey Mouse", "Looney Tunes", "The Simpsons", "Family Guy", "South Park", "Rick and Morty", "Adventure Time", "BoJack Horseman", "Futurama", "Archer", "Bob's Burgers", "The Flintstones", "Scooby-Doo", "The Jetsons", "DuckTales", "Teen Titans Go!", "The Powerpuff"  ]
games = ["Mario", "Zelda", "Sonic"]
def controll(query,animations=animations,games=games):
    config()
    # Define the controll Expert Agent
    controll_expert = Agent(
        role=" Query Observer",
    goal="Analyze the user query to identify emotion and detect if the query contains any Easter egg references",
    backstory="An advanced AI specialized in understanding user queries, extracting emotion, and identifying Easter egg references.",
    verbose=True,
    allow_delegation=False
    )


    # Define the task for the agent
    controll_task = Task(
        description=(
            f"""Analyze the given query: {query} to:
                   1. Detect emotion of the user.
                   2. Detect if the query contains any Easter egg references (animations or games). from this list animation : {animations} and games : {games}"""
        ),
        agent=controll_expert,
        expected_output=("""Return a JSON object containing emotion overview and easter egg references like this example (! only json format !): : 
                         {
            "Emotion": "angry but curious",
            "Easter": { "animation": "SpongeBob", "games": "Mario" }
        }"""
        )
    )

    # Create a Crew with the Financial Expert agent and task
    crew = Crew(
        agents=[controll_expert],
        tasks=[controll_task],
        verbose=1,
        process=Process.sequential,
        Output_Log_File=True,
        
    )

    # Execute the crew's task
    output = crew.kickoff()
    print(str(output))
    return json.loads(str(output))  # Convert the output to JSON format before returning

#controlled = print(controll("i am feeling angry but curious and i want to watch SpongeBob and play Mario"))
