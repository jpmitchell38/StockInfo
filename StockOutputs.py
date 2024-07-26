import matplotlib.pyplot as plt #pip install matplotlib

from StockConnectAPI import *

def graph(listOfTickers, days):
    """
    Loops through the list of tickers and graphs 4 sub plots on one output
 
    Args:
        listOfTickers (list): list Of the Tickers.
        days (int): how many days back the information should go.
 
    Returns:
    """
    string = ""
    for x in range(0, len(listOfTickers)):
        if len(listOfTickers) == 1:
            string += str(listOfTickers[x])
        else:
            if x + 1 == len(listOfTickers):
                string += "and " + str(listOfTickers[x])
            else:
                string += str(listOfTickers[x]) + ", "
            
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    for stock in listOfTickers:
        stock_data = getStockData(stock, days)
        
        # Plot Closing Prices
        ax[0, 0].plot(stock_data['Date'], stock_data['Close'], label=stock)
        ax[0, 0].set_xlabel('Date')
        ax[0, 0].set_ylabel('Closing Price ($)')
        ax[0, 0].set_title('Closing Price of ' + string + ' over Time')
        ax[0, 0].legend()
        ax[0, 0].grid(True)
        ax[0, 0].tick_params(axis='x', labelrotation=30)
        ax[0, 0].yaxis.set_major_formatter('${x:1.2f}')
        ax[0, 0].spines[["top", "right"]].set_visible(False)
        ax[0, 0].grid(linewidth=0.50)

        # Scatter Plot of Closing Price vs. Volume
        ax[0, 1].scatter(stock_data['Close'], stock_data['Volume'], label=stock, alpha=0.5)
        ax[0, 1].set_xlabel('Closing Price')
        ax[0, 1].set_ylabel('Volume')
        ax[0, 1].set_title('Closing Price of ' + string + ' over Volume')
        ax[0, 1].legend()
        ax[0, 1].grid(True)
        ax[0, 1].xaxis.set_major_formatter('${x:1.2f}')
        ax[0, 1].spines[["top", "right"]].set_visible(False)
        ax[0, 1].grid(linewidth=0.50)

        # Volume Over Time
        ax[1, 0].bar(stock_data['Date'], stock_data['Volume'], label=stock, alpha=0.5)
        ax[1, 0].set_xlabel('Date')
        ax[1, 0].set_ylabel('Volume')
        ax[1, 0].set_title('Volume of ' + string + ' over Time')
        ax[1, 0].legend()
        ax[1, 0].grid(True)
        ax[1, 0].tick_params(axis='x', labelrotation=30)
        ax[1, 0].spines[["top", "right"]].set_visible(False)
        ax[1, 0].grid(linewidth=0.50)

        # High-Low Price Range
        ax[1, 1].fill_between(stock_data['Date'], stock_data['High'], stock_data['Low'], alpha=0.3, label=stock)
        ax[1, 1].plot(stock_data['Date'], stock_data['High'], color='blue', linestyle='--')
        ax[1, 1].plot(stock_data['Date'], stock_data['Low'], color='green', linestyle='--')  
        ax[1, 1].set_xlabel('Date')
        ax[1, 1].set_ylabel('Price ($)')
        ax[1, 1].set_title('High-Low Price Range of ' + string + ' over Time')
        ax[1, 1].legend()
        ax[1, 1].yaxis.set_major_formatter('${x:1.2f}')
        ax[1, 1].tick_params(axis='x', labelrotation=30)
        ax[1, 1].spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    plt.savefig('myIMG.png')
    plt.close('all')

