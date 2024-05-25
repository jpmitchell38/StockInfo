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
        
        count = 0
        String = ""
        try:
            input1 = inputtxt1.get(1.0, "end-1c") 
            
            if input1 == "":
                String += "Ticker input cannot be empty\n"
                count += 1
            else:
                input1 = input1.upper()
                input1 = input1.replace(" ", "")
                tickerL = input1.split(",")
                
                passed = 0
                for tick in tickerL:
                    if tick == "" and passed == 0:
                        String += "Invalid ticker format\n"
                        count += 1
                        passed += 1
            
            
 
            try:
                input2 = inputtxt2.get(1.0, "end-1c")
                int(input2)   
            except:
                if input2 == "":
                    if input1 == "":
                        String = "Inputs cannot be empty"
                    else:
                        String += "How many days input cannot be empty\n"
                    count += 1
                else:
                    String += "Invalid integer\n"
                    count += 1
            else:
                days = input2
        except:
            String += "this doesnt get called"
            count += 1
        else:
            if count == 0:
                frame.destroy() 
            else:
                messagebox.showerror("Error", String)
    
    def disable_event():
        pass

    def close_win():
        frame.destroy()
        exit(1)

    def key_pressed(event):
        callNext()


    frame = tk.Tk()
    frame.title("My window")
    frame.geometry('350x250') 
    frame.configure(background='light blue')

    text_var = tk.StringVar()
    text_var.set("Enter the ticker symbols, seperated by a comma")
    label = tk.Label(frame, textvariable=text_var, height=1, width=40, font=("Times New Roman", 11, 'bold'))
    label.config(bg="light blue")
    label.pack(pady=(10,0)) 

    inputtxt1 = tk.Text(frame, 
                   height = 1, 
                   width = 30) 
    
    inputtxt1.pack()

    text_var = tk.StringVar()
    text_var.set("How many days back do you want data to go?")
    label = tk.Label(frame, textvariable=text_var, height=1, width=40, font=("Times New Roman", 11, 'bold'))
    label.config(bg="light blue")
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
                        width=12,
                        cursor="hand2",
                        activebackground="dark grey", 
                        font=("Arial", 12, 'bold')) 
    printButton.pack(pady=20) 


    printButton = tk.Button(frame, 
                        text = "Exit",  
                        command = close_win,
                        padx=10,
                        pady=5,
                        width=12,
                        cursor="hand2",
                        activebackground="red3", 
                        font=("Arial", 12, 'bold'),
                        bg="red")
    printButton.pack() 

    frame.bind('<Return>',key_pressed)
    frame.protocol("WM_DELETE_WINDOW", disable_event)
    frame.resizable(False, False)
    frame.eval('tk::PlaceWindow . center')
    frame.mainloop() 


    return tickerL, days
