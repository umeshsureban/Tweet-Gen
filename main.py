#pip install --upgrade langchain langchain-google-genai streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain  
from langchain import PromptTemplate

import  os

os.environ['Google_api_key'] = "AIzaSyA1H7mh9IfTN0Exu9xykMTBmHdSOy5Qvhc"

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

# Example of using the LLM chain
response = tweet_chain.invoke({"number" : 5, "topic" : "Wars in Middle East"})

print(response.content)


#Sreamlit - frontend creation
import streamlit as st

st.header("MYDY Tweet generator")
          
st.subheader("generate tweets using Gen AI")

topic = st.text_input("Topic")

Number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("generate"):
    tweets = tweet_chain.invoke({"number" : Number, "topic" : topic})
    st.write(tweets.content)
    