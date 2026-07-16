# 🚀 Minimal Backend API

A Dockerized Flask backend built as part of the FlyRank Backend AI Engineering Internship.

This project demonstrates how to build a secure REST API using Flask, PostgreSQL, JWT Authentication, and Docker while following a layered backend architecture.

---

## ✨ Features

- 🔐 User Registration
- 🔑 User Login
- 🔒 JWT Authentication
- 🛡️ Protected Routes
- 🔑 Password Hashing using bcrypt
- 🐘 PostgreSQL Integration
- 🐳 Docker & Docker Compose
- 📂 Layered Architecture (Routes → Services → Repository)
- ⚙️ Environment Variable Configuration
- 🌐 RESTful API Design

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| Framework | Flask |
| Database | PostgreSQL |
| Authentication | JWT (PyJWT) |
| Password Security | bcrypt |
| Database Driver | psycopg3 |
| Containerization | Docker & Docker Compose |

---

## 📁 Project Structure

```text
minimal-backend/

├── database/
│   ├── db.py
│   └── init.sql
│
├── middleware/
│   └── auth_middleware.py
│
├── repositories/
│   ├── patient_repository.py
│   ├── user_repository.py
│   ├── memory_repository.py
│   └── repository_interface.py
│
├── routes/
│   ├── auth_routes.py
│   └── patient_routes.py
│
├── services/
│   ├── auth_service.py
│   └── patient_services.py
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🏗️ Architecture

```
             Client
                │
                ▼
          Flask Routes
                │
                ▼
          Service Layer
                │
                ▼
        Repository Layer
                │
                ▼
          PostgreSQL
```

---

## 🔑 Authentication Flow

```
User Registration

↓

Validate Input

↓

Hash Password (bcrypt)

↓

Store User

↓

Login

↓

Verify Password

↓

Generate JWT

↓

Return Token

↓

Authorization:
Bearer <JWT>

↓

Protected Endpoint
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate user and generate JWT |
| GET | `/profile` | Protected route |
| GET | `/patients` | Retrieve patients |
| POST | `/patients` | Create patient |

---

## ⚙️ Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/accessmed
JWT_SECRET=your_secret_key
```

---

## 🚀 Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Start Docker

```bash
docker compose up --build
```

The backend will be available at

```
http://localhost:5000
```

---

## 🧪 Example Requests

### Register

```http
POST /register
```

```json
{
    "username":"Satyam",
    "email":"abc@gmail.com",
    "password":"hello123"
}
```

---

### Login

```http
POST /login
```

```json
{
    "email":"abc@gmail.com",
    "password":"hello123"
}
```

---

### Protected Route

```http
GET /profile
```

Header

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📈 Future Improvements

- Refresh Tokens
- Role-Based Access Control (RBAC)
- Password Reset
- Email Verification
- SQLAlchemy ORM
- Flask-Migrate
- Swagger/OpenAPI Documentation
- Unit & Integration Testing
- GitHub Actions CI/CD
- Production Deployment

---

## 📚 Learning Outcomes

Through this project I gained practical experience with:

- Flask REST APIs
- PostgreSQL Integration
- Docker
- Docker Compose
- JWT Authentication
- Password Hashing with bcrypt
- Middleware
- Layered Backend Architecture
- Repository Pattern
- Environment-based Configuration

---

## 📄 License

This project was developed for educational purposes as part of the FlyRank Backend AI Engineering Internship.
