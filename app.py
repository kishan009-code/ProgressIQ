from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == "test@gmail.com" and password == "12345":
            return "Login Successful!"

        else:
            return "Invalid email or password"

    return render_template("Login.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )