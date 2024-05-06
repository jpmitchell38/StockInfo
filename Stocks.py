import pandas as pd
import sys
pd.options.mode.chained_assignment = None  # default='warn'
import yfinance as yf #pip install yfinance
from datetime import date, timedelta
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def getTickers():
    """
    Asks the user for up to 8 stock tickers, seperated by a comma
 
    Args:
 
    Returns:
        list: List of all the tickers inputed
    """
    ticker = simpledialog.askstring(title="Question",
                                    prompt="Enter the ticker symbols, seperated by a comma")
    if ticker != "" and type(ticker) != type(None):
        ticker = ticker.upper()
        ticker = ticker.replace(" ", "")
        tickerL = ticker.split(",")
    else:
        messagebox.showerror("Error", "Invalid ticker or format;\n Correct ticker format: AAPL")
        exit(1)
    return tickerL

def getDays(stringToAsk):
    """
    Asks the user for a number based on the dialog given
 
    Args:
        stringToAsk (string): The dialog to ask the user
 
    Returns:
        int: the number that was inputed
    """
    days = simpledialog.askstring(title="Question",
                                    prompt=stringToAsk)
    try:
        int(days)
    except:
        messagebox.showerror("Error", "Invalid integer; Example format: 4")
        exit(1)
    return days

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

def outputConsole(listOfTickers, days):
    """
    loops through the list of tickers and adds information
    about that stock to a string
 
    Args:
        listOfTickers (list): list of tickers
        days (int): how many days back the information should go.
 
    Returns:
        string: information about the stock
    """
    s = ""
    for ticker in listOfTickers:
        data = getStockData(ticker, days)
        pIM, cIP = getStatsReturn(data, days)
        s += ticker + "\n - " + pIM + "\n - " + cIP + "\n\n"
    return s

def graph(listOfTickers, days):
    """
    Loops through the list of tickers and graphs 4 sub plots on one output
 
    Args:
        listOfTickers (list): list Of the Tickers.
        days (int): how many days back the information should go.
 
    Returns:
    """
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    # Loop through tickers, get data for each and plot them on each 4 graphs
    for stock in listOfTickers:
        stock_data = getStockData(stock, days)
        
        # Plot Closing Prices
        ax[0, 0].plot(stock_data['Date'], stock_data['Close'], label=stock)
        ax[0, 0].set_xlabel('Date')
        ax[0, 0].set_ylabel('Closing Price')
        ax[0, 0].set_title('Closing Price of Stock(s) Over Time')
        ax[0, 0].legend()
        ax[0, 0].grid(True)
        ax[0, 0].tick_params(rotation=45)
        ax[0, 0].spines[["top", "right"]].set_visible(False)
        ax[0, 0].grid(linewidth=0.50)

        # Scatter Plot of Closing Price vs. Volume
        ax[0, 1].scatter(stock_data['Close'], stock_data['Volume'], label=stock, alpha=0.5)
        ax[0, 1].set_xlabel('Closing Price')
        ax[0, 1].set_ylabel('Volume')
        ax[0, 1].set_title('Scatter Plot of Closing Price vs Volume')
        ax[0, 1].legend()
        ax[0, 1].grid(True)
        ax[0, 1].spines[["top", "right"]].set_visible(False)
        ax[0, 1].grid(linewidth=0.50)

        # Volume Over Time
        ax[1, 0].bar(stock_data['Date'], stock_data['Volume'], label=stock, alpha=0.5)
        ax[1, 0].set_xlabel('Date')
        ax[1, 0].set_ylabel('Volume')
        ax[1, 0].set_title('Volume of Stock(s) Over Time')
        ax[1, 0].legend()
        ax[1, 0].grid(True)
        ax[1, 0].tick_params(rotation=45)
        ax[1, 0].spines[["top", "right"]].set_visible(False)
        ax[1, 0].grid(linewidth=0.50)

        # High-Low Price Range
        ax[1, 1].fill_between(stock_data['Date'], stock_data['High'], stock_data['Low'], alpha=0.3, label=stock)
        ax[1, 1].plot(stock_data['Date'], stock_data['High'], color='blue', linestyle='--')
        ax[1, 1].plot(stock_data['Date'], stock_data['Low'], color='green', linestyle='--')  
        ax[1, 1].set_xlabel('Date')
        ax[1, 1].set_ylabel('Price')
        ax[1, 1].set_title('High-Low Price Range for Stock(s) Over Time')
        ax[1, 1].legend()
        ax[1, 1].tick_params(rotation=45)
        ax[1, 1].spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    plt.show()

def getStatsReturn(data, days):
    """
    Gets the change in price and percent increase/decrease for the stock
 
    Args:
        data (dataFrame): The first number.
        days (int): how many days back the information should go.
 
    Returns:
        string: a string put together of all the stats for the given stock(s)
    """
    changeInPrice = round((float(data["Close"].iloc[0]) - float(data["Close"].iloc[len(data) - 1])) * -1, 3)
    percentIncrease = round((((float(data["Close"].iloc[0]) - float(data["Close"].iloc[len(data) - 1])) * -1) / (float(data["Close"].iloc[0]))) * 100, 2)

    if percentIncrease > 0:
        strPer = "+" + str(percentIncrease)
    else:
        strPer = str(percentIncrease)

    pIM = "Percent change over " + str(days) +" days: " + str(strPer) + "%"
    cIP = "Change in price over " + str(days) +" days: $" + str(changeInPrice) 

    return pIM, cIP
    
def main():
    ROOT = tk.Tk()
    ROOT.withdraw()

    tryConnectYahoo()

    howMany = getDays("How many stocks do you want to compare? (1-8)")
    if int(howMany) < 1 or int(howMany) > 8:
        messagebox.showerror("Error", "Invalid option; Need a number 1-8")
        exit(1)

    listOfTickers = getTickers()
    if len(listOfTickers) != int(howMany):
        messagebox.showerror("Error", "Invalid number of tickers; Numbers did not match")
        exit(1)

    days = getDays("How many days back do you want data to go?")

    print(outputConsole(listOfTickers, days))
    sys.stdout.flush()
    graph(listOfTickers, days)
          
main()