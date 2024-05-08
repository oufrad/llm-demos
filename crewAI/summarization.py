from dotenv import load_dotenv
import os

from crewai import Agent, Task, Process, Crew
from crewai.project import agent, CrewBase, task, crew
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import json


load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
groq_ai_key = os.getenv("GROQ_API_KEY")

@CrewBase
class ArticleSummarizationCrew():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.groq_llm = ChatGroq(
            model_name="mixtral-8x7b-32768", temperature=0, api_key=groq_ai_key
        )
        self.openai_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=open_ai_key)

    @agent
    def article_summarizer_agent(self) -> Agent:
        return Agent(
            llm = self.groq_llm,
            config= self.agents_config["agents"]["summarization_agent"]
        )

    @task
    def article_summarizations_task(self) -> Task:
        return Task(
            config = self.tasks_config["tasks"]["summarize_article_task"],
            agent = self.article_summarizer_agent()
        )

    @crew
    def article_summirization_crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            process = Process.sequential,
            verbose = 2,
            tasks = self.tasks
        )
