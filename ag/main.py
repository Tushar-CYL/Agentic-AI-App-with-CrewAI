
# main.py
from typing import Dict
from crewai import LLM, Crew
from agents import DisasterManagementAgents
from tasks import DisasterManagementTasks
from dotenv import load_dotenv

load_dotenv()
class DisasterManagementSystem:
    def __init__(self):
        self.llm = LLM(model="gemini/gemini-1.5-pro-latest", temperature=0.7)
        self.agents = DisasterManagementAgents(self.llm)
        self.tasks = DisasterManagementTasks()
        
    def create_crew(self, location: str, disaster_type: str, resources: Dict[str, int]) -> Crew:
        # Create agents
        weather_analyst = self.agents.create_weather_analyst()
        rescue_coordinator = self.agents.create_rescue_coordinator()
        logistics_manager = self.agents.create_logistics_manager()
        
        # Create tasks
        weather_task = self.tasks.create_weather_analysis_task(weather_analyst, location)
        rescue_task = self.tasks.create_rescue_coordination_task(
            rescue_coordinator, disaster_type, location
        )
        logistics_task = self.tasks.create_logistics_task(logistics_manager, resources)
        
        # Create and return crew
        return Crew(
            agents=[weather_analyst, rescue_coordinator, logistics_manager],
            tasks=[weather_task, rescue_task, logistics_task],
            verbose=True
        )
