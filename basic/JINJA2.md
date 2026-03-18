# Jinja2 Template Engine - Complete Guide

Jinja2 is a modern and designer-friendly templating language for Python. It's commonly used with Flask to generate dynamic HTML pages. This guide covers the most important concepts with practical examples.

---

## Table of Contents
1. [Basic Syntax](#basic-syntax)
2. [Variables](#variables)
3. [Filters](#filters)
4. [Control Flow](#control-flow)
5. [Template Inheritance](#template-inheritance)
6. [Macros](#macros)
7. [Loops](#loops)
8. [Comments](#comments)
9. [Built-in Tests](#built-in-tests)
10. [Best Practices](#best-practices)

---

## Basic Syntax

Jinja2 uses three main delimiters:

### 1. **{{ ... }}** - Print/Output Variables
```html
<!-- Renders the value of a variable -->
<p>Hello, {{ username }}!</p>

<!-- Output: Hello, John! -->
```

### 2. **{% ... %}** - Execute Statements
```html
<!-- Used for loops, conditionals, assignments -->
{% if user %}
    <p>User is logged in</p>
{% endif %}
```

### 3. **{# ... #}** - Comments
```html
<!-- Comments that won't appear in output -->
{# This is a comment #}
<p>This will be rendered</p>
```

---

## Variables

### Accessing Variables
```html
<!-- Simple variable -->
{{ message }}

<!-- Dictionary access -->
{{ user['name'] }}
{{ user.name }}

<!-- List access -->
{{ items[0] }}

<!-- Nested access -->
{{ user.profile.email }}
```

### Example with Flask:
```python
from flask import Flask, render_template

@app.route('/user/<name>')
def show_user(name):
    user_data = {
        'name': name,
        'email': 'user@example.com',
        'is_active': True
    }
    return render_template('user.html', user=user_data)
```

```html
<!-- user.html -->
<h1>{{ user.name }}</h1>
<p>Email: {{ user.email }}</p>
<p>Active: {{ user.is_active }}</p>
```

---

## Filters

Filters modify variables. Use the `|` (pipe) operator to apply filters. Filters can be chained together for complex transformations.

### Common Filters:

**1. Uppercase & Lowercase**
```html
<!-- Convert to uppercase -->
{{ message|upper }}  
<!-- OUTPUT: HELLO WORLD -->

<!-- Real-world example: Display user header in caps -->
<h1>{{ title|upper }}</h1>  <!-- OUTPUT: <h1>WELCOME USER</h1> -->

<!-- Convert to lowercase -->
{{ email|lower }}  
<!-- OUTPUT: john@example.com (even if input was JOHN@EXAMPLE.COM) -->

<!-- Use case: Normalizing user input for consistency -->
<p>Username: {{ username|lower }}</p>
```

**2. Title Case**
```html
<!-- Each word starts with capital -->
{{ message|title }}  
<!-- OUTPUT: Hello World -->

<!-- Real-world example: Display product names -->
<h2>{{ product_name|title }}</h2>  <!-- INPUT: "laptop computer" OUTPUT: "Laptop Computer" -->

<!-- Display user full name -->
<p>Welcome, {{ user.full_name|title }}</p>
```

**3. Capitalize**
```html
<!-- Only first character capitalized, rest lowercase -->
{{ message|capitalize }}  
<!-- OUTPUT: Hello world -->

<!-- Real-world example: Display status -->
<span class="status">{{ status|capitalize }}</span>  <!-- INPUT: "active" OUTPUT: "Active" -->

<!-- Display role -->
<p>Role: {{ user.role|capitalize }}</p>  <!-- INPUT: "admin" OUTPUT: "Admin" -->
```

**4. Length**
```html
<!-- Get number of items in list or string length -->
{{ items|length }}  

<!-- Real-world example: Count items in cart -->
<span class="badge">{{ cart_items|length }}</span>  <!-- Shows "5" if 5 items in cart -->

<!-- Display comment count -->
<p>Comments: {{ comments|length }}</p>

<!-- Check if empty -->
{% if items|length > 0 %}
    <p>You have {{ items|length }} items</p>
{% else %}
    <p>Your cart is empty</p>
{% endif %}
```

**5. Default Value (Fallback)**
```html
<!-- Shows default if variable is undefined or empty -->
{{ username|default('Guest') }}

<!-- Real-world examples: -->
<p>Welcome, {{ user.name|default('User') }}</p>

<p>Email: {{ user.email|default('Not provided') }}</p>

<p>Phone: {{ user.phone|default('Contact not available') }}</p>

<!-- Use with complex conditions -->
<span class="badge">{{ user.role|default('Member') }}</span>

<!-- Chaining defaults for multiple fallbacks -->
{{ data.primary|default(data.secondary)|default('No data available') }}
```

**6. Replace**
```html
<!-- Replace text within string -->
{{ text|replace('old', 'new') }}

<!-- Simple replacement -->
{{ "Hello World"|replace('World', 'Jinja') }}
<!-- OUTPUT: Hello Jinja -->

<!-- Real-world example: Display formatted text -->
<p>{{ bio|replace('\n', '<br/>') }}</p>

<!-- Replace special characters -->
{{ phone|replace('-', '') }}  <!-- INPUT: "123-456-7890" OUTPUT: "1234567890" -->

<!-- Replace URLs or links -->
{{ content|replace('http://', 'https://') }}

<!-- Multiple replacements -->
{{ title|replace('Mr.', 'Mr')|replace('Mrs.', 'Mrs') }}
```

**7. String Join**
```html
<!-- Join list items with separator -->
{{ items|join(', ') }}

<!-- If items = ['Apple', 'Banana', 'Cherry'] -->
<!-- OUTPUT: Apple, Banana, Cherry -->

<!-- Real-world examples: -->
<!-- Display tags -->
<p>Tags: {{ post.tags|join(', ') }}</p>  <!-- OUTPUT: python, django, web -->

<!-- Display user skills -->
<p>Skills: {{ user.skills|join(' • ') }}</p>  <!-- OUTPUT: Python • Django • JavaScript -->

<!-- Display breadcrumb navigation -->
<p>{{ breadcrumbs|join(' / ') }}</p>  <!-- OUTPUT: Home / Products / Electronics -->

<!-- Create CSV-like output -->
<p>{{ data|join(';') }}</p>  <!-- OUTPUT: value1;value2;value3 -->

<!-- Join without separator -->
{{ codes|join('') }}  <!-- Concatenate without spaces -->
```

**8. Abs (Absolute Value)**
```html
<!-- Remove negative sign -->
{{ -5|abs }}  
<!-- OUTPUT: 5 -->

{{ -3.14|abs }}  
<!-- OUTPUT: 3.14 -->

<!-- Real-world example: Display distance/difference -->
<p>Temperature difference: {{ current_temp - target_temp|abs }}°C</p>

<!-- Display balance (absolute value) -->
<p>Balance: ${{ account_balance|abs }}</p>

<!-- Calculate absolute difference between two values -->
<p>Difference: {{ value1 - value2|abs }} units</p>
```

**9. Round**
```html
<!-- Round decimal numbers -->
{{ 3.14159|round(2) }}  
<!-- OUTPUT: 3.14 -->

{{ 3.5 }}  
<!-- OUTPUT: 4 (default round function) -->

<!-- Real-world examples: -->
<!-- Display price with 2 decimals -->
<p>Price: ${{ product.price|round(2) }}</p>

<!-- Display percentage -->
<p>Progress: {{ (completion / total) * 100|round(1) }}%</p>

<!-- Display average rating -->
<p>Rating: {{ average_rating|round(1) }} stars</p>

<!-- Round to nearest integer -->
<p>Quantity: {{ item_count|round }} units</p>

<!-- Round to specific decimal places -->
<p>Accuracy: {{ measurement|round(3) }}</p>
```

**10. Format (String Formatting)**
```html
<!-- Format strings with placeholders -->
{{ "%s is %d" | format("John", 25) }}
<!-- OUTPUT: John is 25 -->

<!-- Real-world examples: -->
<!-- Display formatted message -->
<p>{{ "User %s registered on %s" | format(user.name, user.date) }}</p>

<!-- Display address -->
<p>{{ "%s, %s, %s" | format(street, city, country) }}</p>

<!-- Display achievement -->
<p>{{ "%s earned %d points" | format(user.name, points) }}</p>

<!-- Format with multiple data types -->
{{ "Product: %s, Price: $%.2f, Quantity: %d" | format(product, price, qty) }}
```

**11. Reverse**
```html
<!-- Reverse a sequence -->
{{ [1, 2, 3]|reverse|list }}  
<!-- OUTPUT: [3, 2, 1] -->

<!-- Real-world examples: -->
<!-- Display comments in reverse order (newest first) -->
{% for comment in comments|reverse %}
    <div class="comment">{{ comment.text }}</div>
{% endfor %}

<!-- Reverse string -->
{{ "Hello"|reverse }}  
<!-- OUTPUT: olleH -->

<!-- Display items in reverse order -->
<div>{{ items|reverse|join(', ') }}</div>

<!-- Reverse alphabet or sorted list -->
{{ names|sort|reverse|list }}
```

**12. Sort**
```html
<!-- Sort a list in ascending order -->
{{ [3, 1, 2]|sort }}  
<!-- OUTPUT: [1, 2, 3] -->

<!-- Real-world examples: -->
<!-- Sort names alphabetically -->
{% for name in names|sort %}
    <li>{{ name }}</li>
{% endfor %}

<!-- Sort by attribute on dictionaries -->
{{ products|sort(attribute='price')|list }}

<!-- Sort numbers -->
<p>{{ scores|sort|join(', ') }}</p>

<!-- Sort in descending order (sort + reverse) -->
{{ numbers|sort|reverse|list }}
```

**13. Reverse + Sort (Descending Sort)**
```html
<!-- Sort descending -->
{{ [3, 1, 2]|sort|reverse|list }}  
<!-- OUTPUT: [3, 2, 1] -->

<!-- Real-world examples: -->
<!-- Display top scores (highest first) -->
{% for score in scores|sort|reverse %}
    <li>{{ score }}</li>
{% endfor %}

<!-- Display most recent items first -->
{% for post in posts|sort(attribute='date')|reverse %}
    <h3>{{ post.title }}</h3>
    <p>{{ post.date }}</p>
{% endfor %}

<!-- Display prices from high to low -->
<div>{{ product_prices|sort|reverse|join(', ') }}</div>
```

**14. Unique (Remove Duplicates)**
```html
<!-- Remove duplicate items -->
{{ [1, 2, 2, 3]|unique|list }}  
<!-- OUTPUT: [1, 2, 3] -->

<!-- Real-world examples: -->
<!-- Display unique tags -->
<p>{{ post.tags|unique|join(', ') }}</p>

<!-- Display unique authors in list -->
{% for author in articles|map(attribute='author')|unique %}
    <p>{{ author }}</p>
{% endfor %}

<!-- Unique sorted values -->
{{ values|unique|sort|join(', ') }}

<!-- Count unique items -->
<p>Unique items: {{ items|unique|list|length }}</p>
```

**15. First & Last**
```html
<!-- Get first item from list -->
{{ items|first }}  
<!-- OUTPUT: First item in list -->

<!-- Get last item from list -->
{{ items|last }}  
<!-- OUTPUT: Last item in list -->

<!-- Real-world examples: -->
<p>First user: {{ users|first }}</p>

<p>Latest comment: {{ comments|last }}</p>

<!-- Display first item differently -->
{% set featured = products|first %}
<h2>Featured: {{ featured }}</h2>
```

**16. Min & Max**
```html
<!-- Get minimum value -->
{{ numbers|min }}  
<!-- OUTPUT: Smallest number -->

<!-- Get maximum value -->
{{ numbers|max }}  
<!-- OUTPUT: Largest number -->

<!-- Real-world examples: -->
<p>Lowest price: ${{ prices|min }}</p>

<p>Highest score: {{ scores|max }}</p>

<!-- Display price range -->
<p>Price range: ${{ prices|min }} - ${{ prices|max }}</p>
```

**17. Sum (Calculate Total)**
```html
<!-- Add all numbers in list -->
{{ [1, 2, 3, 4]|sum }}  
<!-- OUTPUT: 10 -->

<!-- Real-world examples: -->
<p>Total sales: ${{ sales|sum }}</p>

<p>Cart total: ${{ cart_prices|sum }}</p>

<!-- Sum with attribute (for list of objects) -->
<p>Total quantity: {{ items|sum(attribute='quantity') }}</p>
```

**18. Attribute (Extract Property)**
```html
<!-- Extract specific attribute from list of objects -->
{{ users|map(attribute='name')|list }}

<!-- Real-world examples: -->
<!-- Get all user names -->
<p>Users: {{ users|map(attribute='name')|join(', ') }}</p>

<!-- Get all product prices -->
<p>Prices: {{ products|map(attribute='price')|list }}</p>
```

**19. Select (Filter by Condition)**
```html
<!-- Filter list based on condition -->
{% set active_users = users|selectattr('is_active') %}

<!-- Real-world examples: -->
<p>Active users: {{ users|selectattr('is_active')|map(attribute='name')|join(', ') }}</p>

<!-- Filter products under price -->
<div>
{% for product in products|selectattr('price', '<', 100) %}
    <p>{{ product.name }}: ${{ product.price }}</p>
{% endfor %}
</div>
```

**20. Reject (Opposite of Select)**
```html
<!-- Filter out items that match condition -->
{% for product in products|rejectattr('is_discontinued') %}
    <div>{{ product.name }}</div>
{% endfor %}

<!-- Real-world example: Hide inactive items -->
<p>Active items: {{ items|rejectattr('is_inactive')|length }}</p>
```

### Chaining Multiple Filters

```html
<!-- Combine filters for complex transformations -->

<!-- Example 1: Format text for display -->
{{ user_input|lower|title|capitalize }}

<!-- Example 2: Display sorted unique tags -->
<p>Tags: {{ tags|unique|sort|join(', ')|title }}</p>

<!-- Example 3: Display price range -->
<p>Price: ${{ prices|min|round(2) }} - ${{ prices|max|round(2) }}</p>

<!-- Example 4: Display formatted list -->
{{ names|sort|reverse|join(' and ')|capitalize }}

<!-- Example 5: Extract and format data -->
<p>{{ users|map(attribute='name')|sort|join(', ') }}</p>

<!-- Example 6: Complex data processing -->
{{ 
    (cart_items|sum(attribute='price'))|round(2)
}}

<!-- Example 7: Fallback with formatting -->
{{ user.nickname|default(user.name)|capitalize }}

<!-- Example 8: Join with replacement -->
{{ categories|replace('tech', 'technology')|join(' | ') }}
```

### Real-World Filter Examples

**Display User Profile Card**
```html
<div class="profile">
    <h2>{{ user.name|title }}</h2>
    <p>Username: {{ user.username|lower }}</p>
    <p>Email: {{ user.email|lower }}</p>
    <p>Role: {{ user.role|default('Member')|capitalize }}</p>
    <p>Bio: {{ user.bio|replace('\n', '<br/>')|default('No bio provided') }}</p>
</div>
```

**Display Product List**
```html
<div class="products">
    {% for product in products|sort(attribute='price') %}
    <div class="product">
        <h3>{{ product.name|title }}</h3>
        <p>Price: ${{ product.price|round(2) }}</p>
        <p>Tags: {{ product.tags|unique|join(', ') }}</p>
    </div>
    {% endfor %}
</div>
```

**Display User Statistics**
```html
<div class="stats">
    <p>Total users: {{ users|length }}</p>
    <p>Active users: {{ users|selectattr('is_active')|list|length }}</p>
    <p>Highest score: {{ scores|max|default(0) }}</p>
    <p>Lowest score: {{ scores|min|default(0) }}</p>
    <p>Average: {{ (scores|sum / scores|length)|round(2)|default('N/A') }}</p>
</div>
```

---

## Control Flow

### 1. If / Elif / Else

```html
{% if score >= 90 %}
    <p>Grade: A</p>
{% elif score >= 80 %}
    <p>Grade: B</p>
{% elif score >= 70 %}
    <p>Grade: C</p>
{% else %}
    <p>Grade: F</p>
{% endif %}
```

**With Multiple Conditions:**
```html
{% if user.is_admin and user.is_active %}
    <p>Admin access granted</p>
{% endif %}

{% if user.role == 'editor' or user.role == 'admin' %}
    <p>Can edit content</p>
{% endif %}

{% if not user.is_verified %}
    <p>Please verify your email</p>
{% endif %}
```

### 2. Inline If (Ternary Operator)

```html
<!-- Syntax: value_if_true if condition else value_if_false -->
{{ 'Adult' if age >= 18 else 'Minor' }}

<!-- In variable: -->
{% set status = 'Active' if user.is_active else 'Inactive' %}
```

---

## Template Inheritance

Template inheritance allows you to create a base template and extend it in child templates.

### Base Template (base.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <nav class="navbar">
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>

    <main class="container">
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 My Website</p>
    </footer>
</body>
</html>
```

### Child Template (home.html):
```html
{% extends "base.html" %}

{% block title %}Home - My Website{% endblock %}

{% block content %}
<h1>Welcome to Home</h1>
<p>This is the home page content.</p>
{% endblock %}
```

### Child Template (about.html):
```html
{% extends "base.html" %}

{% block title %}About - My Website{% endblock %}

{% block content %}
<h1>About Us</h1>
<p>This is the about page content.</p>
{% endblock %}
```

### Using super() to Include Parent Content:
```html
{% extends "base.html" %}

{% block content %}
<div class="alert">
    <!-- Include parent block content -->
    {{ super() }}
</div>
{% endblock %}
```

---

## Macros

Macros are reusable template functions. They help reduce code repetition.

### Simple Macro:
```html
<!-- Define a macro -->
{% macro greet(name) %}
    <p>Hello, {{ name }}!</p>
{% endmacro %}

<!-- Use the macro -->
{{ greet('John') }}
{{ greet('Sarah') }}
```

### Macro with Multiple Parameters:
```html
{% macro button(text, link, class='btn-primary') %}
    <a href="{{ link }}" class="btn {{ class }}">{{ text }}</a>
{% endmacro %}

<!-- Usage -->
{{ button('Click Here', '/page1') }}
{{ button('Edit', '/edit', 'btn-warning') }}
```

### Macro with Default Values:
```html
{% macro product_card(name, price, discount=0) %}
    <div class="card">
        <h3>{{ name }}</h3>
        <p class="price">${{ price - discount }}</p>
    </div>
{% endmacro %}

{{ product_card('Laptop', 999, 50) }}
{{ product_card('Mouse', 25) }}
```

### Storing Macros in Separate File:

**macros.html:**
```html
{% macro form_field(name, type='text', required=False) %}
    <div class="form-group">
        <label for="{{ name }}">{{ name|capitalize }}</label>
        <input type="{{ type }}" name="{{ name }}" id="{{ name }}" 
               {% if required %}required{% endif %}>
    </div>
{% endmacro %}
```

**main.html:**
```html
{% from 'macros.html' import form_field %}

<form>
    {{ form_field('username', required=True) }}
    {{ form_field('password', type='password', required=True) }}
    {{ form_field('email', type='email') }}
</form>
```

---

## Loops

### Basic For Loop:
```html
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}

<!-- Output if items = ['Apple', 'Banana', 'Cherry']:
<li>Apple</li>
<li>Banana</li>
<li>Cherry</li>
-->
```

### Loop with Index:
```html
{% for item in items %}
    <p>{{ loop.index }}: {{ item }}</p>
{% endfor %}

<!-- Output:
1: Apple
2: Banana
3: Cherry
-->
```

### Loop Special Variables:
```html
{% for item in items %}
    <p>
        Index (0-based): {{ loop.index0 }}<br>
        Index (1-based): {{ loop.index }}<br>
        Revision Index: {{ loop.revindex }}<br>
        Is First: {{ loop.first }}<br>
        Is Last: {{ loop.last }}<br>
        Length: {{ loop.length }}<br>
    </p>
{% endfor %}
```

### Loop with Condition (If):
```html
{% for item in items %}
    {% if item.is_active %}
        <li class="active">{{ item.name }}</li>
    {% else %}
        <li class="inactive">{{ item.name }}</li>
    {% endif %}
{% endfor %}
```

### Else in Loop (Empty List):
```html
{% for item in items %}
    <li>{{ item }}</li>
{% else %}
    <p>No items found</p>
{% endfor %}
```

### Nested Loops:
```html
{% for user in users %}
    <h3>{{ user.name }}</h3>
    <ul>
        {% for post in user.posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
{% endfor %}
```

### Loop with Dictionary:
```html
{% for key, value in user.items() %}
    <p>{{ key }}: {{ value }}</p>
{% endfor %}

<!-- If user = {'name': 'John', 'age': 30}
Output:
name: John
age: 30
-->
```

---

## Comments

### Single Line Comment:
```html
{# This is a comment and won't be rendered #}
<p>This will be visible</p>
```

### Multi-Line Comment:
```html
{#
    This is a multi-line comment
    It can span multiple lines
    and won't appear in the output
#}
<p>Content here</p>
```

---

## Built-in Tests

Tests check conditions and return True/False.

### Syntax:
```html
{% if variable is test_name %}
    <!-- condition is true -->
{% endif %}
```

### Common Tests:

**1. Defined/Undefined**
```html
{% if username is defined %}
    <p>Username: {{ username }}</p>
{% endif %}

{% if email is undefined %}
    <p>Email not provided</p>
{% endif %}
```

**2. None**
```html
{% if value is none %}
    <p>Value is None</p>
{% endif %}
```

**3. Number**
```html
{% if value is number %}
    <p>Value is a number</p>
{% endif %}
```

**4. String**
```html
{% if value is string %}
    <p>Value is a string</p>
{% endif %}
```

**5. Odd/Even**
```html
{% for num in numbers %}
    {% if num is odd %}
        <p>{{ num }} is odd</p>
    {% elif num is even %}
        <p>{{ num }} is even</p>
    {% endif %}
{% endfor %}
```

**6. Divisible by**
```html
{% if num is divisibleby(3) %}
    <p>{{ num }} is divisible by 3</p>
{% endif %}
```

**7. Iterable**
```html
{% if items is iterable %}
    <p>Items is a list, tuple, or other iterable</p>
{% endif %}
```

**8. Mapping (Dictionary)**
```html
{% if data is mapping %}
    <p>Data is a dictionary</p>
{% endif %}
```

---

## Best Practices

### 1. Use Meaningful Variable Names
```html
<!-- Good -->
{% for user in active_users %}
    <p>{{ user.full_name }}</p>
{% endfor %}

<!-- Avoid -->
{% for u in au %}
    <p>{{ u.fn }}</p>
{% endfor %}
```

### 2. Use Filters for Data Formatting
```html
<!-- Good - Use filters in template -->
<p>{{ price|round(2) }}</p>
<p>{{ name|capitalize }}</p>

<!-- Less ideal - Heavy logic in template -->
```

### 3. Avoid Complex Logic in Templates
```html
<!-- Good - Simple expressions -->
{% if user.is_admin %}
    Show admin panel
{% endif %}

<!-- Avoid - Complex logic -->
{% if (user.role == 'admin' and user.verified) or user.created_at < now - timedelta %}
    <!-- This is too complex for a template -->
{% endif %}
```

**Better approach:** Handle complex logic in Python:
```python
# app.py
@app.route('/dashboard')
def dashboard():
    user = get_user()
    can_access_admin = check_admin_access(user)  # Complex logic here
    return render_template('dashboard.html', can_access=can_access_admin)
```

### 4. Use Template Inheritance for Consistency
```html
<!-- Always extend base.html for consistent layout -->
{% extends "base.html" %}
```

### 5. Use Macros for Reusable Components
```html
<!-- Instead of repeating HTML, use macros -->
{% set button_html %}
    <a href="{{ link }}" class="btn">{{ label }}</a>
{% endset %}
```

### 6. Keep Templates Organized
```
templates/
├── base.html                 # Base layout
├── macros.html              # Reusable macros
├── auth/
│   ├── login.html
│   └── register.html
├── events/
│   ├── list.html
│   └── detail.html
└── admin/
    └── dashboard.html
```

### 7. Use Named Blocks for Clarity
```html
<!-- Good - Clear block names -->
{% block page_title %}{% endblock %}
{% block navigation %}{% endblock %}
{% block main_content %}{% endblock %}
{% block footer %}{% endblock %}

<!-- Avoid - Ambiguous names -->
{% block content1 %}{% endblock %}
{% block section %}{% endblock %}
```

### 8. Always Escape User Input (Security)
```html
<!-- Good - Auto-escaped by default in Flask -->
{{ user_input }}

<!-- Manual escaping if needed -->
{{ user_input|escape }}
{{ user_input|safe }}  <!-- Only if you trust the content -->
```

### 9. Use Default Filters for Missing Variables
```html
<!-- Good - Shows default if not provided -->
<p>Hello, {{ username|default('Guest') }}</p>

<!-- Provides fallback for optional data -->
<p>Email: {{ user.email|default('Not provided') }}</p>
```

### 10. Comment Your Templates
```html
<!-- Section header -->
<!-- Users table with pagination -->
{% for user in users %}
    <!-- Display user row -->
    <tr>
        <td>{{ user.name }}</td>
        <td>{{ user.email }}</td>
    </tr>
{% endfor %}
```

---

## Real-World Example

### Flask App:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    users_data = [
        {'id': 1, 'name': 'John', 'email': 'john@example.com', 'is_admin': True},
        {'id': 2, 'name': 'Sarah', 'email': 'sarah@example.com', 'is_admin': False},
        {'id': 3, 'name': 'Mike', 'email': 'mike@example.com', 'is_admin': False},
    ]
    return render_template('users.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)
```

### users.html:
```html
{% extends "base.html" %}

{% block title %}Users - My App{% endblock %}

{% block content %}
<div class="users-section">
    <h1>Users List</h1>
    
    {% if users %}
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>
            </thead>
            <tbody>
                {% for user in users %}
                <tr class="{% if user.is_admin %}admin-row{% endif %}">
                    <td>{{ loop.index }}</td>
                    <td>{{ user.name|capitalize }}</td>
                    <td>{{ user.email }}</td>
                    <td>
                        {% if user.is_admin %}
                            <span class="badge badge-admin">Admin</span>
                        {% else %}
                            <span class="badge badge-user">User</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p class="empty-message">No users found.</p>
    {% endif %}
</div>
{% endblock %}
```

---

## Summary

| Feature | Syntax | Example |
|---------|--------|---------|
| Output | `{{ }}` | `{{ name }}` |
| Statements | `{% %}` | `{% if condition %}` |
| Comments | `{# #}` | `{# comment #}` |
| Filters | `\|` | `{{ text\|upper }}` |
| Loop | `{% for %}` | `{% for item in items %}` |
| Conditions | `{% if %}` | `{% if x > 5 %}` |
| Inheritance | `{% extends %}` | `{% extends "base.html" %}` |
| Macros | `{% macro %}` | `{% macro func() %}` |

---

## Resources
- [Jinja2 Official Documentation](https://jinja.palletsprojects.com/)
- [Flask Template Documentation](https://flask.palletsprojects.com/templates/)

