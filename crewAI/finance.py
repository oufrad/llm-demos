from crewai import Agent, Task, Crew, Process
from crewai.project import agent, task, crew, CrewBase
from utils import get_llm_keys
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools


@CrewBase
class FinancialCrew():
    agents_config = "config/finance/finance_crew_agents.yaml"
    tasks_config = "config/finance/finance_crew_tasks.yaml"
    (open_ai_key, groq_ai_key) = get_llm_keys()

    def __init__(self):
        self.groq_llm = ChatGroq(model="mixtral-8x7b-32768", api_key=self.groq_ai_key, temperature=0.4)
        self.open_ai_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=self.open_ai_key, temperature=0.4)
        self.human_tools = load_tools(["human"])

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config = self.agents_config["agents"]["reporter"],
            llm = self.groq_llm
        )

    @agent
    def financial_expert(self) -> Agent:
        return Agent(
            config = self.agents_config["agents"]["financial_expert"],
            llm = self.groq_llm
        )

    @agent
    def questioner(self) -> Agent:
        return Agent(
            config = self.agents_config["agents"]["questioner"],
            llm = self.groq_llm,
        )

    @task
    def survey(self) -> Task:
        return Task(
            config = self.tasks_config["tasks"]["finance_survey"],
            tools = self.human_tools,
            agent = self.questioner()
        )

    @task
    def guidance(self) -> Task:
        return Task(
            config = self.tasks_config["tasks"]["financial_guidance"],
            agent = self.financial_expert()
        )

    @task
    def reporting(self) -> Task:
        return Task(
            config = self.tasks_config["tasks"]["financial_report"],
            agent = self.reporter()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            verbose = 2,
            process = Process.sequential,
        )
    

financial_crew = FinancialCrew()
crew = financial_crew.crew()
result = crew.kickoff()
print(result)