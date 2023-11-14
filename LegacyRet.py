import os
import streamlit as st
import pickle
import time
import langchain

# Use the updated import for HuggingFaceHub
from langchain.llms import HuggingFaceHub

# Use the updated import for LLMChain
# from langchain.chains import LLMChain
#
# from langchain.llms import GooglePalm
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import UnstructuredURLLoader
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain import PromptTemplate
# from langchain.chat_models import ChatGooglePalm
#
# st.set_page_config(page_title="FINANCE GUIDE GENERATIVE BOT", page_icon=":books:", layout="wide", initial_sidebar_state="expanded")
#
# # Display a text heading
# st.title("Welcome to the Finance Guide Generative Bot")
#
# # Additional text content
# st.write("This is a Streamlit app for generating finance-related content.")
#
# # Add a text input area
# user_data = st.text_area("Paste or enter your financial data here:")


# import streamlit as st
# from langchain.llms import GooglePalm
# from langchain.chat_models import ChatGooglePalm
# from langchain.schema import AIMessage, HumanMessage, SystemMessage
#
# st.set_page_config(page_title="FINANCE GUIDE GENERATIVE BOT", page_icon=":books:", layout="wide",
#                    initial_sidebar_state="expanded")
#
# # Display a text heading
# st.title("Welcome to the Finance Guide Generative Bot")
#
# # Additional text content
# st.write("This is a Streamlit app for generating finance-related content.")
#
# # Add a text input area
# user_data = st.text_area("Paste or enter your financial data here:")
#
# # Add a submit button
# submit_button = st.button("Submit")
#
# # Check if user has submitted data
# if submit_button:
#     # Perform financial analysis using langchain
#     api_key = 'AIzaSyByFoyQYuNDC9jsCwdNfs8_UhgmPNJWHJI'
#     chat = ChatGooglePalm(google_api_key=api_key)
#     prompt = '''You are a financial expert who is able to analyze one's personal monthly credit card statement, bank account statement, and cash
#     expense log, and give a deep analysis on what went good, what went wrong, and recommend some actionable items to improve one's personal financial health.
#     You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good"
#     "very good"), and "recommendation" (string).
#     "analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
#     "financial health" is the rating of one's financial condition based on the analysis provided.
#     "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the upcoming month.
#     Let's start!!! '''
#
#     # Create langchain messages
#     messages = [SystemMessage(content=prompt), HumanMessage(content=user_data)]
#
#     # Perform chat-based financial analysis
#     output = chat(messages)
#
#     # Print the output to the console
#     print("Output:", output.content)
#
#     # Display the analysis output
#     # Display the analysis output as plain text
#     st.subheader("Financial Analysis Result:")
#     st.text(str(output.content))
#


# import streamlit as st
# import fitz  # PyMuPDF
# import tempfile
# from langchain.llms import GooglePalm
# from langchain.chat_models import ChatGooglePalm
# from langchain.schema import AIMessage, HumanMessage, SystemMessage



# st.set_page_config(page_title="FINANCE GUIDE GENERATIVE BOT", page_icon=":books:", layout="wide", initial_sidebar_state="expanded")

# # Display a text heading
# st.title("Welcome to the Finance Guide Generative Bot")

# # Additional text content
# st.write("This is a Streamlit app for generating finance-related content.")

# # Add a file uploader for PDF files
# pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# # Add a submit button
# submit_button = st.button("Submit")

# # Check if user has submitted data
# if submit_button and pdf_file:
#     # Save the PDF content to a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#         temp_pdf.write(pdf_file.read())

#     # Perform PDF text extraction
#     pdf_content = ""
#     pdf_reader = fitz.open(temp_pdf.name)
#     for page_number in range(pdf_reader.page_count):
#         page = pdf_reader[page_number]
#         pdf_content += page.get_text()

#     # Perform financial analysis using langchain
#     api_key = 'AIzaSyByFoyQYuNDC9jsCwdNfs8_UhgmPNJWHJI'
#     chat = ChatGooglePalm(google_api_key=api_key)

#     # Replace the static prompt with your specific prompt
#     prompt = '''
#     You are a financial expert who is able to analyze one's personal monthly credit card statement, bank account statement, and cash
#     expense log, and give a deep analysis on what went good, what went wrong, and recommend some actionable items to improve one's personal financial health.
#     You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good"
#     "very good"), and "recommendation" (string).
#     "analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
#     "financial health" is the rating of one's financial condition based on the analysis provided.
#     "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the upcoming month.
#     Let's start!!!
#     '''

#     # Create langchain messages
#     messages = [SystemMessage(content=prompt), HumanMessage(content=pdf_content)]

#     # Perform chat-based financial analysis
#     output = chat(messages)

#     # Display the analysis output as plain text
#     st.subheader("Financial Analysis Result:")
#     st.text(str(output.content))

#     # Remove the temporary file
#     temp_pdf.close()


# with st.container():
#     with st.sidebar:
#         members = [
            
#         ]

#         st.markdown("<h1 style='font-size:28px'>Team Members</h1>", unsafe_allow_html=True)

#         for member in members:
#             st.write(f"Name: {member['name']}")
#             st.write(f"Email: {member['email']}")
#             st.write(f"LinkedIn: {member['linkedin']}")
#             st.write("")


# with st.container():
#     st.write("---")
#     st.header("Your Valuable feedback appricable!")
#     st.write("##")

#     # Adding some vertical space
#     st.write("\n\n\n")

#     contact_form = """
#     <form action="https://formsubmit.co/rohan.saraswat2003@gmail.com" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
#         <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
#         <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"></textarea><br>
#         <button type="submit" style="width: 100%; padding: 10px; border-radius: 10px; background-color: #4CAF50; color: white;">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)

#     with right_column:
#         st.empty()


import streamlit as st
import fitz  # PyMuPDF
import tempfile
from langchain.llms import GooglePalm
from langchain.chat_models import ChatGooglePalm
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the chat model
api_key = 'AIzaSyByFoyQYuNDC9jsCwdNfs8_UhgmPNJWHJI'
chat_model = ChatGooglePalm(google_api_key=api_key)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="Finance Guide Generative Bot", page_icon=":books:", layout="wide", initial_sidebar_state="expanded")

# Introduction message
st.title("Finance Guide Generative Bot")
st.write("I am your financial advisor. You can chat with me or upload the PDF of your financial data.")

# Set initial prompt for financial analysis
initial_prompt = '''
You are a financial expert who is able to analyze one's personal monthly credit card statement, bank account statement, and cash
expense log, and give a deep analysis on what went good, what went wrong, and recommend some actionable items to improve one's personal financial health.
You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good"
"very good"), and "recommendation" (string).
"analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
"financial health" is the rating of one's financial condition based on the analysis provided.
"recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the upcoming month.
Let's start!!!
'''

# Live Chat Section
st.subheader("Iam your finincial guide input your documents")

# Create a placeholder for live chat messages
chat_messages_placeholder = st.empty()

# Add initial prompt as a system message only if it's not in the conversation
if not any(isinstance(message, SystemMessage) for message in st.session_state.messages):
    st.session_state.messages.append(SystemMessage(content=initial_prompt))

user_input = st.text_input("Type your message:")
submit_chat_button = st.button("Submit Chat")

pdf_upload = st.file_uploader("Upload a PDF file", type=["pdf"])
submit_pdf_button = st.button("Submit PDF")

def perform_chat(messages):
    try:
        # Get model response
        model_response = chat_model(messages)

        # Add model response to the conversation
        st.session_state.messages.append(AIMessage(content=model_response.content))

        # Display ongoing chat conversation in a text box
        chat_text = ""
        for message in st.session_state.messages:
            if isinstance(message, HumanMessage):
                chat_text += f"User: {message.content}\n"
            elif isinstance(message, AIMessage):
                chat_text += f"Model: {message.content}\n"

        chat_messages_placeholder.text_area("Chat Conversation", value=chat_text, height=200)

    except Exception as e:
        # Handle the exception gracefully
        st.error(f"An error occurred: {str(e)}")

try:
    if submit_chat_button and user_input:
        # Add user message to the conversation
        st.session_state.messages.append(HumanMessage(content=user_input))

        # Perform the chat
        perform_chat(st.session_state.messages)

    if submit_pdf_button and pdf_upload:
        # Save the PDF content to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(pdf_upload.read())

        # Clear previous messages and add the initial prompt
        st.session_state.messages = [SystemMessage(content=initial_prompt)]

        # Add user's PDF content to the conversation
        st.session_state.messages.append(HumanMessage(content=temp_pdf.name))

        # Perform the chat
        perform_chat(st.session_state.messages)

except Exception as e:
    # Handle the exception gracefully
    st.error(f"An error occurred: {str(e)}")

# Clear chat session
clear_chat_button = st.button("Clear Chat")
if clear_chat_button:
    st.session_state.messages = []
    chat_messages_placeholder.text_area("Chat Conversation", value="", height=200)










