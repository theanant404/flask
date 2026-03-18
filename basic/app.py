from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# routes
@app.route("/", methods=["GET"])  # uri http://localhost:9000/
def root():
    data = {
        "name": "Flask App",
        "version": "1.0.0",
        "description": "A simple Flask application",
    }
    return jsonify({"status": "success", "data": data}, 200)


@app.route("/about/anant")  # uri http://localhost:9000/about/anant
def about_anant():
    return """
<h1>About Flask App</h1>
<p>This is a simple Flask application that demonstrates how to create a basic web server using Flask. It includes a root endpoint that returns some information about the app in JSON format, and an about endpoint
"""


@app.route(
    "/auth/register", methods=["GET", "POST"]
)  # uri http://localhost:9000/auth/register
def register_user_account():
    if request.method == "POST":
        # Here you would handle the registration logic, such as validating input and saving user data
        return jsonify(
            {"status": "success", "message": "User registered successfully"}, 201
        )
    return "<h1>Register</h1><p>Please submit your registration details using a POST request.</p>"


@app.route("/<name>")
def anant(name):
    return f"Hello {name}! Welcome to Flask App"


## Get data from users
@app.route("/auth/register", methods=["POST"])
def register_user():
    form_data = request.form  # Access form data
    body_data = request.get_json(
        silent=True
    )  # Access JSON data from request body [silent=True to avoid error if no JSON is sent]
    if body_data:
        data = body_data
    else:
        data = form_data
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")

    print(
        f"Received user data: Name={name}, Email={email}, Username={username}, Password={password}"
    )
    return jsonify(
        {"status": "success", "message": "User data received", "data": data}, 201
    )


# Dynamic route to get user information
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    # Here you would typically fetch user data from a database
    return (
        jsonify(
            {
                "status": "success",
                "data": {
                    "username": username,
                    "name": "John Doe",
                    "email": "john@example.com",
                },
            }
        ),
        200,
    )


# get data form users using query parameters
@app.route("/search")
def search():
    query = request.args.get("q")
    query2 = request.args.get("q1")
    print(f"Received search query: {query}")
    print(f"Received search query 2: {query2}")
    return (
        jsonify({"status": "success", "message": f"Search query received: {query}"}),
        200,
    )


# jinja template
@app.route("/home")
def home():
    user_data = [
        {
            "name": "Anant",
            "email": "anant@gm.com",
            "age": 30,
            "marks": {"Math": 90, "Science": 85},
        },
        {
            "name": "John",
            "email": "john@example.com",
            "age": 25,
            "marks": {"Math": 80, "Science": 90},
        },
        {
            "name": "Alice",
            "email": "alice@example.com",
            "age": 28,
            "marks": {"Math": 85, "Science": 88},
        },
    ]
    return render_template("home.html", users=user_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        print(data)
        return render_template("auth/register.html")
    return render_template("auth/register.html")


## Http Methods
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
