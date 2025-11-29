import streamlit as st
import google.generativeai as genai


key = "AIzaSyAC6YmhQvZUzjUNljOWO-RPiPFkRis9RtE"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")


st.title("my bot")
st.write("aao baat kare")



user_input = st.chat_input("Type your message...")


if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    response = model.generate_content(user_input).text


    
    with st.chat_message("assistant"):
        st.write(response)
