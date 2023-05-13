import secrets
from typing import Any, List, Dict

from flask import Flask, Response, request, jsonify

app = Flask(__name__)

movies: List[Dict[str, Any]] = [
    {"id": 1, "title": "The Godfather", "year": 1972, "genre": "Crime"},
    {"id": 2, "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama"},
    {"id": 3, "title": "Schindler's List", "year": 1993, "genre": "Biography"},
    {"id": 4, "title": "Raging Bull", "year": 1980, "genre": "Biography"},
    {"id": 5, "title": "Casablanca", "year": 1942, "genre": "Romance"},
    {"id": 6, "title": "Citizen Kane", "year": 1941, "genre": "Drama"},
]


@app.route("/auth", methods=["POST"])
def auth() -> Response:
    """
    Perform authentication
    """
    data: Any = request.get_json()
    if (
        {"username", "password"}.issubset(data)
        and data["username"] == "admin"
        and data["password"] == "admin"
    ):
        access_token: str = secrets.token_urlsafe()
        refresh_token: str = secrets.token_urlsafe()
        print(access_token)
        return jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "status": "success",
            }
        )
    return jsonify({"status": "login failed"}), 401


@app.route("/movies", methods=["GET"])
def get_movies() -> Response:
    """
    Get all movies
    """
    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=19003)
