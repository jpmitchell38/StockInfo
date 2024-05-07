import matplotlib.pyplot as plt #pip install matplotlib

from StockConnectAPI import *


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