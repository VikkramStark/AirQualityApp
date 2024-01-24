from flaskapp import app 
from flaskapp.gases import gases 

app.register_blueprint(gases, url_prefix = "/gases")    

@app.route("/") 
def home():
    return "Hello World!"   