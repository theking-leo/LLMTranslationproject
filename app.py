import streamlit as st
import boto3
import openai
import time


# Set your OpenAI API Key
openai.api_key = "your_openai_api_key"

# AWS Textract: Extract text from file
def extract_text_from_file(file):
    """
    Use AWS Textract to extract text from uploaded files.
    """
    client = boto3.client('textract', region_name='us-east-1')  # Specify your AWS region
    response = client.analyze_document(
        Document={'Bytes': file.read()},
        FeatureTypes=['TABLES', 'FORMS']
    )
    extracted_text = ''
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + '\n'
    return extracted_text

# AWS Translate: Translate extracted text
def translate_text(text, target_language):
    """
    Use AWS Translate to translate text into the selected language.
    """
    client = boto3.client('translate', region_name='us-east-1')  # Specify your AWS region
    response = client.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode=target_language
    )
    return response['TranslatedText']

# OpenAI GPT-4: Summarize text
def summarize_text(text):
    """
    Use OpenAI GPT-4 to summarize the translated text.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ]
        )
        summary = response["choices"][0]["message"]["content"].strip()
        return summary
    except Exception as e:
        return f"Error summarizing text: {e}"

# OpenAI GPT-4: Answer user questions
def ask_chatbot(question, context):
    """
    Use OpenAI GPT-4 to answer questions based on the provided context.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers questions based on the provided context."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ]
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return answer
    except Exception as e:
        return f"Error in chatbot response: {e}"

# Streamlit App
st.title("Pathfinder AI")
st.sidebar.title("Settings")
st.subheader("Your Guide for Immigrants and Job Seekers Moving Abroad")


# Language selection
language_options = [
    ("English", "en"),
    ("Spanish", "es"),
    ("French", "fr"),
    ("Chinese", "zh"),
    ("Danish", "da"),
    ("Vietnamese", "vi"),
    ("German", "de")
]
target_language = st.sidebar.selectbox("Select Target Language", language_options, format_func=lambda x: x[0])

# Initialize placeholders for document content
extracted_text = ""
translated_text = ""
summary = ""

# File uploader
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "jpg", "png"])

if uploaded_file:
    st.write(f"File uploaded: {uploaded_file.name}")
    
    try:
        # Extract text from uploaded file
        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_file(uploaded_file)

        # Translate extracted text
        with st.spinner("Translating text..."):
            translated_text = translate_text(extracted_text, target_language[1])

        # Summarize translated text
        with st.spinner("Summarizing text..."):
            summary = summarize_text(translated_text)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

# Display extracted text, translation, and summary
st.subheader("Extracted Text")
st.text_area("Extracted Text", value=extracted_text, height=200)

st.subheader("Translated Text")
st.text_area("Translated Text", value=translated_text, height=200)

st.subheader("Summary")
st.text_area("Summary", value=summary, height=100)

# Chatbot interaction
st.subheader("Ask Questions About the Document")
question = st.text_input("Enter your question here:")
if question:
    with st.spinner("Thinking..."):
        answer = ask_chatbot(question, translated_text or extracted_text)
    st.write("Chatbot Response:")
    st.write(answer)

# Provide a download button for the translated text
if translated_text:
    st.download_button(
        label="Download Translated Text",
        data=translated_text,
        file_name="translated_text.txt",
        mime="text/plain"
    )
