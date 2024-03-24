# AI Planet - QnA with Document Backend

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


