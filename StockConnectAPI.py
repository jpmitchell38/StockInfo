from datetime import date, timedelta
import yfinance as yf #pip install yfinance
import finnhub
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('FINNHUB_API_KEY')
finnhub_client = finnhub.Client(api_key=api_key)

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

def get_recommendation_trends(symbol):
    recommendation_trends = finnhub_client.recommendation_trends(symbol)
    average_score = -1
        
    if recommendation_trends:
        most_recent_trend = recommendation_trends[0] 
        # print(most_recent_trend)
        
        weights = {
            'strongBuy': 5,
            'buy': 4,
            'hold': 3,
            'sell': 2,
            'strongSell': 1
        }
        
        counts = {
            'strongBuy': most_recent_trend.get('strongBuy', 0),
            'buy': most_recent_trend.get('buy', 0),
            'hold': most_recent_trend.get('hold', 0),
            'sell': most_recent_trend.get('sell', 0),
            'strongSell': most_recent_trend.get('strongSell', 0)
        }
        
        weighted_sum = (
            counts['strongBuy'] * weights['strongBuy'] +
            counts['buy'] * weights['buy'] +
            counts['hold'] * weights['hold'] +
            counts['sell'] * weights['sell'] +
            counts['strongSell'] * weights['strongSell']
        )
        total_count = (
            counts['strongBuy'] +
            counts['buy'] +
            counts['hold'] +
            counts['sell'] +
            counts['strongSell']
        )

        average_score = weighted_sum / total_count if total_count > 0 else 0
        
        if average_score - int(average_score) < 0.5:
            average_score =  int(average_score)
        else:
            average_score =  int(average_score) + 1       
    
    return average_score