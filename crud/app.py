from flask import Flask, request, render_template, flash, session
from models import User
from connect_db import db
from routes.auth_route import auth_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
