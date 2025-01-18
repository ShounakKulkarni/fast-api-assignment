# fast-api-assignment

## Prerequisites
Before you begin, make sure you have the following installed:

Python 3.7 or higher

pip (Python package installer)

MongoDB (or use a cloud MongoDB service like MongoDB Atlas)

## Installation
Follow these steps to set up the project on your local machine.

### Clone the Repository

Clone the repository to your local machine using Git:

``
git clone https://github.com/ShounakKulkarni/fast-api-assignment.git
``

``
cd fast-api-assignment
``


### Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies.
``
python3 -m venv venv
``

### Activate the Virtual Environment

#### On Windows:
``
venv\Scripts\activate
``

#### On macOS/Linux:
``
source venv/bin/activate
``

### Install Dependencies
``
pip install fastapi uvicorn pymongo
``
fastapi: The FastAPI framework for building the API.

uvicorn: The ASGI server for running FastAPI.

pymongo: MongoDB client to connect and interact with MongoDB.

## Setting Up MongoDB
If you're using MongoDB locally, make sure MongoDB is installed and running on your machine. Alternatively, you can use MongoDB Atlas (a cloud-hosted MongoDB service). You will need to update the connection URI in your FastAPI code to point to your MongoDB instance.
Running the API Server

Once the dependencies are installed and MongoDB is set up, you can run the FastAPI application using Uvicorn:

``
uvicorn main:app --reload
``

## Access the API
Once the server is running, you can access the API by opening a browser and navigating to:

``
http://127.0.0.1:8000
``
The FastAPI app also generates interactive API documentation, which you can access at:

Swagger UI: http://127.0.0.1:8000/docs

