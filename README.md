# StockInfo

This project allows users to input a list of stocks and specify the number of days back from which to retrieve data. It fetches this data and presents four insightful graphs: Closing Price vs Time, Closing Price vs Volume, Volume vs Time, and High-Low Range vs Time.

<div style="display: flex; justify-content: space-between;">
    <img src="docs/Screenshot 2024-07-15 142147.png" alt="Graph 1" style="width: 45%;"/>
    <img src="docs/Screenshot 2024-07-15 144409.png" alt="Graph 2" style="width: 45%;"/>
</div>

<br>
## How Its Made:

Tech used: Python, HTML, CSS

I utilized Python for the backend of this project, enabling connectivity to the Yahoo Finance API to fetch stock data dynamically. With Flask, I managed incoming inputs from the web interface. The HTML structure neatly organizes content for easy styling with CSS.

<br>
## How to Run

###
    git clone https://github.com/jpmitchell38/StockInfo.git

### 
    cd StockInfo/

###
    pip install -r requirements.txt

###
    python StockMain.py

You can copy the URL provided, which starts with "http://"

<br>
## Side Note

Both the accounts that you see contributed to the projects are mine