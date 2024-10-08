import os
import io
import matplotlib
import csv
import tempfile
import base64

from flask import Flask, request, render_template, Response
from datetime import datetime
from helperfiles.StockConnectAPI import *
from helperfiles.StockOutputs import *

matplotlib.use('Agg') 

app = Flask(__name__, template_folder='.', static_url_path='', static_folder='')
tickerL = []

TEMP_UPLOAD_FOLDER = tempfile.mkdtemp()


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
        
        img_bytes, isDataValid, stock = graph(tickerL, days)
        if not isDataValid:
            message = stock + " is an invalid ticker"
            return render_template('index.html', 
                                   message=message,
                                   img_path=img_path)
                
        if img_bytes:
            return render_template('index.html', message=message, img_data=img_bytes.getvalue())
    return render_template('index.html', img_path=img_path)


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
    
@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    message = None
    ticker = None
    pe = None
    peg = None
    div = None
    profit = None
    short = None
    isValid = None
    price = None

    if request.method == 'POST':
        ticker = request.form.get('first_input_data', '').strip().upper()
        if not ticker.isalpha():
            message = "Invalid ticker. Please ensure it is alphabetic."
        else:
            pe, peg, div, profit, short, isValid, price = get_metrics(ticker)
            if not isValid:
                isValid = None
                message = "Invalid ticker"
            else:
                isValid = 0
                if pe is not None:
                    pe = round(pe, 2)
                if peg is not None:
                    peg = round(peg, 2)
                if div is not None:
                    div = round(div, 2)
                if profit is not None:
                    profit = round(profit, 2)
                if short is not None:
                    short = round(short, 2)

    try:
        return render_template('metrics.html', message=message, ticker=ticker, pe=pe, peg=peg, div=div, profit=profit, short=short, isValid=isValid, price=price)
    except Exception as e:
        return "Error rendering template", 500

@app.route('/report', methods=['GET', 'POST'])
def report():
    message = None
    csv_data = None
    
    if request.method == 'POST':
        data1 = request.form['first_input_data']
        
        if not validate_ticker_format1(data1):
            message = "Invalid ticker format. Please ensure all tickers are alphabetic"
            return render_template('report.html', message=message)
        
        input = data1.upper()
        input = input.replace(" ", "")
        tickerL = input.split(",")
        
        try:
            data = getReport(tickerL)
            if len(data) == 0:
                message = "Invalid ticker"
            else:
                csv_output = io.StringIO()
                csv_writer = csv.writer(csv_output)
                csv_writer.writerows(data)
                csv_output.seek(0)
                csv_data = csv_output.getvalue() 
        except:
            message = "Request timed out"
    
    return render_template('report.html', message=message, csv_data=csv_data)

@app.route('/download')
def download_file():
    csv_data = request.args.get('csv_data')
    
    if not csv_data:
        return "No file data found", 400

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=report.csv"}
    )
    
@app.template_filter('b64encode')
def b64encode(data):
    return base64.b64encode(data).decode('utf-8')

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