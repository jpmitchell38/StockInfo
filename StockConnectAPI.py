from datetime import date, timedelta
import yfinance as yf #pip install yfinance

def getStockData(tickers, numOfDays):
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

    ticker_str = ' '.join(tickers)

    data = yf.download(ticker_str, start=startdate, end=enddate, group_by='ticker', progress=False)

    all_data = []
    if len(tickers) == 1:
        if data.empty:
            return False, "", tickers[0]
        else:
            data["Date"] = data.index
            data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
            data.reset_index(drop=True, inplace=True)
            all_data.append(data)
    else:
        for ticker in tickers:
            if data.empty:
                return False, "", tickers[0]
            elif data[ticker]['Open'].isna().any():
                return False, "", ticker
            else:
                ticker_data = data[ticker]
                ticker_data["Date"] = ticker_data.index
                ticker_data = ticker_data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
                ticker_data.reset_index(drop=True, inplace=True)
            all_data.append(ticker_data)
    return True, all_data, ""