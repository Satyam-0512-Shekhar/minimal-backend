from flask import Flask

from database.db import conn
from repositories.postgres_repository import PostgresRepository
from services.patient_services import PatientService
from routes.patient_routes import register_routes

app = Flask(__name__)

service = PatientService(PostgresRepository(conn))

register_routes(app, service)

@app.route("/")
def home():
    return {"message": "Hello from my backend!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)