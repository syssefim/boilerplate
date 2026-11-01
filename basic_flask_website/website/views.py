from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# home
@views.route('/')
def home():
    return render_template('index.html')

@views.route('/<name>')
def user(name):
    return f"Hello {name}!"
