from flask import Flask, request
import json 
from flask import jsonify

app = Flask(__name__)

db = []


def add_patient_to_db(name, id, blood_type): 
    new_patient = {"name": name, "id": id, 
                    "blood_type": blood_type, "test": {}}
    db.append(new_patient)
    return True


def init_server(): 
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")


@app.route("/add_patient", methods = ["POST"])
def add_patient(): 
    #Get the data from the request
    in_data = request.get_json()
    #Call Other function to do the request
    answer = add_patient_driver(in_data)
    #Provide a response
    return jsonify(answer)


@app.route("/new_patient", methods = ["POST"])
def new_patient():
    in_data = request.get_json()
    answer = add_new_patient(in_data)
    return jsonify(answer
    

@app.route("/get_results/<patient_id>", methods = ["GET"])
def get_resutls(patient_id):
    for patient in db:
        if patient["id"] == int(patient_id):
            return jasonify(patient["test"]). 200 
    return "Patient id {} is not a database".formate(patient_id), 400


def validate_patient_id(patient_id):
    try:
        patient_id_int = int(patient_id)
    except ValueError:
        return "Patient id was not ineger", 400 
    return True, 200

    

def add_patient_driver(in_data):
    answer, status_code = add_validate_add_patient_input(in_data)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    print(db)
    return True


def add_validate_add_patient_input(in_data):
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_massage = "Key {} is missing\n".format(key)
            return error_message, 400 
        if type(in_data[key]) is not expected_type:
            error_message = "value of key {} is not of \
                            type {}".formate(key, expected_type)
    return True, 200 


if __name__ == "__main__":
    init_server()
    app.run()

