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


import streamlit as st
import fitz  # PyMuPDF
import tempfile
from langchain.llms import GooglePalm
from langchain.chat_models import ChatGooglePalm
from langchain.schema import AIMessage, HumanMessage, SystemMessage



st.set_page_config(page_title="FINANCE GUIDE GENERATIVE BOT", page_icon=":books:", layout="wide", initial_sidebar_state="expanded")

# Display a text heading
st.title("Welcome to the Finance Guide Generative Bot")

# Additional text content
st.write("This is a Streamlit app for generating finance-related content.")

# Add a file uploader for PDF files
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Add a submit button
submit_button = st.button("Submit")

# Check if user has submitted data
if submit_button and pdf_file:
    # Save the PDF content to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_file.read())

    # Perform PDF text extraction
    pdf_content = ""
    pdf_reader = fitz.open(temp_pdf.name)
    for page_number in range(pdf_reader.page_count):
        page = pdf_reader[page_number]
        pdf_content += page.get_text()

    # Perform financial analysis using langchain
    api_key = 'AIzaSyByFoyQYuNDC9jsCwdNfs8_UhgmPNJWHJI'
    chat = ChatGooglePalm(google_api_key=api_key)

    # Replace the static prompt with your specific prompt
    prompt = '''
    You are a financial expert who is able to analyze one's personal monthly credit card statement, bank account statement, and cash
    expense log, and give a deep analysis on what went good, what went wrong, and recommend some actionable items to improve one's personal financial health.
    You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good"
    "very good"), and "recommendation" (string).
    "analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
    "financial health" is the rating of one's financial condition based on the analysis provided.
    "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the upcoming month.
    Let's start!!!
    '''

    # Create langchain messages
    messages = [SystemMessage(content=prompt), HumanMessage(content=pdf_content)]

    # Perform chat-based financial analysis
    output = chat(messages)

    # Display the analysis output as plain text
    st.subheader("Financial Analysis Result:")
    st.text(str(output.content))

    # Remove the temporary file
    temp_pdf.close()


with st.container():
    with st.sidebar:
        members = [
            
        ]

        st.markdown("<h1 style='font-size:28px'>Team Members</h1>", unsafe_allow_html=True)

        for member in members:
            st.write(f"Name: {member['name']}")
            st.write(f"Email: {member['email']}")
            st.write(f"LinkedIn: {member['linkedin']}")
            st.write("")


with st.container():
    st.write("---")
    st.header("Your Valuable feedback appricable!")
    st.write("##")

    # Adding some vertical space
    st.write("\n\n\n")

    contact_form = """
    <form action="https://formsubmit.co/rohan.saraswat2003@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"></textarea><br>
        <button type="submit" style="width: 100%; padding: 10px; border-radius: 10px; background-color: #4CAF50; color: white;">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()






