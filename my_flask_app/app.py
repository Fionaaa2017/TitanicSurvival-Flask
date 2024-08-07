#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:02:04 2024

@author: niqiubao
"""

from flask import Flask,request,render_template
import pickle
import os
import numpy as np

app=Flask(__name__)
print(os.getcwd())

model=pickle.load(open('models/model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    features=[]
    values=[x for x in request.form.values()]
    #Add age
    features.append(float(values[0]))
    #Add sex
    if values[1]=='female':
        features.append(0)
    else:
        features.append(1)
    #Add class
    if values[3]=='Pclass_1':
        features.append(0)
        features.append(0)
    elif values[3]=='Pclass_2':
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(1)
        

    features_final=[np.array(features)]
    prediction=model.predict(features_final)
    
    if prediction==1:
        output="You will survive in Titanic Disaster 😃"
    elif prediction==0:
        output="You will not survive in the Titanic Disaster 😭"
    
    return render_template('index.html',prediction_text=output)


if __name__=="__main__":
    app.run(debug=True)
