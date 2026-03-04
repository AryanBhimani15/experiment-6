from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Information</h1>
    <p><b>Name:</b> Aryan Bhimani</p>
    <p><b>App ID:</b> APP12345</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)