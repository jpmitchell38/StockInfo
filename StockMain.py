import sys
import tkinter as tk
from tkinter import messagebox

from StockInputs import *
from StockConnectAPI import *
from StockOutputs import *

# Send back which ticker was incorrect if it fails - Done
# Put dollar sign on price on the graphs
# Let them enter the input until they enter a correct input
# Bottom left Graph can be changed, maybe to percent change, can bin it depending on how long it is (could divide the time by 6)
# In the plot titles, put the stock in the titles


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