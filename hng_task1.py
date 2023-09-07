from flask import Flask, jsonify, request
from datetime import datetime

# Create an instance of Flask
app = Flask(__name__)


# Create a route
@app.route('/api')
def index():
    """returns a json response of of specific hng info"""
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = "https://github.com/Uthmanduro/HNG_tasks/hng_task1.py"
    github_repo_url = "https://github.com/Uthmanduro/HNG_tasks"
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = datetime.utcnow().strftime("%A")
    status_code = 200

    return jsonify({"slack_name": slack_name, "current_day": current_day, "current_time": current_time, "track": track, "github_file_url": github_file_url, "github_repo_url": github_repo_url, "status_code": status_code}), status_code


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
