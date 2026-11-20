# ITC4344 Cloud Computing – PaaS Practical
# File 1: main.py
# Purpose: This Python file defines a simple Flask web application for the Google App Engine practical.
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
        <p>This application is deployed using Google App Engine.</p>
        <p>Course: ITC4344 Cloud Computing</p>
        <p>Service Model: Platform as a Service (PaaS)</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

How to save this as a Python file
1.	Open Notepad on your laptop.
2.	Copy only the Python code above and paste it into Notepad.
3.	Select File > Save As.
4.	Set File name to main.py.
5.	Set Save as type to All files (*.*).
6.	Save it inside your ITC4344-PaaS folder.
7.	Check that the filename is main.py, not main.py.txt.
