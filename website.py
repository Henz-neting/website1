from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Dummy user data
USER = {"username": "admin", "password": "secret"}

HTML_PAGE = open("login.html").read()

@app.route("/")
def home():
    return HTML_PAGE

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == USER["username"] and password == USER["password"]:
        return "<h2>Login successful!</h2>"
    else:
        return "<h2>Invalid credentials.</h2><a href='/'>Try again</a>"

if __name__ == "__main__":
    app.run(debug=True)
