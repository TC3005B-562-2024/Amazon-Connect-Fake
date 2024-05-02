"""
Fake Amazon Connect API
"""

import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from data_fakeada import FakeInfo


app = Flask(__name__)
CORS(app, origins='*')
db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="",
)
fake_data = FakeInfo()

@app.errorhandler(400)
def bad_request_error(error):
    """
    Returns a 400 error when the request is invalid
    """
    error_message = f"Error {error.code}: {error.name}"
    return jsonify({"error": error_message}), 400

@app.errorhandler(404)
def not_found_error(error):
    """
    Returns a 404 error when the resource is not found
    """
    error_message = f"Error {error.code}: {error.name}"
    return jsonify({"error": error_message}), 404

@app.route('/')
def hello_world():
    """
    Returns a hello world message
    """
    return 'Hello from Flask!'

@app.route("/fake/info", methods=["POST"])
def metrics_data():
    """
    Returns fake metrics based on the alert id that is requested
    """
    data = request.json
    cursor = db.cursor()
    cursor.execute(
        "SELECT resource, is_solved FROM alert WHERE identifier = %s",
        (data["identifier"],),
    )
    result = cursor.fetchone()
    cursor.close()
    # Get the resource column from the result
    # example: "routing-profile:123456"
    if not result:
        return jsonify({"error": "Alert not found or resource is null"}), 404
    resource_arn = result[0].split(":")[0]
    is_solved = True if result[1] == 1 else False

    try:
        data_to_return = fake_data.fake_info(resource_arn, is_solved)
    except ValueError:
        return jsonify({"error": "Invalid type"}), 400
    return jsonify(data_to_return)


if __name__ == "__main__":
    app.run(debug=True)
