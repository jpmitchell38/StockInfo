from tkinter import messagebox
import tkinter as tk

tickerL = []
days = 0

def runWindow():
    global tickerL
    global days
    def callNext():
        global tickerL
        global days

        input = inputtxt1.get(1.0, "end-1c") 

        if input != "" and type(input) != type(None):
            input = input.upper()
            input = input.replace(" ", "")
            tickerL = input.split(",")
        else:
            if input == "":
                messagebox.showerror("Error", "Invalid ticker or format;\n Can not leave empty")
                exit(1)
            messagebox.showerror("Error", "Invalid ticker or format")
            exit(1)

        input = inputtxt2.get(1.0, "end-1c") 
        try:
            int(input)   
        except:
            messagebox.showerror("Error", "Invalid integer; Example format: 60")
            exit(1)
        days = input
        frame.destroy() 


    frame = tk.Tk()
    frame.title("My window")
    frame.geometry('300x200') 

    text_var = tk.StringVar()
    text_var.set("Enter the ticker symbols, seperated by a comma")
    label = tk.Label(frame, textvariable=text_var, height=1, width=40, font=("Times New Roman", 12))
    label.pack(pady=(10,0)) 

    inputtxt1 = tk.Text(frame, 
                   height = 1, 
                   width = 30) 
    
    inputtxt1.pack()

    text_var = tk.StringVar()
    text_var.set("How many days back do you want data to go?")
    label = tk.Label(frame, textvariable=text_var, height=1, width=40, font=("Times New Roman", 12))
    label.pack(pady=(10,0)) 

    inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
    inputtxt2.pack()


    
    printButton = tk.Button(frame, 
                        text = "See Graphs",  
                        command = callNext,
                        padx=10,
                        pady=5,
                        width=15,
                        font=("Arial", 12)) 
    printButton.pack(pady=16) 

    frame.resizable(False, False)
    frame.eval('tk::PlaceWindow . center')
    frame.mainloop() 


    return tickerL, days
