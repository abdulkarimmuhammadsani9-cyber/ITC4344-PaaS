# ITC4344 Cloud Computing – PaaS Practical
# File 1: main.py
# Purpose: This Python file defines a simple Flask web application.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>ITC4344 PaaS Practical</title>
    </head>
    <body style="font-family: Arial; text-align: center; padding: 60px;">
        <h1>Hello, Cloud Computing!</h1>
        <h2>Welcome to ITC4344</h2>
        <p>This application is deployed using Render.</p>
        <p>Course: ITC4344 Cloud Computing</p>
        <p>Service Model: Platform as a Service (PaaS)</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
    
