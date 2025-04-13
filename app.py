import streamlit as st
from agents import (
    talent_manager,
    sourcing_agent,
    screening_agent,
    engagement_agent,
    scheduling_agent,
)

# Page setup
st.set_page_config(page_title="Intelligent Talent Acquisition Assistant", layout="centered")
st.title("🤖 Intelligent Talent Acquisition Assistant")
st.markdown("Welcome to your GenAI-powered hiring assistant! Select a role from the sidebar to begin.")

# Sidebar navigation
option = st.sidebar.radio(
    "Choose an agent to interact with:",
    (
        "Talent Acquisition Manager",
        "Sourcing Agent",
        "Screening Agent",
        "Engagement Agent",
        "Scheduling Agent",
    ),
)

# Routing based on selection
if option == "Talent Acquisition Manager":
    talent_manager.talent_acquisition_manager_interface()
elif option == "Sourcing Agent":
    sourcing_agent.sourcing_agent_interface()
elif option == "Screening Agent":
    screening_agent.screening_agent_interface()
elif option == "Engagement Agent":
    engagement_agent.engagement_agent_interface()
elif option == "Scheduling Agent":
    scheduling_agent.scheduling_agent_interface()
