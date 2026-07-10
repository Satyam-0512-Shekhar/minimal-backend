# Minimal Flask Backend

A simple backend application built using Python and Flask that demonstrates the HTTP request-response cycle by exposing two JSON API endpoints.


## Features

- Built with Flask
- Two JSON API endpoints
- Lightweight and beginner-friendly
- Easy to run locally

---

## Project Structure

```
minimal-backend/
│── .venv/
│── app.py
│── requirements.txt
│── README.md
└── .gitignore
```

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.x installed
- pip (Python Package Manager)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/minimal-backend.git
cd minimal-backend
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows (Command Prompt)

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the Flask development server:

```bash
py app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## API Endpoints

### GET /

Returns a welcome message.

Response

```json
{
    "message": "Hello from my backend!"
}
```

---

### GET /about

Returns information about the developer.

Response

```json
{
    "name": "Satyam Shekhar",
    "course": "BCA",
    "backend": "Flask"
}
```

---

## Testing the API

### Using Browser

Open:

```
http://127.0.0.1:5000/
```

and

```
http://127.0.0.1:5000/about
```

---

### Using curl

```bash
curl http://127.0.0.1:5000/
```

```bash
curl http://127.0.0.1:5000/about
```

---

## Technologies Used

- Python
- Flask
- REST API
- JSON

---

## Author

Satyam Shekhar

BCA Student | Backend Development Enthusiast