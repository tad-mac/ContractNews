from flask import render_template, flash, redirect, render_template, request, session, abort
from app import app
from app.forms import LoginForm


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
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/submit')
def submit():
    return render_template("submit.html")
