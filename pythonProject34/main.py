import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="ur API_key")


def generate_story(word1,word2,word3,wordcount):
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages =[
        {"role":"user","content":"write a story with" +word1+"\n" +word2+"\n" +word3},
        {"role":"user","content":"the story length should be"+ str(wordcount)},
    ])
    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(result)
    return result
    #return "this is a story generator"

word1 = st.text_input("enter word1: ")
word2 = st.text_input("enter word2: ")
word3 = st.text_input("enter word3: ")
wordcount = st.slider("select word count",min_value=300, max_value=1000,value=300)
submit_button = st.button("generate story")
if submit_button:
    message = st.empty()
    message.text("generating story...")
    story = generate_story(word1,word2,word3,wordcount)
    message.text("")
    st.write(story)
    st.download_button(label="download story", data=story,file_name="story.txt", mime="text/txt")