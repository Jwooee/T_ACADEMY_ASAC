from flask import Flask, render_template, request
import pandas as pd
from flask_paginate import Pagination, get_page_args # 페이징 무조건 해야지...
import dbcontrol as dbc

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.html")

@app.route("/mainpage")
def mainpage():
    return render_template("mainpage2.html")

@app.route("/uhanmain")
def uhanmain():
    return render_template("uhanmain.html")


@app.route("/uhanbase")
def uhanbase():
    data = dbc.selectbase("(주)유한양행")
    return render_template("uhanbase.html", data=data)

@app.route("/uhanresult")
def uhanresult():
    pname = request.args["pname"]
    data = dbc.selectmed("(주)유한양행", pname)
    # 여기두.. 대신 조건문으로 넣어서 뾰로롱
    return render_template("uhanbase.html", data=data)

# 유한양행 의약품
@app.route("/uhanmed")
def uhanmed():
    return render_template("uhanmed.html")
@app.route("/uhanbase1")
def uhanbase1():
    data = dbc.selectbase1("(주)유한양행")
    return render_template("uhanbase.html", data=data)
@app.route("/uhanresult1")
def uhanresult1():
    pname = request.args["pname"]
    data = dbc.selectmed1("(주)유한양행", pname)
    return render_template("uhanbase.html", data=data)





# 유한양행 의약외품
@app.route("/uhanmed2")
def uhanmed2():
    return render_template("uhanmed2.html")
@app.route("/uhanbase2")
def uhanbase2():
    data = dbc.selectbase2("(주)유한양행")
    return render_template("uhanbase.html", data=data)
@app.route("/uhanresult2")
def uhanresult2():
    pname = request.args["pname"]
    data = dbc.selectmed2("(주)유한양행", pname)
    return render_template("uhanbase.html", data=data)





# 유한양행 한약(생약)
@app.route("/uhanmed3")
def uhanmed3():
    return render_template("uhanmed3.html")
@app.route("/uhanbase3")
def uhanbase3():
    data = dbc.selectbase3("(주)유한양행")
    return render_template("uhanbase.html", data=data)
@app.route("/uhanresult3")
def uhanresult3():
    pname = request.args["pname"]
    data = dbc.selectmed3("(주)유한양행", pname)
    return render_template("uhanbase.html", data=data)



### 여기부터 녹십자

@app.route("/nokmain")
def nokmain():
    return render_template("nokmain.html")


@app.route("/nokbase")
def nokbase():
    data = dbc.selectbase("(주)녹십자")
    return render_template("uhanbase.html", data=data)

@app.route("/nokresult")
def nokresult():
    pname = request.args["pname"]
    data = dbc.selectmed("(주)녹십자", pname)
    # 여기두.. 대신 조건문으로 넣어서 뾰로롱
    return render_template("uhanbase.html", data=data)

# 녹십자 의약품
@app.route("/nokmed")
def nokmed():
    return render_template("nokmed.html")
@app.route("/nokbase1")
def nokbase1():
    data = dbc.selectbase1("(주)녹십자")
    return render_template("uhanbase.html", data=data)
@app.route("/nokresult1")
def nokresult1():
    pname = request.args["pname"]
    data = dbc.selectmed1("(주)녹십자", pname)
    return render_template("uhanbase.html", data=data)





# 녹십자 의약외품
@app.route("/nokmed2")
def nokmed2():
    return render_template("nokmed2.html")
@app.route("/nokbase2")
def nokbase2():
    data = dbc.selectbase2("(주)녹십자")
    return render_template("uhanbase.html", data=data)
@app.route("/nokresult2")
def nokresult2():
    pname = request.args["pname"]
    data = dbc.selectmed2("(주)녹십자", pname)
    return render_template("uhanbase.html", data=data)





# 녹십자 한약(생약)
@app.route("/nokmed3")
def nokmed3():
    return render_template("nokmed3.html")
@app.route("/nokbase3")
def nokbase3():
    data = dbc.selectbase3("(주)녹십자")
    return render_template("uhanbase.html", data=data)
@app.route("/nokresult3")
def nokresult3():
    pname = request.args["pname"]
    data = dbc.selectmed3("(주)녹십자", pname)
    return render_template("uhanbase.html", data=data)


### 광동제약


@app.route("/kwangmain")
def kwangmain():
    return render_template("kwangmain.html")


@app.route("/kwangbase")
def kwangbase():
    data = dbc.selectbase("광동제약(주)")
    return render_template("uhanbase.html", data=data)

@app.route("/kwangresult")
def kwangresult():
    pname = request.args["pname"]
    data = dbc.selectmed("광동제약(주)", pname)
    # 여기두.. 대신 조건문으로 넣어서 뾰로롱
    return render_template("uhanbase.html", data=data)

# 광동제약 의약품
@app.route("/kwangmed")
def kwangmed():
    return render_template("kwangmed.html")
@app.route("/kwangbase1")
def kwangbase1():
    data = dbc.selectbase1("광동제약(주)")
    return render_template("uhanbase.html", data=data)
@app.route("/kwangresult1")
def kwangresult1():
    pname = request.args["pname"]
    data = dbc.selectmed1("광동제약(주)", pname)
    return render_template("uhanbase.html", data=data)





# 광동제약 의약외품
@app.route("/kwangmed2")
def kwangmed2():
    return render_template("kwangmed2.html")
@app.route("/kwangbase2")
def kwangbase2():
    data = dbc.selectbase2("광동제약(주)")
    return render_template("uhanbase.html", data=data)
@app.route("/kwangresult2")
def kwangresult2():
    pname = request.args["pname"]
    data = dbc.selectmed2("광동제약(주)", pname)
    return render_template("uhanbase.html", data=data)


# 광동제약 한약(생약)
@app.route("/kwangmed3")
def kwangmed3():
    return render_template("kwangmed3.html")
@app.route("/kwangbase3")
def kwangbase3():
    data = dbc.selectbase3("광동제약(주)")
    return render_template("uhanbase.html", data=data)
@app.route("/kwangresult3")
def kwangresult3():
    pname = request.args["pname"]
    data = dbc.selectmed3("광동제약(주)", pname)
    return render_template("uhanbase.html", data=data)

@app.route("/addmed")
def addmed():
    return render_template("addmed.html")

@app.route("/addProc")
def addProc():
    adminid = request.args["adminid"]
    adminpw = int(request.args["adminpw"])
    if adminid!="admin" and adminpw!=123123:
        result = "운영자 아이디/비밀번호를 확인하세요"
    else:
        pname = request.args["pname"]
        cname = request.args["cname"]
        cat = request.args["cat"]
        desc_med = request.args["desc_med"]
        shape = request.args["shape"]

        result = dbc.insertmed(pname, cname, cat, desc_med, shape)
    return render_template("addProc.html", result=result)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=4000, debug=True)