import streamlit as st

def handle_query(query):
    return f"✅ Screening output for: '{query}'"

def screening_agent_interface():
    st.title("📝 Screening Agent")

    st.write("I screen candidates based on job descriptions!")

    st.markdown("**💡 Example Questions:**")
    st.markdown("- Does this resume match the job description?")
    st.markdown("- Highlight skills for a data analyst role.")
    st.markdown("- Who has experience with Django?")

    user_input = st.text_input("💬 Your screening query:")

    if user_input:
        with st.spinner("Screening..."):
            response = handle_query(user_input)
        st.success("Screened!")
        st.markdown(f"**AI Response:** {response}")
