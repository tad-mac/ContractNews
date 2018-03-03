from flask import render_template, flash, redirect, render_template, request, session, abort

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


@app.route('/loginform')
def loginform():
    return render_template("login.html")


@app.route('/loggin')
def logging():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong Password or Username')
        return render_template("login")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/submit')
def submit():
    return render_template("submit.html")
