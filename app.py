from flask import Flask, jsonify, g

from database.db import conn

from repositories.patient_repository import PostgresRepository
from repositories.user_repository import UserRepository

from services.patient_services import PatientService
from services.auth_service import AuthService

from routes.patient_routes import register_routes
from routes.auth_routes import register_auth_routes

from middleware.auth_middleware import token_required


app = Flask(__name__)

patient_service = PatientService(PostgresRepository(conn))
auth_service = AuthService(UserRepository(conn))

register_routes(app, patient_service)
register_auth_routes(app, auth_service)


@app.route("/")
def home():
    return {
        "message": "Hello from my backend!"
    }


@app.route("/profile")
@token_required(auth_service)
def profile():

    return jsonify(g.current_user)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )