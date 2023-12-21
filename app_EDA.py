#Import required libraries
import os 
from apikey import apikey 

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#OpenAIKey
os.environ['OPENAI_API_KEY'] = apikey
load_dotenv(find_dotenv())

# Title & Welcoming Message
st.title('Data Analyst Chatbot 📈')
st.write("Hello, 👋 I am trained to do EDA on your csv files! Click on the button below 👇 to get started!")

# Explanation Sidebar
with st.sidebar:
    st.write('**Project Overview.**')
    st.caption('''**This project was built using OpenAI API, Langchain, Python, and Streamlit. 
               Python was the programming langauge used. The OpenAI API was used to import LLM's.
               Langchain was used to import pandas agents to run specific data tasks. Streamlit was used to quickly deploy the model 
               and give it a nice user interface.**''')

    st.divider()

    st.caption("<p style ='text-align:center'> created by Matt 🏝️</p>",unsafe_allow_html=True )

# Intialise the key in session state 
if 'clicked' not in st.session_state:
    st.session_state.clicked ={1:False}

# Function to update the value in session state (so that nothing disappears when csv is uploaded)
def clicked(button):
    st.session_state.clicked[button]= True
st.button("Start EDA", on_click = clicked, args=[1])
if st.session_state.clicked[1]:
    user_csv = st.file_uploader("Upload your file here", type="csv")
    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

        # Loading the LLM Model
        llm = OpenAI(temperature=0)

        # Function Sidebar
        @st.cache_data
        def steps_eda():
            steps_eda = llm('What are the steps of EDA')
            return steps_eda

        # Pandas Agent
        pandas_agent = create_pandas_dataframe_agent(llm, df, verbose = True)

        # Pandas Agent Parameters for Data Analysis (Functions Main)
        @st.cache_data
        def function_agent():
            st.write("**Data Overview**")
            st.write("The first rows of your dataset look like this:")
            st.write(df.head())
            st.write("**Data Cleaning**")
            columns_df = pandas_agent.run("What are the meaning of the columns?")
            st.write(columns_df)
            missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
            st.write(missing_values)
            duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
            st.write(duplicates)
            st.write("**Data Summarisation**")
            st.write(df.describe())
            correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships.")
            st.write(correlation_analysis)
            outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.")
            st.write(outliers)
            new_features = pandas_agent.run("What new features would be interesting to create?.")
            st.write(new_features)
            return

        @st.cache_data
        def function_question_variable():
            st.line_chart(df, y =[user_question_variable])
            summary_statistics = pandas_agent.run(f"Give me a summary of the statistics of {user_question_variable}")
            st.write(summary_statistics)
            normality = pandas_agent.run(f"Check for normality or specific distribution shapes of {user_question_variable}")
            st.write(normality)
            outliers = pandas_agent.run(f"Assess the presence of outliers of {user_question_variable}")
            st.write(outliers)
            trends = pandas_agent.run(f"Analyse trends, seasonality, and cyclic patterns of {user_question_variable}")
            st.write(trends)
            missing_values = pandas_agent.run(f"Determine the extent of missing values of {user_question_variable}")
            st.write(missing_values)
            return
        
        @st.cache_data
        def function_question_dataframe():
            dataframe_info= pandas_agent.run(user_question_dataframe)
            st.write(dataframe_info) 

        # Main

        st.header('Exploratory Data Analysis') 
        st.subheader('General information about the dataset')

        with st.sidebar:
            with st.expander('Explortory Data Analysis Steps'):
                st.write(steps_eda())

        function_agent()

        st.subheader('Variable of Study')
        user_question_variable = st.text_input('What variable are you interested in?')
        if user_question_variable is not None and user_question_variable !="":
            function_question_variable()

            st.subheader('Further study')

        if user_question_variable:
            user_question_dataframe = st.text_input( "Is there anything else you would like to know about your dataframe?")
            if user_question_dataframe is not None and user_question_dataframe not in ("","no","No"):
                function_question_dataframe()
            if user_question_dataframe in ("no", "No"):
                st.write("")