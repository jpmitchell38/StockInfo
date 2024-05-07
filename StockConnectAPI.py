from tkinter import messagebox
from datetime import date, timedelta
import yfinance as yf #pip install yfinance



def tryConnectYahoo():
    """
    Tries to connect with yahoo finance with apple just to make sure it can connect.
    If it fails to connect, it shuts down the program and spits out an error.
 
    Args:
 
    Returns:

    """
    today = date.today()

    enddate = today.strftime("%Y-%m-%d")
    startdate = date.today() - timedelta(days=int(30))
    startdate = startdate.strftime("%Y-%m-%d")

    try:
        data = yf.download("AAPL", 
                            start=startdate, 
                            end=enddate, 
                            progress=False)
        data["Date"] = data.index
        data = data[["Date", "Open", "High", 
                "Low", "Close", "Adj Close", "Volume"]]
        data.reset_index(drop=True, inplace=True)
    except:
        messagebox.showerror("Error", "Can't connect to yahoo currently")
        exit(1)
    finally:
        if len(data) == 0:
            messagebox.showerror("Error", "Can't connect to yahoo currently")
            exit(1)

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

    data = yf.download(nameOfStock, 
                            start=startdate, 
                            end=enddate, 
                            progress=False)
    if len(data) == 0:
        messagebox.showerror("Error", "Invalid ticker or format;\n Correct ticker format: AAPL")
        exit(1)

    data["Date"] = data.index
    data = data[["Date", "Open", "High", 
                "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)

    return data