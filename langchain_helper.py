import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import load_tools, initialize_agent, AgentType,Tool
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_pet_name(animal_type: str, pet_color: str) -> str:
    # Initialize model
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama3-70b-8192",
        api_key=GROQ_API_KEY
    )
    
    # Create prompt template
    prompt_template = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it. It is {pet_color} in color. Suggest five cool names."
    )
    
    # Create chain using Runnable interface
    chain = (
        {"animal_type": RunnablePassthrough(), "pet_color": RunnablePassthrough()}
        | prompt_template 
        | llm
        | StrOutputParser()
    )
    
    # Invoke the chain with both parameters
    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response

def run_agent_operations():
    """Function to perform Wikipedia searches and math operations using Groq"""
    llm = ChatGroq(
        temperature=0.5,
        model_name="llama3-70b-8192",
        api_key=GROQ_API_KEY
    )
    
    # Set up tools
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    tools = [
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="Useful for looking up facts on Wikipedia"
        ),
        Tool(
            name="Calculator",
            func=lambda x: str(eval(x)),  # Simple math evaluation
            description="Useful for performing mathematical calculations"
        )
    ]
    
    # Initialize agent
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    # Run the agent with the query from the image
    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )
    return result

if __name__ == "__main__":
    # Run pet name generator
    print("=== PET NAME GENERATOR ===")
    print(generate_pet_name("cat", "pink"))
    
    # Run agent operations
    print("\n=== AGENT OPERATIONS ===")
    print(run_agent_operations())