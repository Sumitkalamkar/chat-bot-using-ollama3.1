from langchain_community.llms import Ollama
import streamlit as st
import asyncio

# Initialize the model
llm = Ollama(model="llama3.1")

st.title('Sam 1.1')

# Input area for prompt
prompt = st.text_area('Ask here!:')

async def generate_response(prompt):
    return llm.invoke(prompt, stop=[''])

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(generate_response(prompt))
            st.write(result)
