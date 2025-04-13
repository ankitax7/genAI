import streamlit as st

def handle_query(query):
    return f"🤖 This is a simulated AI response to your query: '{query}'"

def talent_acquisition_manager_interface():
    st.title("🎯 Talent Acquisition Manager")

    st.write("Ask anything related to the hiring process!")

    st.markdown("**💡 Example Questions:**")
    st.markdown("- What’s the current status of the hiring process?")
    st.markdown("- How many candidates have been shortlisted?")
    st.markdown("- Any interviews scheduled this week?")

    user_input = st.text_input("💬 Your question:")

    if user_input:
        with st.spinner("Thinking..."):
            response = handle_query(user_input)
        st.success("Done!")
        st.markdown(f"**AI Response:** {response}")
