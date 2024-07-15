# StockInfo

This project asks the user for a list of stocks, and how many days back do you want to grab data from. It fetches the data then has an output of four graphs. Closing Price vs Time, Closing Price vs Volume, Volume Vs Time, High-Low Range vs Time.  

![alt text](<docs/Screenshot 2024-07-15 142147.png>)

## How Its Made:

Tech used: Python, HTML, CSS

I used python for the backend part of the project, where I can connect to the yahoo finance api and grab data about a stock and put it into a graph. Using the Flask package in python im able to listen to the inputs coming from the website. The html file organizes the different content so im able to style them with css. 

## How to Run

```git clone https://github.com/jpmitchell38/StockInfo.git```

cd into directory (StockInfo)

```pip install -r requirements.txt```

```python StockMain.py```

copy the url it gives you that starts with "http://"


