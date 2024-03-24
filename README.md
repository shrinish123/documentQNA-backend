# 'AI Planet - QnA with Document' --Backend

 AI Planet - QnA with Document Backend is built with FastAPI-Python, SQLite and with help of OpenAI Models along with LangChain.

# About 

The backend currently stores documents uploaded in the File management system itself and with the help of Langchain and OpenAI models and is able to answer questions related to document along with contextual chat history related to that document.


# Setting up the Project

* Make sure you have python installed.
* Clone the repository to your local machine
```bash
 git clone https://github.com/<your-github-username>/documentQNA-backend.git
```
* Change directory to documentQNA-backend
 ```bash
 cd  documentQNA-backend
 ```
* Create a virtual environment
 ```bash
 python -m venv venv
 ```
* Activate the virtual environment (For Windows)
 ```bash
 .\venv\scripts\activate  
 ``` 

* Install the dependencies : 
 ```bash
 pip install -r requirements.txt
 ```
* Configure the .env file by copy pasting the .env.example file and create a new .env file and add your API keys as required 

* To start running project locally:
```bash
  uvicorn api.app:app 
 ```
* The server would be up and running on http://localhost:8000

# API Documentation 

* To upload a document :

```bash
  URL : 'http://localhost:8000/document/create'
  body : file : [Your_document]

  Example_Response : 
  {
    "id" : 1,
    "title" : "file_name",
    "path" : "path to file where it is uploaded in backend directory"
  }
 ```

* To get an answer corresponding to document :

```bash
  URL : 'http://localhost:8000/chat_message/get_answer{doc_id}'
  body : question : "example question"

  Example_Response : "answer to the question"
 ```

# Application Architecture

* The backend consists of 3 major folders : 
  1. api 
  2. engine
  3. docs <br> 
  Apart from this we have configuration files like data.db as sqlite database,.env files, requirements.txt, .gitginore files.

* The api folder has a standard structure with the following structure:
  1. models 
  2. routers  <br> 
  These folders consist of the respective entity files for the models and routers respectively. <br> 
  THe app.py is the main file where the server is initiated. <br> 
  Config file for easier switching of environments.  <br> 
  database file for Database configurations and intiation.  <br> 

* The engine is where we process the document and with the context of chat history we answer the question being asked.  <br> 
  The main.py consists of all the processing and returns the answer and also makes sure that question answer gets appended to chat history.  <br> 
  utils.py consists of some other helper functions required for the engine.  <br> 

* docs  <br> 
  This is where we are storing all the files currently and will be processed by the engine.



