from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.runnables import RunnableMap
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import load_tools

load_dotenv()
80 p - 20 t
prompt_template = PromptTemplate(
    input_variables=["animal_type"],
    template="I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
)

@tool
def calculate_age(age: int):
    return age * 3


def langchain_agent():
    llm = ChatOpenAI(model="deepseek:deepseek-chat", temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = executor.invoke(
        {"input": "What is the average age of a dog? Multiply age by 3."}
    )
    print(result["output"])


def langchain_agent(): # old style
    llm = init_chat_model(
        model="deepseek:deepseek-chat",
        temperature=0.5,
    )
    tools = load_tools(["wikipedia", "llm_math"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    result = agent.run(
        "What is the average age of a dog? Multiply age by 3."
    )
    print(result)

def generate_pet_name(animal_type: str = "dog", pet_color: str = "white"):
    llm = init_chat_model(
        model="deepseek:deepseek-chat",
        temperature=0.7,
    )
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color}. Suggest me five cool names for my pet."
    )
    chain = RunnableMap({
        "name": prompt_template | llm
    })

    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    print(response)
