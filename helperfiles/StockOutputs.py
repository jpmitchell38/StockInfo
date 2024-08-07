import matplotlib.pyplot as plt #pip install matplotlib

from helperfiles.StockConnectAPI import *

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
        elif len(listOfTickers) == 2:
            string += str(listOfTickers[x]) + " and " + str(listOfTickers[x + 1])
            break
        else:
            if x + 1 == len(listOfTickers):
                string += "and " + str(listOfTickers[x])
            else:
                string += str(listOfTickers[x]) + ", "
            
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    validData, stock_data, badTicker = getStockData(listOfTickers, days)
    if (not validData):
        return False, badTicker

    count = 0
    for stock in stock_data:
        ax[0, 0].plot(stock['Date'], stock['Close'], label=listOfTickers[count])
        ax[0, 0].set_xlabel('Date')
        ax[0, 0].set_ylabel('Closing Price ($)')
        ax[0, 0].set_title('Closing Price of ' + string + ' over Time')
        ax[0, 0].legend()
        ax[0, 0].grid(True)
        ax[0, 0].tick_params(axis='x', labelrotation=30)
        ax[0, 0].yaxis.set_major_formatter('${x:1.2f}')
        ax[0, 0].spines[["top", "right"]].set_visible(False)
        ax[0, 0].grid(linewidth=0.50)

        ax[0, 1].scatter(stock['Close'], stock['Volume'], label=listOfTickers[count], alpha=0.5)
        ax[0, 1].set_xlabel('Closing Price')
        ax[0, 1].set_ylabel('Volume')
        ax[0, 1].set_title('Closing Price of ' + string + ' over Volume')
        ax[0, 1].legend()
        ax[0, 1].grid(True)
        ax[0, 1].xaxis.set_major_formatter('${x:1.2f}')
        ax[0, 1].spines[["top", "right"]].set_visible(False)
        ax[0, 1].grid(linewidth=0.50)

        ax[1, 0].bar(stock['Date'], stock['Volume'], label=listOfTickers[count], alpha=0.5)
        ax[1, 0].set_xlabel('Date')
        ax[1, 0].set_ylabel('Volume')
        ax[1, 0].set_title('Volume of ' + string + ' over Time')
        ax[1, 0].legend()
        ax[1, 0].grid(True)
        ax[1, 0].tick_params(axis='x', labelrotation=30)
        ax[1, 0].spines[["top", "right"]].set_visible(False)
        ax[1, 0].grid(linewidth=0.50)

        ax[1, 1].fill_between(stock['Date'], stock['High'], stock['Low'], alpha=0.3, label=listOfTickers[count])
        ax[1, 1].plot(stock['Date'], stock['High'], color='blue', linestyle='--')
        ax[1, 1].plot(stock['Date'], stock['Low'], color='green', linestyle='--')  
        ax[1, 1].set_xlabel('Date')
        ax[1, 1].set_ylabel('Price ($)')
        ax[1, 1].set_title('High-Low Price Range of ' + string + ' over Time')
        ax[1, 1].legend()
        ax[1, 1].yaxis.set_major_formatter('${x:1.2f}')
        ax[1, 1].tick_params(axis='x', labelrotation=30)
        ax[1, 1].spines[["top", "right"]].set_visible(False)
        
        count += 1

    plt.tight_layout()
    plt.savefig('myIMG.png')
    plt.close('all')
    return True, ""

