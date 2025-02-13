from flask import Flask
import os

import docker
import schedule
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to stAItus-test!</p>"

if __name__ == "__main__":

    print("Monitoring started. Press Ctrl+C to stop.")

    port = int(os.environ.get('PORT', 5003))
    app.run(debug=False, host='0.0.0.0', port=port)

    while True:
        schedule.run_pending()
        time.sleep(1)