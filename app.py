from flask import Flask, render_template, jsonify
import json

app = Flask(__name__, template_folder='.')

with open('file.json', 'r') as f:
    data = json.load(f)

@app.route("/")
def index():
    return render_template('index.html', title="page", jsonfile=json.dumps(data))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
