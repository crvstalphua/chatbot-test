import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title='WorkChats - An LLM-powered chatbot')

with st.sidebar:
    st.title('WorkChats :)')

    st.markdown('''
    ## How to Use
    This chatbot will answer all of your workpass related questions!
    Simply type in your queries and give it a minute.
    ''')

    add_vertical_space(5)
    st.write('Made by crvstalphua, referenced: [Streamlit](<https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/>)')

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi! I'm WorkChats, here to help you out!"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi']

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()

def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path='cookies.json')
    response = chatbot.chat(prompt)
    return response

with response_container: 
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))

#link: https://crvstalphua-chatbot-test-streamlit-app-ig5flz.streamlit.app/