import os
import jwt

from functools import wraps
from flask import request, jsonify, g


def token_required(auth_service):

    def decorator(f):

        @wraps(f)
        def decorated(*args, **kwargs):

            auth_header = request.headers.get("Authorization")

            if not auth_header:
                return jsonify({
                    "error": "Authorization header missing"
                }), 401

            if not auth_header.startswith("Bearer "):
                return jsonify({
                    "error": "Invalid Authorization header"
                }), 401

            token = auth_header.split(" ")[1]

            try:

                payload = jwt.decode(
                    token,
                    os.getenv("JWT_SECRET"),
                    algorithms=["HS256"]
                )

                user = auth_service.repository.find_by_id(payload["user_id"])

                if user is None:
                    return jsonify({
                        "error": "User not found"
                    }), 401

                g.current_user = user

            except jwt.ExpiredSignatureError:
                return jsonify({
                    "error": "Token expired"
                }), 401

            except jwt.InvalidTokenError:
                return jsonify({
                    "error": "Invalid token"
                }), 401

            return f(*args, **kwargs)

        return decorated

    return decorator