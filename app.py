from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash



# Flask App Configuration
app = Flask(__name__)
app.secret_key ="this_is_a_secret_key_and_it_should_be_longer_than_32_characters"
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes


# Database Configuration
mongo_client = "mongodb://localhost:27017/paperless_dcs"
client = MongoClient(mongo_client)
db = client.get_database("paperless_dcs")
users_collection = db["users"]






@app.route("/")
def welcome():
    return render_template('/welcome.html')


@app.route("/login")
def login():
    return render_template('/login.html')


@app.route('/submit_login', methods=['POST'])
def submit_login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one({"email": email})

    if user and check_password_hash(user["password"], password):
        session["user"] = user["email"]
        session["role"] = user["role"]
        session["username"] = user["username"]
        session["username"] = user.get("username", "")
        session["office"] = user.get("office", "")
        session["unit"] = user.get("unit", "")
    

        return jsonify({
            "success": True,
            "role": user["role"]
        })

    return jsonify({"success": False, "error": "Invalid email or password."}), 401



@app.route("/director")
def director_dashboard():

    if "user" not in session:
        return redirect(url_for("login"))


    return render_template(
        '/dashboard_director.html',
        username=session.get("username", ""),
        role=session.get("role", ""),
        office=session.get("office", ""),
        unit=session.get("unit", "")
    )

@app.route("/registry")
def registry_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        '/dashboard_registry.html',
        username=session.get("username", ""),
        role=session.get("role", ""),
        office=session.get("office", ""),
        unit=session.get("unit", ""), content= "dashboard_registry.html"
    )


@app.route("/documents_content")
def documents_content():
    return render_template("documents_content.html")


@app.route("/add_document")
def add_document():
    return render_template("add_document.html")


@app.route("/all_document")
def all_document():
    return render_template("all_document.html")

@app.route("/open_document")
def open_document():
    return render_template("open_document.html")

@app.route("/assigned_documents")
def assigned_documents():
    return render_template("assigned_documents.html")



@app.route("/officer")
def officer_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard_officer.html",
        username=session.get("username", ""),
        role=session.get("role", ""),
        office=session.get("office", ""),
        unit=session.get("unit", "")
    )

@app.route("/logout")
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for("login"))










if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5505, debug=True)
