import os
import json
from pathlib import Path
from flask import render_template, request, url_for
from bikeStore import app


@app.route("/")
@app.route("/home")
def home():
    title = "Home"
    return render_template("home.html", title=title)

@app.route("/bikes")
def bikes():
    title = "Bikes"
    return render_template("bikes.html", title=title)

@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)
