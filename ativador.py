from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)

class Register(db.Model): #THIS COULD BE ENCAPSULATED IN ITS OWN FILE, BUT IT IS LOCATED HERE FOR SIMPLICTY
    id = db.Column(db.Integer, primary_key=True)
    activation_key = db.Column(db.String(32), unique = True, nullable = False)
    application_key = db.Column(db.String(32), unique = True, nullable = False)

@app.route('/activate', methods=['POST'])
def activate():
    if request.method == "POST":

        data = request.json

        #print(str(data["activation_key"]))

        #activation_key = 

        result = Register.query.filter_by(activation_key=str(data["activation_key"])).first()

        #print(result)

        if result is not None:
            return jsonify({"result": "success", "application_key": result.application_key}) #"application_key": result.application_key

        return jsonify({"result": "failure"})
    else:
        return jsonify({"POST only!"});

#TODO: SERVICE FOR LOADING THE KEYS INTO THE DATABASE (CAN BE DONE MANUALLY TOO)

if __name__ == "__main__":
    app.run(debug=True)