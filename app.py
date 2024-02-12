from flask import Flask, render_template, url_for,request
import pickle as p
import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



modelfile = 'models/final_prediction.pickle'  
model = p.load(open(modelfile, 'rb'))
scaler= pickle.load(open('models/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/predict',methods =['GET','POST'])
def predict():
    principal_1st = float(request.form["1st_principal"])
    principal_2nd =float(request.form['2nd_principal'])
    principal_3rd= float(request.form['3rd_principal'])
    principal_4th=float(request.form['4th_principal'])
    principal_5th = float(request.form['5th_principal'])
    principal_6th  = float(request.form['6th_principal'])
    principal_7th= float(request.form['7th_principal'])
    principal_8th=float(request.form['8th_principal'])
    principal_9th = float(request.form['9th_principal'])
    principal_10th =float(request.form['10th_principal'])


    total = [[principal_1st, principal_2nd, principal_3rd, principal_4th,principal_5th,principal_6th,principal_7th,
               principal_8th,principal_9th, principal_10th]]
    prediction = model.predict(scaler.transform(total))
    prediction = int(prediction[0])
    print( prediction)

    if prediction==0:
        return render_template('index.html',predict="Predicts wafer is bad")
   
    else: 
        return render_template('index.html',predict="Predicts wafer is good")
    


    




if __name__ == '__main__':
    app.run(debug=True)
