

from flask import Blueprint, render_template, redirect, url_for


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route('/about')
def about():
    return "This is page 2"
