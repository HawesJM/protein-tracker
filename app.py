import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_days")
def get_days():
    days = mongo.db.days.find().sort("day_date", -1).limit(7)
    return render_template("days.html", days=days)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("create-username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("create-username").lower(),
            "password": generate_password_hash(
                request.form.get("create-password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("create-username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/record_day", methods=["GET", "POST"])
def record_day():
    if request.method == "POST":
        day = {
            "day_date": request.form.get("entry_date"),
            "category_name": request.form.get("category_one"),
            "food_item": request.form.get("food_item_one"),
            "protein_amount": request.form.get("protein_one"),
            "category_name_two": request.form.get("category_two"),
            "food_item_two": request.form.get("food_item_two"),
            "protein_amount_two": request.form.get("protein_two"),
            "category_name_three": request.form.get("category_three"),
            "food_item_three": request.form.get("food_item_three"),
            "protein_amount_three": request.form.get("protein_three"),
            "category_name_four": request.form.get("category_four"),
            "food_item_four": request.form.get("food_item_four"),
            "protein_amount_four": request.form.get("protein_four"),
            "category_name_five": request.form.get("category_five"),
            "food_item_five": request.form.get("food_item_five"),
            "protein_amount_five": request.form.get("protein_five"),
            "category_name_six": request.form.get("category_six"),
            "food_item_six": request.form.get("food_item_six"),
            "protein_amount_six": request.form.get("protein_six"),
            "category_name_seven": request.form.get("category_seven"),
            "food_item_seven": request.form.get("food_item_seven"),
            "protein_amount_seven": request.form.get("protein_seven"),
            "category_name_eight": request.form.get("category_eight"),
            "food_item_eight": request.form.get("food_item_eight"),
            "protein_amount_eight": request.form.get("protein_eight"),
            "category_name_nine": request.form.get("category_nine"),
            "food_item_nine": request.form.get("food_item_nine"),
            "protein_amount_nine": request.form.get("protein_nine"),
            "category_name_ten": request.form.get("category_ten"),
            "food_item_ten": request.form.get("food_item_ten"),
            "protein_amount_ten": request.form.get("protein_ten"),
            "created_by": session["user"],
            "description": request.form.get("log_description"),
            "friendly_description": (
                request.form.get("log_description").replace(" ", "")
            )
        }
        mongo.db.days.insert_one(day)
        flash("Day Successfully Recorded!")
        return redirect(url_for("get_days"))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("record_day.html", categories=categories)


@app.route("/edit_day/<day_id>", methods=["GET", "POST"])
def edit_day(day_id):
    day = mongo.db.days.find_one({"_id": ObjectId(day_id)})
    days = list(mongo.db.days.find())
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    if request.method == "POST":
        edit_day = {
            "day_date": request.form.get("entry_date"),
            "category_name": request.form.get("category_one"),
            "food_item": request.form.get("food_item_one"),
            "protein_amount": request.form.get("protein_one"),
            "category_name_two": request.form.get("category_two"),
            "food_item_two": request.form.get("food_item_two"),
            "protein_amount_two": request.form.get("protein_two"),
            "category_name_three": request.form.get("category_three"),
            "food_item_three": request.form.get("food_item_three"),
            "protein_amount_three": request.form.get("protein_three"),
            "category_name_four": request.form.get("category_four"),
            "food_item_four": request.form.get("food_item_four"),
            "protein_amount_four": request.form.get("protein_four"),
            "category_name_five": request.form.get("category_five"),
            "food_item_five": request.form.get("food_item_five"),
            "protein_amount_five": request.form.get("protein_five"),
            "category_name_six": request.form.get("category_six"),
            "food_item_six": request.form.get("food_item_six"),
            "protein_amount_six": request.form.get("protein_six"),
            "category_name_seven": request.form.get("category_seven"),
            "food_item_seven": request.form.get("food_item_seven"),
            "protein_amount_seven": request.form.get("protein_seven"),
            "category_name_eight": request.form.get("category_eight"),
            "food_item_eight": request.form.get("food_item_eight"),
            "protein_amount_eight": request.form.get("protein_eight"),
            "category_name_nine": request.form.get("category_nine"),
            "food_item_nine": request.form.get("food_item_nine"),
            "protein_amount_nine": request.form.get("protein_nine"),
            "category_name_ten": request.form.get("category_ten"),
            "food_item_ten": request.form.get("food_item_ten"),
            "protein_amount_ten": request.form.get("protein_ten"),
            "created_by": session["user"],
            "description": request.form.get("log_description"),
            "friendly_description": (
                request.form.get("log_description").replace(" ", "")
            )
        }

        mongo.db.days.update_one(
            {"_id": ObjectId(day_id)}, {"$set": edit_day})
        flash("Day Successfully Updated!")
    
    return render_template(
        "edit_day.html",
        day=day,
        categories=categories,
        days=days
    )


@app.route("/delete_day/<day_id>")
def delete_day(day_id):
    mongo.db.days.delete_one({"_id": ObjectId(day_id)})
    flash("Record Successfully Deleted")
    return redirect(url_for("get_day"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))


 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)