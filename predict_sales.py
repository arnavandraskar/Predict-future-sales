#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics import mean_squared_error
from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return flask.render_template('D:/Case Study/Predict future sales/index.html')

@app.route('/predict', methods=['POST'])
def predict_sales():
    '''
    This function will return prediction of future sale. 
    '''
    
    with open('D:/Case Study/Predict future sales/lgb_grid_2b','rb') as loc:
        best_model = pickle.load(loc)
        
    #with open('D:/Case Study/Predict future sales/data_val','rb') as loc:
    #    X_val = pickle.load(X_val)
    
    with open('D:/Case Study/Predict future sales/data_test','rb') as loc:
        X_test = pickle.load(loc)
        
    to_predict_list = request.form.to_dict()
    try: 
        pred = best_model.predict(X_test[X_test.shop_id == int(to_predict_list['shop_id'])][X_test.item_id == int(to_predict_list['item_id'])])
        return 'prediction : {}'.format(int(pred))
    
    except:
        return "Please enter valid shop_id/item_id"
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)       

