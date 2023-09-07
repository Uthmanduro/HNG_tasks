from flask import Flask, jsonify, request
from datetime import datetime
import time

# Create an instance of Flask
app = Flask(__name__)


def get_validated_time():
    """returns a valid time with a difference of 2 seconds"""
    format = "%Y-%m-%dT%H:%M:%SZ"
    current_time = datetime.utcnow()
    time.sleep(1)
    new_current_time = datetime.utcnow()
    time_difference = (new_current_time - current_time).total_seconds()
    if abs(time_difference) <= 2:
        return new_current_time.strftime(format)
    else:
        return "Invalid time"


# Create a route
@app.route('/api')
def index():
    """returns a json response of of specific hng info"""

    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current file url in repo
    github_file_url = "https://github.com/Uthmanduro/HNG_tasks/blob/main/hng_task1.py"

    # Get current repo url
    github_repo_url = "https://github.com/Uthmanduro/HNG_tasks"

    # Get current time with validation of 2 seconds
    current_time = get_validated_time()

    # Get current day
    current_day = datetime.utcnow().strftime("%A")
    status_code = 200

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }
    # Return a json response
    return jsonify(response), status_code


# Run the app
if __name__ == '__main__':
    app.run()
