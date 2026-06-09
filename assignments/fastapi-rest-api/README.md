# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using FastAPI that handles data creation, retrieval, updating, and deletion with request validation and automatic API documentation.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Build a FastAPI application that defines a root endpoint and a set of item endpoints for basic CRUD operations.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Define a root (`/`) endpoint that returns a welcome message
- Use Pydantic models to validate request data
- Include at least one GET endpoint to list items
- Include at least one POST endpoint to create new items

### 🛠️ Add CRUD Endpoints

#### Description
Add endpoints for reading, updating, and deleting items from an in-memory data store.

#### Requirements
Completed program should:

- Define an endpoint to retrieve an item by its ID
- Define an endpoint to update an existing item by its ID
- Define an endpoint to delete an item by its ID
- Return appropriate JSON responses for success and error cases
- Make the API available at `http://127.0.0.1:8000/docs` for interactive documentation
