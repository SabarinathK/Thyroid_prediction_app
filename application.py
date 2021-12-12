from flask import Flask,render_template, request, jsonify
import numpy as np
import joblib


appplication = Flask(__name__)


@appplication.route("/", methods=['GET','POST'])
def home():  
    return render_template("index.html")


@application.route("/prediction", methods=['POST'] )
def prediction():
    if request.method == "POST":
        TSH =(request.form["TSH"])
        FTI =(request.form["FTI"])
        TT4 =(request.form["TT4"])
        T3 =(request.form["T3"])
        query_hypothyroid =(request.form["query_hypothyroid"])
        on_thyroxine =(request.form["on_thyroxine"])
        sex =(request.form["sex"])
        pregnant =(request.form["pregnant"])
        psych =(request.form["psych"])
        model=joblib.load("Thyroid_Disease_Detection.pkl")
        arr=np.array([[TSH, FTI ,TT4, T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])
        prediction=model.predict(arr)
        
    return render_template('after.html',data=prediction)


if __name__ == "__main__":
    application.run() 
