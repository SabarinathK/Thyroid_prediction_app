from flask import Flask,render_template, request, jsonify
import numpy as np
import joblib


appplication = Flask(__name__)


@appplication.route('/')
def home():  
    return render_template("index.html")





if __name__ == "__main__":
    application.run() 
