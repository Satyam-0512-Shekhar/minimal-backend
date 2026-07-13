# Containerized Flask + PostgreSQL Backend

A minimal Flask backend demonstrating the Repository Pattern with PostgreSQL running in Docker. This project replaces an in-memory repository with a PostgreSQL repository while keeping the service and route layers unchanged.

---

## Assignment

**Code:** BE-04  
**Track:** Backend AI Engineering  
**Phase:** Foundations

---

## Features

- Flask REST API
- PostgreSQL running in Docker
- Docker Compose for running the entire stack
- Repository Pattern
- Service Layer
- Environment variables using `.env`
- Persistent PostgreSQL storage using Docker Volumes

---

## Project Structure

```text
minimal-backend/
│
├── database/
│   ├── db.py
│   └── init.sql
│
├── repositories/
│   ├── repository_interface.py
│   ├── memory_repository.py
│   └── postgres_repository.py
│
├── routes/
│   └── patient_routes.py
│
├── services/
│   └── patient_services.py
│
├── .env.example
├── .gitignore
├── app.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Architecture

```text
Postman
      │
      ▼
Flask Routes
      │
      ▼
Patient Service
      │
      ▼
Repository Interface
      │
 ┌────┴──────────┐
 │               │
 ▼               ▼
Memory      PostgreSQL
Repository   Repository
```

Only the repository implementation changes.

The service layer and route layer remain unchanged.

---

# Technologies Used

- Python 3.12
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Psycopg 3
- python-dotenv

---

# Setup

## Clone Repository

```bash
git clone <repository-url>
cd minimal-backend
```

---

## Create Environment File

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/accessmed
```

---

## Run the Project

```bash
docker compose up --build
```

The entire stack (Flask + PostgreSQL) starts with one command.

---

# API Endpoints

## GET Patients

```http
GET /patients
```

Response

```json
[]
```

---

## Create Patient

```http
POST /patients
```

Request

```json
{
    "name": "Satyam",
    "age": 20,
    "disease": "Flu"
}
```

Response

```json
{
    "id": 1,
    "name": "Satyam",
    "age": 20,
    "disease": "Flu"
}
```

---

# Repository Swap

The application follows the Repository Pattern.

Initially, data could be stored using the in-memory repository.

For this assignment, the repository implementation was changed to PostgreSQL.

No changes were required in:

- Service Layer
- Route Layer

Only the repository implementation changed.

---

# Database Initialization

Database tables are automatically created using

```text
database/init.sql
```

when PostgreSQL starts for the first time.

---

# Persistence Verification

Persistence was verified using the following process:

1. Started the application using

```bash
docker compose up
```

2. Created patient records using the POST endpoint.

3. Verified records using the GET endpoint.

4. Stopped the containers.

```bash
docker compose down
```

5. Started the stack again.

```bash
docker compose up
```

6. Retrieved the records again using

```http
GET /patients
```

The records remained available, confirming that PostgreSQL data persisted through the Docker volume.

---

# Environment Variables

`.env` is excluded from Git.

A sample configuration is provided in

```text
.env.example
```

---

# Docker Volume

PostgreSQL uses a named Docker volume for persistent storage.

This ensures that data survives container restarts.

---

# Requirements

Install dependencies locally (optional):

```bash
pip install -r requirements.txt
```

---

# Future Improvements

- JWT Authentication
- Redis Caching
- User Management
- CRUD Operations
- API Validation
- Logging
- Unit Testing

---

# Author

Satyam Shekhar

Backend AI Engineering Track