from flaskapp import db, app 
from datetime import datetime 

class GasData(db.Model):
    id = db.Column(db.Integer, primary_key = True)  
    # cluster_id = db.Column(db.Integer, nullable = False)   
    #oxygen = db.Column(db.Integer, nullable = False) 
    #cmo = db.Column(db.Integer, nullable = False) 
    co2 = db.Column(db.Integer, nullable = False) 
    methane = db.Column(db.Integer, nullable = False) 
    hydrogen = db.Column(db.Integer,nullable = False) 
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)  

with app.app_context() as appc:  
    appc.push()  
    db.create_all() 

