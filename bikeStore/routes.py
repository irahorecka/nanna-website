import os
import json
from pathlib import Path
from flask import render_template, request, url_for
from bikeStore import app


@app.route("/")
@app.route("/home")
def home():
    title = "Horecka Bikes"
    return render_template("home.html", title=title)
