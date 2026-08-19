from flask import Flask, render_template, request,session
from werkzeug.security import generate_password_hash,check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.secret_key = "progressiq-secret-key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="progressiq"
)
print("MySQL connected:", db.is_connected())
@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor()

        query = "SELECT * FROM users WHERE email = %s"

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        cursor.close()

        if user and check_password_hash(user[3], password):
            print("Login successful!")
            session["user_id"] = user[0]
        else:
            print("Invalid email or password!")

    return render_template("Login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        cursor = db.cursor()

        query = """
            INSERT INTO users (username, email, password, created_at)
            VALUES (%s, %s, %s, CURDATE())
        """

        cursor.execute(query, (username, email, hashed_password))
        db.commit()

        cursor.close()

        print("User registered successfully!")

    return render_template("Register.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return "Please login first."

    return "Welcome to your ProgressIQ Dashboard!"

@app.route("/logout")
def logout():

    session.clear()

    return "You have been logged out."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )