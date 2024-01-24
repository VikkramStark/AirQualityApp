from flask import Blueprint, jsonify, request 
from flaskapp.models import GasData 
from flaskapp import db 

gases = Blueprint("gases",__name__)  

@gases.get("/home")
@gases.get("/info") 
def home():
    return "<h1>Hello World!</h1><h2>POST a request to feed Data into Database</h2>"   

@gases.route("/",methods = ["POST"])
def post_gas():
    data = request.get_json(force = True) 
    #oxygen = data.get("oxygen")  
    hydrogen = data.get("hydrogen") 
    methane = data.get("methane") 
    #cmo = data["cmo"] 
    co2 = data.get("co2") 
    gas = GasData(hydrogen = hydrogen, methane = methane, co2 = co2) #oxygen, cmo  
    try:
        db.session.add(gas) 
        db.session.commit() 
        print("Data Added Successfully!!")  
        return jsonify({"message":"Data Added Successfully"}), 200  
    except Exception as e: 
        db.session.rollback() 
        print(e) 
        return jsonify({"message":"An Exception Occured!!"}), 400  
    

@gases.route("/", methods = ["GET"])  
def get_gases():
    gases = GasData.query.all() 
    res = [] 
    for gas in gases:
        data = {"id":gas.id, "methane":gas.methane, "hydrogen":gas.hydrogen, "co2":gas.co2,"timestamp":gas.timestamp}  # "oxygen":gas.oxygen, "cmo":gas.cmo,
        res.append(data) 

    return jsonify(res)    

@gases.route("/delete/all") 
def clear_all_values():
    GasData.query.delete() 
    db.session.commit() 
    return jsonify({"message", "values cleared successfully!!"}),200 