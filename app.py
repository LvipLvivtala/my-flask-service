from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Cloud Technologies</h1>
    <p>My first Docker application</p>
    <hr>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
    """

@app.route("/about")
def about():
    return """
    <h1>About Page</h1>
    <p>This is a lab work on containerization using Docker and Flask.</p>
    <p><a href="/">Back to Home</a></p>
    """

@app.route("/contact")
def contact():
    return """
    <h1>Contact Page</h1>
    <p>Author: Yeralkhan</p>
    <p>Environment: Oracle Cloud Ubuntu Server</p>
    <p><a href="/">Back to Home</a></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
