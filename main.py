from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Crash Docker</title>
<h1>Crash Docker Container</h1>
<form method="POST">
    <button type="submit">Crash Now</button>
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os._exit(1)  # This forcefully kills the process (crashes container)
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
