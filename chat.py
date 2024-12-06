from crewai import Agent, Task, Crew, Process 
import os
import json
def config():
    # Determine the model's dimensionality
    os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
    os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  # Adjust based on available model
    os.environ["OPENAI_API_KEY"] = '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'  # Adjust based on your OpenAI API key
    GROQ_API_KEY = ""


def chato(emotion , query, history):
    config()
    # Define the chat Expert Agent
    emotion_based_expert = Agent(
    role="Expert chatbot",
    goal="Analyze the user's query, respond based on their emotional state and conversation history.",
    backstory="An AI designed to understand user query and preferences, providing responses that align with the user's emotional state and personal preferences based on history of conversation, ensuring a personalized and empathetic conversation.",
    verbose=False,
    allow_delegation=False
    )


    # Define the task for the agent
    # Define the task for the emotion-based expert chatbot
    chat_task = Task(
    description=(
        f"""Analyze the user's query:{query} to:
               1. Tailor the response based on the user's emotional state and preferences emotion {emotion}, history {history}.
               2. Ensure that the response aligns with the user's mood and needs, providing empathy and personalization."""
    ),
    agent=emotion_based_expert,
    expected_output="""Return a JSON object containing the personalized response like this example:
    {
        "response": "I'm glad you're feeling positive! How can I assist you today?",
    }"""
)


    # Create a Crew with the Financial Expert agent and task
    crew = Crew(
        agents=[emotion_based_expert],
        tasks=[chat_task],
        verbose=1,
        process=Process.sequential,
        Output_Log_File=False,
    )


    # Execute the crew's task
    output = crew.kickoff()
    return json.loads(str(output))
