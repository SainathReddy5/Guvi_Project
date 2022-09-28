from types import BuiltinMethodType
from flask import Flask,request
from flask import render_template
import pickle
import pandas as pd
import numpy as np
import flask_cors

app = Flask(__name__)

pipe = pickle.load(open("pipe.pkl","rb"))

@app.route("/")
def hello_world():
    return render_template('index.html')
    pass
    
@app.route("/predict",methods=['POST'])
def predict():
    AREA = request.form.get("AREA")
    INT_SQFT = request.form.get("INT_SQFT")
    N_ROOMS = request.form.get("N_ROOMS")
    N_BEDROOMS = request.form.get("N_BEDROOMS")
    N_BATHROOMS = request.form.get("N_BATHROOMS")
    PARK_FACIL = request.form.get("PARK_FACIL")
    BUILDTYPE = request.form.get("BUILDTYPE")
    UTLIAVAIL = request.form.get("UTIL_AVAIL")
    STREET = request.form.get("STREET")
    MZZONE = request.form.get("MZZONE")
    AGE = request.form.get("AGE")

    input = pd.DataFrame([[AREA,INT_SQFT,N_BEDROOMS,N_BATHROOMS,N_ROOMS,PARK_FACIL,BUILDTYPE,UTLIAVAIL,STREET,MZZONE,AGE]],columns=['AREA','INT_SQFT','N_BEDROOM','N_BATHROOM','N_ROOM','PARK_FACIL','BUILDTYPE','UTILITY_AVAIL','STREET','MZZONE','AGE'])
    prediction = pipe.predict(input)[0]


    return str(prediction)
    pass


if __name__ == '__main__':
    app.run(debug=True)
