from flask import Blueprint, render_template
from canteen.models import create_table

riviera = Blueprint("riviera", __name__)

@riviera.route("/riviera")
def index():
    create_table("")
    return render_template("riviera/index.html")


def menu():
    return render_template("riviera/menu.html")