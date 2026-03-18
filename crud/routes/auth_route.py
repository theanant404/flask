from flask import Blueprint, request, render_template, flash, session
from connect_db import db
from models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        username = data.get("username")
        if not name or not email or not password or not username:
            flash("All fields are required!", "danger")
            return render_template("auth/register.html")
        # name, email,password,username
        already_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()
        if already_user:
            flash("User with this email or username already exists!", "danger")
            return render_template("auth/register.html")
        # user not found
        new_user = User(
            name=name,
            email=email,
            password=password,
            username=username,
            is_verified=False,
        )
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully!", "success")
        return render_template("auth/login.html")
    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            flash("Email and password are required!", "danger")
            return render_template("auth/login.html")
        user = User.query.filter_by(email=email).first()
        if not user or user.password != password:
            flash("Invalid email or password!", "danger")
            return render_template("auth/login.html")
        flash("Logged in successfully!", "success")
        session["user_id"] = user.id
        session["username"] = user.username
        session["is_verified"] = user.is_verified
        session["name"] = user.name
        return render_template("home.html", user=user)
    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out!", "success")
    return render_template("auth/login.html")
