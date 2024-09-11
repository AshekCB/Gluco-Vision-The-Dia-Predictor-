from flask import Flask,render_template,request,redirect,url_for
import bmi_caluclator 
import age_caluclator
import databases as db
from checking_booking import check_appointment
import models as model

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("home.html")


@app.route("/about",methods=["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/bmi",methods=["POST","GET"])
def bmi():
    if request.method=="POST":
        h=request.form['height']
        w=request.form['weight']
        result=bmi_caluclator.caluclate(float(w),float(h))
        return render_template("bmi_cal.html",result=float(result))
    else:
        return render_template("bmi_cal.html",result="")


@app.route("/age",methods=["POST","GET"])
def age():
    if request.method=="POST":
        by=request.form['birthyear']
        result=age_caluclator.caluclator(int(by))
        return render_template("age.html",result=result)
    else:
        return render_template("age.html",result="")
    
@app.route("/appointments",methods=["POST","GET"])
def appointments():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        doctor = request.form['doctor']
        desc=request.form['description']

        result=db.book_appointment(name,email,phone,date,time,doctor,desc)
        return render_template("appointments.html",result=result)
    else:
        return render_template("appointments.html")
    
@app.route("/checkings",methods=["POST","GET"])
def checkings():
    if request.method=="POST":
        bid=request.form['booking_id']
        result=check_appointment(str(bid))
        return render_template("bookings.html",result=result)
    else:
        return render_template("bookings.html")

@app.route("/predictions",methods=["POST","GET"])
def predictions():
    if request.method=="POST":
        preg=request.form['pregnancies']
        gluco=request.form['glucose']
        bp=request.form['bloodPressure']
        sthick=request.form['skinThickness']
        ins=request.form['insulin']
        bmi=request.form['bmi']
        pedgree=request.form['pedigreeFunction']
        age=request.form['age']

        result=model.predictor(int(preg),float(gluco),int(bp),float(sthick),int(ins),float(bmi),float(pedgree),int(age))

        return redirect(url_for('result', result=result))
    else:
        return render_template("predictions.html")

@app.route("/result")
def result():
    
    result = request.args.get('result', type=int)
    return render_template("result.html", result=result)



@app.route("/guard",methods=["POST","GET"])
def guard():
    if request.method=="POST":
        return render_template("guard.html")
    else:
        return render_template("guard.html") 
       






if __name__=="__main__":
    app.run(debug=True)
