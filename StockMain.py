import sys
import tkinter as tk
from tkinter import messagebox

from StockInputs import *
from StockConnectAPI import *
from StockOutputs import *


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