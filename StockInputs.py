from tkinter import simpledialog
from tkinter import messagebox


def getTickers():
    """
    Asks the user for up to 8 stock tickers, seperated by a comma
 
    Args:
 
    Returns:
        list: List of all the tickers inputed
    """
    ticker = simpledialog.askstring(title="Question",
                                    prompt="Enter the ticker symbols, seperated by a comma")
    if ticker != "" and type(ticker) != type(None):
        ticker = ticker.upper()
        ticker = ticker.replace(" ", "")
        tickerL = ticker.split(",")
    else:
        if ticker == "":
            messagebox.showerror("Error", "Invalid ticker or format;\n Can not leave empty")
            exit(1)
        messagebox.showerror("Error", "Invalid ticker or format")
        exit(1)
    return tickerL

def getDays(stringToAsk):
    """
    Asks the user for a number based on the dialog given
 
    Args:
        stringToAsk (string): The dialog to ask the user
 
    Returns:
        int: the number that was inputed
    """
    days = simpledialog.askstring(title="Question",
                                    prompt=stringToAsk)
    try:
        int(days)
    except:
        messagebox.showerror("Error", "Invalid integer; Example format: 4")
        exit(1)
    return days