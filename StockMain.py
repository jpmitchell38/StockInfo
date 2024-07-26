from flask import Flask, request, render_template #pip install flask
import os
import matplotlib
matplotlib.use('Agg') 

from StockConnectAPI import *
from StockOutputs import *

# Put the stocks and the time above the graphs

app = Flask(__name__, template_folder='.', static_url_path='', static_folder='')
tickerL = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data1 = request.form['first_input_data']
        data2 = request.form['second_input_data']


        input = data1.upper()
        input = input.replace(" ", "")
        tickerL = input.split(",")
        
        days = data2
        
        graph(tickerL, days)
                
                
        return render_template('index.html', message="Data submitted successfully!", img_path="myIMG.png")
    return render_template('index.html')



def main():
    app.run()
    
    if os.path.exists("myIMG.png"):
        os.remove("myIMG.png")
          
main()