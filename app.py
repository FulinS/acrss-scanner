import os
from datetime import datetime

#somehow import SQL
from flask import Flask, flash, redirect, render_template, request
import csv

# Configure application
app = Flask(__name__)

# Configure SQLite database
#db = SQL("sqlite:///birthdays.db")

mode="late"
date=datetime.now()
id=[]
with open('static/ids.csv', mode ='r')as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        id.append(lines)

@app.route("/", methods=["GET", "POST"])
def index():
    global mode
    if request.method=="GET":
        return render_template("index.html", md=mode)
    else:
        bt = request.form.get("bt")
        mode=bt
        return redirect("/")

@app.route("/scan", methods=["POST"])
def scan():
    sdtid=request.form.get("barcode")
    for i in id:
        if sdtid==i["Student #"]:
            with open(f"static/{mode}.txt", "a") as f:
                f.write(f"{i["First Name"]} {i["Last Name"]}, {i["Grade"]}, {date.strftime("%H")}:{date.strftime("%M")}:{date.strftime("%S")}\n")
            return render_template("success.html", name=f"{i["First Name"]} {i["Last Name"]}", time=f"at {date.strftime("%H")}:{date.strftime("%M")}:{date.strftime("%S")}", mode=mode)
    return render_template("invalid.html")
