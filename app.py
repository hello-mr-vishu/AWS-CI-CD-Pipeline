import pickle
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        pass
    