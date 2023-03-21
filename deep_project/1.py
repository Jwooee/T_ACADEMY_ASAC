from flask import Flask, render_template, request
from calculator import calcBMI
from strok import meodel
import pandas as pd
import numpy as pn
import sys

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/hw1") 
def hw1():
 return render_template('hw1.html')

@app.route("/hw1proc") 
def hw1proc():
    age = int(request.args['age'])
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    obesity = calcBMI( height, weight)
    bmi = obesity
    gender = int(request.args['gender'])
    hypertension = int(request.args['hypertension'])
    heart_disease = int(request.args['heart_disease'])
    ever_married = int(request.args['ever_married'])
    Residence_type = int(request.args['Residence_type'])
    work_type = int(request.args['work_type'])
    avg_glucose_level = int(request.args['avg_glucose_level'])
    smoking_status = int(request.args['smoking_status'])

    result2 = meodel(age, bmi, gender, hypertension, heart_disease,
        ever_married, Residence_type, work_type, avg_glucose_level,
        smoking_status)
    return render_template('hw1proc.html', result2= result2)
    # return render_template('hw1proc.html',result2= result2)

@app.route("/table")
def table():
    df = pd.read_csv(r'predresults2.csv')
    html = {'df' :df.to_html(justify='center')}
    return render_template('table.html', html =html)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/insert")
def insert():
    return render_template('insert.html')

@app.route("/delete")
def delete():
    return render_template('delete.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 4000, debug = True)
