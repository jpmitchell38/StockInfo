from flask import Flask, request, render_template, Response, redirect, url_for #pip install flask
from datetime import datetime
import os
import matplotlib

matplotlib.use('Agg') 

from helperfiles.StockConnectAPI import *
from helperfiles.StockOutputs import *

app = Flask(__name__, template_folder='.', static_url_path='', static_folder='')
tickerL = []

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    message = None
    img_path = None
    
    if request.method == 'HEAD':
        return Response(status=200)
    
    if request.method == 'POST':
        data1 = request.form['first_input_data']
        data2 = request.form['second_input_data']

        if not validate_ticker_format1(data1):
            message = "Invalid ticker format. Please ensure all tickers are alphabetic"
            return render_template('index.html', 
                                   message=message,
                                   img_path=img_path)
            
        if not validate_ticker_format2(data2):
            messsage = "Invalid input. Please ensure days back is a number that is greater than 7"
            return render_template('index.html', 
                                   message = messsage,
                                   img_path = img_path)

        input = data1.upper()
        input = input.replace(" ", "")
        tickerL = input.split(",")
        
        days = data2
        
        isDataValid, stock = graph(tickerL, days)
        if not isDataValid:
            message = stock + " is an invalid ticker"
            return render_template('index.html', 
                                   message = message,
                                   img_path = img_path)
                
                
        return render_template('index.html', message=message, img_path="myIMG.png")
    return render_template('index.html')


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    average_score = None
    message = None
    ticker = None
    rounded = None

    if request.method == 'POST':
        ticker = request.form.get('first_input_data', '').strip().upper()
        if not ticker.isalpha():
            message = "Invalid ticker. Please ensure it is alphabetic."
        else:
            average_score, rounded = get_recommendation_trends(ticker)
            if average_score == -1:
                message = "Invalid ticker"

    try:
        return render_template('analysis.html', analysis=average_score, message=message, ticker=ticker, rounded=rounded)
    except Exception as e:
        return "Error rendering template", 500


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