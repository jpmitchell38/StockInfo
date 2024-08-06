from flask import Flask, request, render_template, Response #pip install flask
from datetime import datetime
import os
import matplotlib

matplotlib.use('Agg') 

from StockConnectAPI import *
from StockOutputs import *

app = Flask(__name__, template_folder='.', static_url_path='', static_folder='')
tickerL = []

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    img_path = None
    
    if request.method == 'HEAD':
        return Response(status=200)
    
    if request.method == 'POST':
        data1 = request.form['first_input_data']
        data2 = request.form['second_input_data']

        if not validate_ticker_format1(data1):
            return render_template('index.html', 
                                   message="Invalid ticker format. Please ensure all tickers are alphabetic",
                                   img_path=img_path)
            
        if not validate_ticker_format2(data2):
            return render_template('index.html', 
                                   message = "Invalid input. Please ensure days back is a number that is greater than 7",
                                   img_path = img_path)

        input = data1.upper()
        input = input.replace(" ", "")
        tickerL = input.split(",")
        
        days = data2
        
        isDataValid, stock = graph(tickerL, days)
        if not isDataValid:
            return render_template('index.html', 
                                   message = stock + " is an invalid ticker",
                                   img_path = img_path)
                
                
        return render_template('index.html', message="", img_path="myIMG.png")
    return render_template('index.html')


def validate_ticker_format1(ticker_string):
    tickers = ticker_string.split(',')
    for ticker in tickers:
        ticker = ticker.strip()
        if not ticker.isalpha():
            return False
    return True

def validate_ticker_format2(days_string):
    if days_string.isdigit():
        days = int(days_string)
        if days >= 7:
            return True
    return False

if __name__ == '__main__':
    app.run()
    
    if os.path.exists("myIMG.png"):
        os.remove("myIMG.png") 