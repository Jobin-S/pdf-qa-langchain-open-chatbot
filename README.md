

# LLM Chat App for PDF Q&A

This repository contains code for an application that uses LangChain and OpenAI's LLM model to create a question-answering bot for PDF documents. Users can upload a PDF file, ask questions about its content, and receive answers from the bot.

Live Link - https://pdf-langchain-openai-chatbot.streamlit.app/

## Features

- Upload PDF: Users can upload a PDF file containing the document they want to inquire about.
- Ask Questions: Users can input questions related to the content of the PDF document.
- Get Answers: The application uses LangChain and OpenAI's LLM model to analyze the PDF document and provide answers to the user's questions.

## Technologies Used

- [Streamlit](https://streamlit.io/): Used for building the web application interface.
- [LangChain](https://python.langchain.com/): Provides text processing and analysis functionalities.
- [OpenAI](https://platform.openai.com/docs/models) LLM Model: Used for natural language processing tasks.
- [PyPDF2](https://pythonhosted.org/PyPDF2/): Used for reading PDF files.
- [FAISS](https://github.com/facebookresearch/faiss): Used for similarity search functionality.
- [dotenv](https://pypi.org/project/python-dotenv/): Used for loading environment variables.
- [pickle](https://docs.python.org/3/library/pickle.html): Used for serializing and deserializing Python objects.

## Usage

To use the application, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Set up your OpenAI API key by creating a `.env` file and adding your key as `OPENAI_API_KEY=your_api_key`.
3. Run the application using `streamlit run app.py`.
4. Upload a PDF file containing the document you want to inquire about.
5. Input your questions in the provided text input field.
6. Press Enter key to receive answers from the bot.

## Contributors

- [Jobin Selvanose](https://www.linkedin.com/in/jobinselvanose/): Creator of the application.

## Acknowledgments

Special thanks to Streamlit, LangChain, OpenAI, PyPDF2, FAISS, dotenv, and pickle for providing the tools and libraries necessary to build this application.

## License

This project is licensed under the MIT License - see the ([LICENSE](https://raw.githubusercontent.com/Jobin-S/pdf-qa-langchain-open-chatbot/main/LICENSE) file for details.
