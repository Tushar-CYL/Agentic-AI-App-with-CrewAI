# tasks.py
from typing import List, Dict
from crewai import Task, Agent
from dotenv import load_dotenv

load_dotenv()
class DisasterManagementTasks:
    @staticmethod
    def create_weather_analysis_task(agent: Agent, location: str) -> Task:
        return Task(
            description=f"""Analyze weather patterns for {location}:
            1. Monitor current conditions
            2. Predict potential disaster scenarios
            3. Provide early warnings""",
            expected_output="""A detailed weather analysis report containing:
            1. Current weather conditions
            2. Potential disaster risks
            3. Early warning recommendations
            4. Timeline of expected weather changes""",
            agent=agent
        )
    
    @staticmethod
    def create_rescue_coordination_task(agent: Agent, disaster_type: str, location: str) -> Task:
        return Task(
            description=f"""Coordinate rescue operations for {disaster_type} in {location}:
            1. Allocate rescue teams
            2. Prioritize affected areas
            3. Manage emergency resources""",
            expected_output="""A comprehensive rescue operation plan including:
            1. Team deployment strategy
            2. Priority zones map
            3. Resource allocation schedule
            4. Emergency response timeline""",
            agent=agent
        )
    
    @staticmethod
    def create_logistics_task(agent: Agent, resources: Dict[str, int]) -> Task:
        return Task(
            description=f"""Manage resource distribution:
            1. Track available resources: {resources}
            2. Optimize distribution routes
            3. Ensure efficient supply chain""",
            expected_output="""A detailed logistics management plan containing:
            1. Resource inventory status
            2. Distribution route optimization
            3. Supply chain efficiency metrics
            4. Resource allocation priorities""",
            agent=agent
        )

