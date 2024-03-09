# Data Analysis Chatbot 📈

## A Streamlit Chatbot that does Exploratory Analysis on csv Files

The purpose of the chatbot is to show data cleaning suggestions, correlations, potentional outliers, variable creation suggestions, and skewness in the data of a given csv file. The following project is made up of the following main components: 

- Python to code the chatbot
- OpenAI's API to access large language models
- Langchain to import Pandas Agents to answer specific questions about the csv
- Streamlit to host the chatbot and create a nice user interface
- VS code to edit and test everything

## Here is a Demo of the Project

https://github.com/mattkope/Data-Analysis-Chatbot/assets/133834623/ba9b9140-6958-443f-a17c-242a0d7ffce8

## Installation Instructions

1. Clone the git repository using the command: `git clone`
2. Get a OpenAI API Key from [OpenAI](https://platform.openai.com/api-keys) and then paste it into the apikey.py file.
3. Open the folder in VS code and create a [Python environment](https://code.visualstudio.com/docs/python/environments). The Python version used was 3.11. Then open up the command prompt in VS code and type the following: `pip install -r requirements.txt`.
4. Once everything has been installed type the following in the command prompt in VS code to run the Streamlit app: `streamlit run app_EDA.py`
5. Input the twitter csv file or your own to start the data analysis
6. If you so choose to, you can then deploy the model online using Streamlit as host. You just need to create an online account. 

## Recommended Documentation if you want to Tweak the Program

- [Streamlit documentation](https://docs.streamlit.io/)
- [LangChain documentation](https://python.langchain.com/docs/get_started/introduction) 
- [OpenAI API documentation](https://platform.openai.com/docs/introduction)

## Known Issues

The further study portion of the chatbot only appears after a second variable has been inputted into the exploratory field. 

## Known Issues

The further study portion of the chatbot onloy appears after a second variable has been inputted into the exploratory field. 
