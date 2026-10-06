# Job Application Tracker API

A REST API for tracking job applications, built with FastAPI, SQLAlchemy, and SQLite.

## Features

- Create job applications
- View all applications
- View an application by ID
- Update application details
- Delete applications
- Health-check endpoint

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API from the project root:

```bash
uvicorn app.main:app --reload
```

Open Swagger API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Check whether the API is running |
| POST | `/applications` | Create a job application |
| GET | `/applications` | Get all job applications |
| GET | `/applications/{application_id}` | Get one job application |
| PATCH | `/applications/{application_id}` | Update an application |
| DELETE | `/applications/{application_id}` | Delete an application |
