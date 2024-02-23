"""
This is just a basic template for implementation of Gpt Api using langchain
"""

## integrating with openapi
import os
from constants import openapi_key
from langchain.llms import OpenAI
import streamlit as st

#importing and setting api key
os.environ["OPENAI_API_KEY"] = openapi_key

#ui streamlit
st.title("LangChain Demo With Open API First One")
input_text= st.text_input("Enter the topic u want to serach: ")


##openapi connecting and instancing model
llm = OpenAI(temperature=0.6)


##condition input inserted or not and inputting into model 

if input_text:
    try:
        output = llm(input_text)
        st.write(output)
    except:
        output = "Quota Exceeded"
        st.write(output)

else:
    output = "Enter Description to search bully~~?"
    st.write(output)
