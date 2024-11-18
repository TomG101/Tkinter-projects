import tkinter
import random
screen = tkinter.Tk()
screen.geometry("800x600")

def play_game(user_selection):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    label7.config(text = "Computer selected:" + computer_choice )
    label5.config(text = "Player selected:" + user_selection)


label = tkinter.Label(screen,text = "Rock Paper Scissors",font = ("Arial",40))
label2 = tkinter.Label(screen,text = "1",font = ("Arial",20))
label3 = tkinter.Label(screen,text = "Your Options:",font = ("Arial",20))
label4 = tkinter.Label(screen,text = "Score:",font = ("Arial",20))
label5 = tkinter.Label(screen,text = "Player Selected:",font = ("Arial",20))
label6 = tkinter.Label(screen,text = "Player Score:",font = ("Arial",20))
label7 = tkinter.Label(screen,text = "Computer Selected:",font = ("Arial",20))
label8 = tkinter.Label(screen,text = "Computer Score:",font = ("Arial",20))
button = tkinter.Button(screen,text = "Rock")
button2 = tkinter.Button(screen,text = "Paper")
button3 = tkinter.Button(screen,text = "Scissors")
label.place(x = 200, y = 50)
label2.place(x = 275, y = 100)
label3.place(x = 75, y = 200)
label4.place(x = 100, y = 300)
label5.place(x = 200, y = 350)
label6.place(x = 425, y = 350)
label7.place(x = 200, y = 400)
label8.place(x = 425, y = 400)
button.place(x = 200, y = 250)
button2.place(x = 300, y = 250)
button3.place(x = 400, y = 250)

screen.mainloop()
