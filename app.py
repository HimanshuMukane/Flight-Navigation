from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for this Flask app

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5500)  # Run this Flask app on port 5500
