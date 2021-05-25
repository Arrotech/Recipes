import os

from flask import make_response, jsonify
from app import create_app


app = create_app(os.environ.get('FLASK_ENV'))


@app.route('/')
def home():
    """Redirect to home."""
    return make_response(jsonify({
        "status": "OK",
        "message": "Welcome to our recipes web services"
    }), 200)


if __name__ == '__main__':
    app.run()
