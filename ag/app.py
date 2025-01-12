
# app.py
import streamlit as st
from datetime import datetime
from typing import Dict
from main import DisasterManagementSystem
from dotenv import load_dotenv

load_dotenv()
def main():
    st.set_page_config(page_title="Disaster Management System", layout="wide")
    
    st.title("AI-Powered Disaster Management System")
    
    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Sidebar for input parameters
    st.sidebar.header("Disaster Parameters")
    location = st.sidebar.text_input("Location")
    disaster_type = st.sidebar.selectbox(
        "Disaster Type",
        ["Flood", "Earthquake", "Hurricane", "Wildfire", "Other"]
    )
    
    # Resource management
    st.sidebar.header("Available Resources")
    rescue_teams = st.sidebar.number_input("Number of Rescue Teams", min_value=1)
    medical_supplies = st.sidebar.number_input("Medical Supply Units", min_value=0)
    vehicles = st.sidebar.number_input("Available Vehicles", min_value=0)
    
    resources = {
        "rescue_teams": rescue_teams,
        "medical_supplies": medical_supplies,
        "vehicles": vehicles
    }
    
    # Main interface
    if st.button("Generate Response Plan"):
        if location and disaster_type:
            with st.spinner("Analyzing situation and generating response plan..."):
                try:
                    system = DisasterManagementSystem()
                    crew = system.create_crew(location, disaster_type, resources)
                    result = crew.kickoff()
                    
                    # Add to chat history
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.session_state.chat_history.append({
                        "timestamp": timestamp,
                        "location": location,
                        "disaster_type": disaster_type,
                        "response_plan": result
                    })
                    
                    # Display result
                    st.success("Response plan generated successfully!")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please fill in all required fields.")
    
    # Display history
    if st.session_state.chat_history:
        st.header("Response History")
        for entry in reversed(st.session_state.chat_history):
            with st.expander(f"{entry['disaster_type']} - {entry['location']} ({entry['timestamp']})"):
                st.markdown(entry['response_plan'])

if __name__ == "__main__":
    main()