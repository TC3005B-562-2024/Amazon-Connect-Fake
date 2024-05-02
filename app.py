"""
Fake Amazon Connect API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from data_fakeada import FakeInfo


app = Flask(__name__)
CORS(app, origins="*")
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


@app.route("/")
def hello_world():
    """
    Returns a hello world message
    """
    return "Hello from Flask!"


@app.route("/fake/info", methods=["POST"])
def metrics_data():
    """
    Returns fake metrics based on the alert id that is requested
    """
    try:
        data = request.json
        alert_id = data.get("alertId")
        resource_arn = data.get("resourceArn").split(":")[0]
        is_solved = data.get("isSolved")
        try:
            data_to_return = fake_data.fake_info(alert_id, resource_arn, is_solved)
        except ValueError:
            return jsonify({"error": "Invalid type"}), 400
        return jsonify(data_to_return)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
