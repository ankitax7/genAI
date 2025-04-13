import streamlit as st

def handle_query(query):
    return f"📄 Simulated sourcing answer: '{query}'"

def sourcing_agent_interface():
    st.title("🔍 Sourcing Agent")

    st.write("I help you find the best candidates!")

    st.markdown("**💡 Example Questions:**")
    st.markdown("- Find me resumes with Python and ML experience.")
    st.markdown("- Show recent LinkedIn-sourced profiles.")
    st.markdown("- Any candidates from last month’s job post?")

    user_input = st.text_input("💬 Your sourcing query:")

    if user_input:
        with st.spinner("Searching..."):
            response = handle_query(user_input)
        st.success("Here you go!")
        st.markdown(f"**AI Response:** {response}")
