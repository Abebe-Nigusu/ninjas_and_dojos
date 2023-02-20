from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.model_dojo import Dojo

@app.route("/dojos")
def index_dojo():
    all_dojos = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos=all_dojos)

@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")

@app.route('/dojo/<int:id>')
def join_dojo_ninja(id):
    data = {
        "id": id
    }
    all_dojos=Dojo.get_one_with_ninjas(data)

    return render_template('dojo.html',  all_dojos=all_dojos)

if __name__ == "__main__":
    app.run(debug=True)
