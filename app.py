from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Details</h1>
    <p>Name: Aryan Bhimani</p>
    <p>AppID: EXPERIMENT-6</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)