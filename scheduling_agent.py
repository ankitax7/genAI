import streamlit as st

def handle_query(query):
    return f"📅 Scheduling info for: '{query}'"

def scheduling_agent_interface():
    st.title("📆 Scheduling Agent")

    st.write("I help manage interview and meeting schedules.")

    st.markdown("**💡 Example Queries:**")
    st.markdown("- Schedule an interview with John next Tuesday.")
    st.markdown("- Who is available this Friday?")
    st.markdown("- Check calendar slots for the panel.")

    user_input = st.text_input("💬 Your scheduling query:")

    if user_input:
        with st.spinner("Checking calendar..."):
            response = handle_query(user_input)
        st.success("Scheduled!")
        st.markdown(f"**AI Response:** {response}")
