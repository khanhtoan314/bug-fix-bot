"""
This file is called streamlit_app.py.

This is where the streamlit app code lives, which is run by the streamlit framework.
and the main entry point for the user interface, that allows users to interact with the application.
the bug-fix bot. 

"""

# Import necessary libraries
import streamlit as st
from bug_detection_device import bug_detector
import time

# Set up the page configuration of the app
st.set_page_config(
    page_title="Bug-Fix Bot: Your AI Coding Assistant",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Header of the app
st.title("🐞 Bug-Fix Bot: Your AI Coding Assistant")
st.markdown("""
    Welcome to Bug-Fix Bot! This AI-powered assistant helps you 
    identify and fix bugs in your code snippets.

    All you need to do is paste your code into the input box below, 
    and click the "Detect Bugs" button.
    The bot will analyze your code and provide suggestions for improvements.               

    *Powered by Google Gemini via Vertex AI.*
            
"""    
)

# Footer of the app
st.markdown("""---""")
st.markdown("""
<div style="text-align: center;">
    <p> Developed by Khanh Toan Nguyen | Artificial Intelligence Class | Fall 2025
<div>
""", unsafe_allow_html=True)

# Code for the input of the app
st.subheader("Paste Your Code Snippet Below:")

user_code = st.text_area(
    label="Please paste your code snippet here:",
    height=280,
    placeholder="""e.g., def greet(name):\n    
    print(f'Hello, {name}!')
        
greet("World")
"""    
)

# Detector button of the app
if st.button("Detect Bugs"):
    if not user_code.strip():
        st.warning("Please enter a code snippet to analyze.")
    else:
        with st.spinner("Analyzing your code for bugs..."):
            start_time = time.time()
            bugs_found = bug_detector(user_code)
            end_time = time.time()
            time.sleep(2)  # Simulate processing time

        # Response time calculation
        response_time = end_time - start_time    
        
        # Displaying the results
        st.subheader("Analysis Results:")

        if "System Error" in bugs_found['bug']:
            st.error(bugs_found['bug'])
        else:
            st.markdown("**Bugs Detected:**")
            st.error(bugs_found['bug'])

            st.markdown("**Suggested Fixes:**")
            st.success(bugs_found['fix'])

            st.caption(f"Response Time: {response_time:.2f} seconds")
