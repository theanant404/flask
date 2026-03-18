## 1. New Flask App Setup

### Step 1: Create project folder

```bash
mkdir basic
cd basic
```

### Step 2: Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
# If python is not recognized:
py -m venv .venv
```

### Step 3: Activate virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows (Command Prompt):

```bash
.venv\Scripts\activate
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

### Step 4: Install Flask

```bash
pip install Flask
```

### Step 5: Create `app.py`

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
```

### Step 6: Run the app

macOS/Linux:

```bash
python3 app.py
```

Windows:

```bash
python app.py
```

Open: `http://127.0.0.1:9000`

### Step 7: Deactivate when done

```bash
deactivate
```

## 2. Route Examples

`@app.route()` maps a URL path to a Python function.

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")  # http://127.0.0.1:9000/
def home():
    return """
    <h1>Welcome to the Home Page!</h1>
    <p>This is a simple Flask application.</p>
    """


@app.route("/about")  # http://127.0.0.1:9000/about
def about():
    return """
    <h1>About Us</h1>
    <p>This is a simple Flask application.</p>
    """


@app.route("/contact")  # http://127.0.0.1:9000/contact
def contact():
    return """
    <h1>Contact Us</h1>
    <ul>
        <li>Email: info@example.com</li>
        <li>Phone: +1 234 567 890</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
```

## 3. HTTP Methods in Flask

By default, routes accept only `GET`. Use `methods=[...]` to allow other methods.

```python
from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "Registration successful!"

    return """
    <h1>Register</h1>
    <form method="post">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="submit" value="Register">
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
```

Common methods:

- `GET`: Read data
- `POST`: Create/submit new data
- `PUT`: Replace existing data
- `PATCH`: Partially update data
- `DELETE`: Remove data
- `OPTIONS`: Check supported methods
- `HEAD`: Get headers only

## 4. Accessing User Data

Use different request objects depending on how data is sent.

- `request.form` for form data
- `request.get_json()` for JSON body
- `request.args` for query params
- URL parameters for path values

```python
from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    form_data = request.form
    json_data = request.get_json(silent=True) or {}

    name = form_data.get("name") or json_data.get("name")
    email = form_data.get("email") or json_data.get("email")
    return f"Registration successful for {name} ({email})"


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    return f"Search results for: {query}"


@app.route("/get-profile/<int:user_id>", methods=["GET"])
def get_profile(user_id):
    return f"Profile information for user ID: {user_id}"


@app.route("/update-profile", methods=["PUT"])
def update_profile():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Unknown")
    email = data.get("email", "Unknown")
    return f"Profile updated for {name} with email {email}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
```

## 5. Quick Test Commands

```bash
curl -X GET http://127.0.0.1:9000/
curl -X GET "http://127.0.0.1:9000/search?q=flask"
curl -X POST http://127.0.0.1:9000/register -d "name=Anant&email=anant@example.com"
curl -X PUT http://127.0.0.1:9000/update-profile -H "Content-Type: application/json" -d '{"name":"Anant","email":"anant@example.com"}'
```
