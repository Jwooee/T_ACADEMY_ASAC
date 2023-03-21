from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_args
import random
from tensorflow.keras.models import load_model
import tensorflow.keras.preprocessing.image as p
from datetime import datetime

model = load_model('C:/Users/NTX550/Desktop/WED_D/static/fashion_cnn_main.h5')

def classFashion(img):
    tili = ['golf', 'soccer', 'street', 'suit', 'sweat']
    testImg = p.load_img(img, target_size=(256,256) )
    imgArr = p.img_to_array(testImg)/255
    return tili[int(model.predict(imgArr.reshape(1,256,256,3)).argmax(axis=1))]


app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/name2")
def name2():
    return render_template('name2.html')


@app.route("/name4")
def name4():
    return render_template('name4.html')


@app.route("/name3", methods=["POST", "GET"])
def name3():
    rd = random.randrange(1, 90)

    try:
        if request.form["golf"] == "":
            res = f"../static/image/골프패션/{rd}.jpg"
    except:
        try:
            if request.form["street"] == "":
                res = f"../static/image/스트릿패션/스트릿패션_{rd}.jpg"    
        except:
            try:
                if request.form["suit"] == "":
                    res = f"../static/image/정장패션/정장패션_{rd}.jpg"
            except:
                try:
                    if request.form["soccer"] == "":
                        res = f"../static/image/축구패션/{rd}.jpg"
                except:
                    if request.form["sweats"] == "":
                        res = f"../static/image/츄리닝패션/츄리닝패션_{rd}.jpg"
    return render_template('name3.html', res=res)

@app.route("/guess", methods=["POST","GET"])
def guess():
    return render_template('guess.html')





@app.route("/result", methods=["POST","GET"])
def file():
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    myfile = request.files["myfile"]
    print(myfile.filename)
    myfile.save(f"C:/Users/NTX550/Desktop/WED_D/static/newimage/{current_time}.jpg")
    result = classFashion(f"C:/Users/NTX550/Desktop/WED_D/static/newimage/{current_time}.jpg")
    return render_template('result.html', result=result, filepath=f"../static/newimage/{current_time}.jpg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
