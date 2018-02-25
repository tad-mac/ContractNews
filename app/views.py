from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/articles')
def recent():
    return render_template("articles.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/submit')
def submit():
    return render_template("submit.html")
