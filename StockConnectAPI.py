# from tkinter import messagebox
from datetime import date, timedelta
import yfinance as yf #pip install yfinance
import contextlib
import os

def getStockData(nameOfStock, numOfDays):
    """
    Connects to the yahoo finance api and grabs data for the given stock,
    for a certain number of days back to present
 
    Args:
        nameOfStock (string): the name of the stock ticker 
        numOfDays (int): The number of days back you want to get data
 
    Returns:
        dataFrame: infomation about the stock
    """
    today = date.today()

    enddate = today.strftime("%Y-%m-%d")
    startdate = date.today() - timedelta(days=int(numOfDays))
    startdate = startdate.strftime("%Y-%m-%d")

    with open(os.devnull, 'w') as fnull:
            with contextlib.redirect_stderr(fnull):
                data = yf.download(nameOfStock, 
                            start=startdate, 
                            end=enddate, 
                            progress=False)

    if len(data) == 0:
        return False, data
    else:
        data["Date"] = data.index
        data = data[["Date", "Open", "High", 
                    "Low", "Close", "Adj Close", "Volume"]]
        data.reset_index(drop=True, inplace=True)

        return True, data