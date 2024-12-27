# LLM Translation and Chatbot Project

This project is a **Streamlit web application** designed to assist users with translating documents and providing chatbot functionality for questions about the document. It leverages **AWS Textract** for document text extraction, **AWS Translate** for translations, and **OpenAI's GPT-4 API** for chatbot functionality.

The app is deployed on **Streamlit Cloud**, and you can access it here: [LLM Translation App](https://your-app-name.streamlit.app).

---

## Features

1. **Document Upload**:
   - Supports **PDF**, **JPG**, **PNG**, and other common formats.
   - Extracts text using **AWS Textract**.

2. **Translation**:
   - Translates extracted text into multiple languages using **AWS Translate**.
   - Supported languages: English, Spanish, French, German, Chinese, Vietnamese, and Danish.

3. **Chatbot**:
   - Allows users to ask questions about the document.
   - Powered by **OpenAI GPT-4** for real-time answers.

4. **Download Translated Text**:
   - Users can download the translated text as a plain text file.

---

## Installation

To run the app locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/theking-leo/LLMTranslationproject.git
cd LLMTranslationproject

### 2. Create a Virtual Environment
It’s recommended to use a virtual environment for dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
Install the required libraries listed in requirements.txt:
pip install -r requirements.txt

### 4. Configure AWS and OpenAI
AWS Configuration: Set up your AWS credentials in ~/.aws/credentials or configure them in the code.
OpenAI API Key: Add your OpenAI API key to the app.py file.

###5. Run the Application
Run the Streamlit app locally:
streamlit run app.py
Deployment
The application is deployed on Streamlit Cloud and can be accessed via this link:

👉 LLM Translation App

Project Structure
LLMTranslationproject/
├── app.py                # Main Streamlit application file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── LLM_Translation.ipynb # Optional: Jupyter notebook for initial prototyping


Dependencies
Python 3.7+
Streamlit (Web Framework)
Boto3 (AWS SDK for Python)
OpenAI API (For chatbot functionality)
To install the dependencies, run:

pip install -r requirements.txt



Here’s a comprehensive README.md file tailored for your LLM Translation Project. It includes all the necessary details about the project, its functionality, and the deployment on Streamlit.

markdown
Copy code
# LLM Translation and Chatbot Project

This project is a **Streamlit web application** designed to assist users with translating documents and providing chatbot functionality for questions about the document. It leverages **AWS Textract** for document text extraction, **AWS Translate** for translations, and **OpenAI's GPT-4 API** for chatbot functionality.

The app is deployed on **Streamlit Cloud**, and you can access it here: [LLM Translation App](https://your-app-name.streamlit.app).

---

## Features

1. **Document Upload**:
   - Supports **PDF**, **JPG**, **PNG**, and other common formats.
   - Extracts text using **AWS Textract**.

2. **Translation**:
   - Translates extracted text into multiple languages using **AWS Translate**.
   - Supported languages: English, Spanish, French, German, Chinese, Vietnamese, and Danish.

3. **Chatbot**:
   - Allows users to ask questions about the document.
   - Powered by **OpenAI GPT-4** for real-time answers.

4. **Download Translated Text**:
   - Users can download the translated text as a plain text file.

---

## Installation

To run the app locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/theking-leo/LLMTranslationproject.git
cd LLMTranslationproject
2. Create a Virtual Environment
It’s recommended to use a virtual environment for dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Install the required libraries listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Configure AWS and OpenAI
AWS Configuration: Set up your AWS credentials in ~/.aws/credentials or configure them in the code.
OpenAI API Key: Add your OpenAI API key to the app.py file.
5. Run the Application
Run the Streamlit app locally:

bash
Copy code
streamlit run app.py
The app will be accessible at http://localhost:8501.

Deployment
The application is deployed on Streamlit Cloud and can be accessed via this link:

👉 LLM Translation App

Project Structure
bash
Copy code
LLMTranslationproject/
├── app.py                # Main Streamlit application file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── LLM_Translation.ipynb # Optional: Jupyter notebook for initial prototyping
Dependencies
Python 3.7+
Streamlit (Web Framework)
Boto3 (AWS SDK for Python)
OpenAI API (For chatbot functionality)
To install the dependencies, run:


pip install -r requirements.txt
Future Improvements
Add more supported languages for translation.
Enhance error handling for unsupported file types.
Improve chatbot context handling.


Author
Developed by theking-leo
Feel free to connect or contribute to the project via GitHub!

Acknowledgments
AWS for Textract and Translate services.
OpenAI for GPT-4 API.
Streamlit for providing an easy-to-use framework for building interactive web apps.

---

### Instructions:
1. Replace **`https://your-app-name.streamlit.app`** with your actual Streamlit deployment link.
2. Save this content as `README.md` in the root of your project directory.
3. Add and push it to GitHub:
   ```bash
   git add README.md
   git commit -m "Add comprehensive README.md"
   git push origin main

