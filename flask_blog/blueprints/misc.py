from flask import Blueprint, render_template

misc = Blueprint('misc', __name__,template_folder="../templates")


@misc.get("/")
def main():
    return render_template("main.html")
