import sys

from StockInputs import *
from StockConnectAPI import *
from StockOutputs import *

# Let them enter the input until they enter a correct input - done ish, but if ticker is incorrect it cloes
# Refacter stockinput
# Bottom left Graph can be changed, maybe to percent change, can bin it depending on how long it is (could divide the time by 6)
# In the plot titles, put the stock in the titles


def main():
    tryConnectYahoo()
    
    listOfTickers, days = runWindow()
    
    consoleOutput = graph(listOfTickers, days)
    print(consoleOutput)
    
    # sys.stdout.flush()
          
main()