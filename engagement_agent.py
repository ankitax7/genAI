import streamlit as st

def handle_query(query):
    return f"📧 Engagement message for: '{query}'"

def engagement_agent_interface():
    st.title("💬 Engagement Agent")

    st.write("I help craft messages to engage candidates!")

    st.markdown("**💡 Example Prompts:**")
    st.markdown("- Write a follow-up email for the interview.")
    st.markdown("- Create a message to invite for screening.")
    st.markdown("- Compose a rejection message politely.")

    user_input = st.text_input("💬 Your messaging prompt:")

    if user_input:
        with st.spinner("Composing..."):
            response = handle_query(user_input)
        st.success("Message ready!")
        st.markdown(f"**AI Response:** {response}")
