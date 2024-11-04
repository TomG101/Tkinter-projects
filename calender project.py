import tkinter
import calendar
screen = tkinter.Tk()
screen.geometry("800x800")
screen.title("Calendar")

def show_calendar():
    screen2 = tkinter.Tk()
    screen2.geometry("800x800")
    screen2.title("Calendar")
    year = int(entry1.get())
    calendar_text = calendar.calendar(year)
    text = tkinter.Text(screen2)
    text.insert(tkinter.END,calendar_text)
    text.pack()
    screen2.mainloop()

label = tkinter.Label(screen,text = "Calendar",font= ("Arial", 50, "bold"),bg = "red",fg = "white")
label2 = tkinter.Label(screen,text = "Enter Year",bg = "green")
entry1 = tkinter.Entry(screen) 
button = tkinter.Button(screen,text = "Show Calendar",bg = "red",command = show_calendar)
button2 = tkinter.Button(screen,text = "Exit",bg = "red")
label.pack()
label2.pack()
entry1.pack()
button.pack()
button2.pack()
screen.mainloop()