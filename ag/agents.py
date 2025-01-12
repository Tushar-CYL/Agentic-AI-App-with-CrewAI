# agents.py
from crewai import Agent, Task, Crew, LLM
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()
class DisasterManagementAgents:
    def __init__(self, llm: Optional[LLM] = None):
        self.llm = llm
        
    def create_weather_analyst(self) -> Agent:
        return Agent(
            role="Weather Analysis Expert",
            goal="Analyze weather patterns and predict potential disaster scenarios",
            backstory="Expert meteorologist with experience in disaster prediction and analysis",
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )
    
    def create_rescue_coordinator(self) -> Agent:
        return Agent(
            role="Rescue Operations Coordinator",
            goal="Coordinate rescue teams and resources efficiently",
            backstory="Experienced emergency response coordinator with expertise in resource management",
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )
    
    def create_logistics_manager(self) -> Agent:
        return Agent(
            role="Logistics Manager",
            goal="Manage and optimize resource allocation and supply chains",
            backstory="Supply chain expert specializing in emergency resource distribution",
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )
