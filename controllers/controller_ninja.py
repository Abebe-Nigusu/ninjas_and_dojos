from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

@app.route("/ninjas")
def index():
    return render_template("ninja.html", dojos=Dojo.get_all_dojos())

@app.route('/ninja/create', methods=["POST"])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
