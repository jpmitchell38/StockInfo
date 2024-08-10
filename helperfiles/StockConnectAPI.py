from datetime import date, timedelta
import yfinance as yf #pip install yfinance
import finnhub
from dotenv import load_dotenv
import os

from helperfiles.calculate import *

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
    roundByTwo = None
        
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
        roundByTwo = average_score
        roundByTwo = round(roundByTwo, 2) if total_count > 0 else 0
        
        if average_score - int(average_score) < 0.5:
            average_score =  int(average_score)
        else:
            average_score =  int(average_score) + 1       
    
    return average_score, roundByTwo

def get_metrics(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    
    if len(info) == 1:
        return None, None, None, None, None, False, None
    
    price = info.get('currentPrice', None)
    one = calculatePE(info)
    two = get_peg_ratio(info)
    three = get_dividend_yield(info)
    four = get_profit_margin(info)
    five = get_short_interest(info)
    
    six, seven = get_recommendation_trends(symbol)
    calculateNumber(one, two, four, five, seven, symbol)
    
    # calculate based of a percentage of points, every item gets either 0/1/2
    # or 1/2/3 points, take the total of possible and if its a certain percentage
    # (like 75% of the points or more its a buy)
    
    return one, two, three, four, five, True, price


#   Traditional Companies: 15-20
#   Growth Companies: 20-30 or higher
# great is 15-25, okay is 10 on either side, rest is bad
def calculatePE(info):
    pe_ratio = ""
    try:
        price = info.get('currentPrice', None)  # Use 'currentPrice' if available
        eps = info.get('trailingEps', None)  # Use 'trailingEps' for EPS

        if price is None or eps is None:
            return None
        else:
            pe_ratio = price / eps
            return pe_ratio
    except:
        return None


# PEG Ratio < 1: A PEG ratio below 1 is often considered a sign that the stock might be 
# undervalued relative to its growth prospects. This means the stock's price is low relative to its earnings growth rate.

# Implications: Negative growth suggests that the company is facing financial difficulties, 
# declining revenues, or other issues that are causing its earnings to fall.

# 0-1 is great, 1-4 is okay, anything else is bad
def get_peg_ratio(info):
    try:
        pe_ratio = info.get('trailingPE')
        earnings_growth_rate = info.get('earningsGrowth')
        
        if pe_ratio is not None and earnings_growth_rate is not None:
            
            earnings_growth_rate *= 100
            peg_ratio = pe_ratio / earnings_growth_rate
            
            return peg_ratio
        else:
            return None
    
    except Exception as e:
        return None


# Dividend Yield > 3-4%: A dividend yield of 3% or higher is generally considered attractive, 
# especially for income-focused investors. However, a very high yield (e.g., 7%+) 
# may indicate potential risk or a declining stock price.
def get_dividend_yield(info):
    try:       
        # Get annual dividends per share and current price
        dividend_rate = info.get('dividendRate')  # Annual dividend per share
        price = info.get('currentPrice')  # Current price per share
        
        if dividend_rate and price:
            dividend_yield = (dividend_rate / price) * 100
            
            return dividend_yield
        else:
            return None
    except:
        return None

    
# How to Use: Compare with industry averages. Higher margins suggest better cost control and pricing power.
# 21%+ is great, 10-20% is good, below 10% is bad
def get_profit_margin(info):
    try:
        # Get net income and total revenue
        net_income = info.get('netIncomeToCommon')
        total_revenue = info.get('totalRevenue')
        
        if net_income and total_revenue:
            profit_margin = (net_income / total_revenue) * 100
            return profit_margin
        else:
            return None
    except:
        return None
    
# How to Use: High short interest might signal negative sentiment or potential for a short squeeze.
# below 5% is low risk, 5-15 is moderate, 15+ is high
def get_short_interest(info):
    try:
        # Get shares short and average daily volume
        shares_short = info.get('sharesShort')
        average_daily_volume = info.get('averageVolume')
        
        if shares_short and average_daily_volume:
            short_interest_ratio = shares_short / average_daily_volume
            return short_interest_ratio
        else:
            return None
    except:
        return None