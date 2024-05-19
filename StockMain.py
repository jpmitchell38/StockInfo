import sys

from StockInputs import *
from StockConnectAPI import *
from StockOutputs import *

# Find out where if you input a wrong ticker it outputs something
# Let them enter the input until they enter a correct input
# Bottom left Graph can be changed, maybe to percent change, can bin it depending on how long it is (could divide the time by 6)
# In the plot titles, put the stock in the titles


def main():
    listOfTickers, days = runWindow()
    tryConnectYahoo()

    print(outputConsole(listOfTickers, days))
    sys.stdout.flush()
    graph(listOfTickers, days)
          
main()