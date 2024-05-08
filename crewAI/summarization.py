from dotenv import load_dotenv
import os

from crewai import Agent, Task, Process, Crew
from crewai.project import agent, CrewBase, task, crew
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import json


load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

@CrewBase
class ArticleSummarizationCrew():
    agents_config = "./agents.yml"

    def __init__(self):
        self.groq_llm = ChatGroq(
            model_name="mixtral-8x7b-32768", temperature=0, api_key=groq_key
        )
        self.openai_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=openai_key)

    @agent
    def article_summarizer_agent(self):
        return Agent(
            llm = self.groq_llm,
            config= self.agents_config["agent"]["summarization_agent"]
        )

    @task
    def article_summarizations_task(self):
        return Task(
            config = self.agents_config["tasks"]["summarize_article_task"],
            agent = self.article_summarizer_agent()
        )

    @Crew
    def article_summirization_crew(self):
        return Crew(
            agents = self.agents,
            process = Process.sequential,
            verbose = 2,
            tasks = self.tasks
        )


load_dotenv()


open_ai_key = os.getenv("OPENAI_API_KEY")
groq_ai_key = os.getenv("GROQ_API_KEY")