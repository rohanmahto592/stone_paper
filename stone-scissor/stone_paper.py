from tkinter import *
import random
window=Tk()
window.geometry("1100x700")
window.title("Rock Paper Scissor")
window.configure(background="orange")
window.resizable(0,0)

label_1=Label(window,text="Rock Paper Scissors",bg="orange",fg="green")
label_1.pack()
label_1.configure(font=("Zapfino",40))
label_2=Label(window,text="Lets Start the game!!",fg="gray",bg="orange",font="Zapfino")
label_2.pack(padx=15)
label_2.configure(font=("Zapfino",22))
main_frame=Frame(window,background='#FFB5C2')
main_frame.configure(background="orange")
main_frame.pack(fill=BOTH)
label_3=Label(main_frame,text="Your Options:",bg="orange",fg="red",font="Zapfino")
label_3.grid(row=0,column=0,padx=100,pady=20)

##button
scissor_icon=PhotoImage(file="icon2/scizors.png")
scissor_button=Button(main_frame,text="scissor",image=scissor_icon,font='vardana 12 bold',fg='#003380',bg="black")
scissor_button.grid(row=2,column=1,padx=8,pady=5)
scissor_button.configure(background="orange")

rock_icon=PhotoImage(file="icon2/stone.png")
rock_button=Button(main_frame,image=rock_icon,bg="black")
rock_button.grid(row=2,column=2,padx=20,pady=12)

paper_icon=PhotoImage(file="icon2/image.png")
paper_button=Button(main_frame,image=paper_icon,bg="black")
paper_button.grid(row=2,column=3,padx=30,pady=12)
label_4=Label(main_frame,text="Scores:",bg="orange",fg="brown",font="Zapfino")
label_4.grid(row=3,column=0,padx=100,pady=20)

label_5=Label(main_frame,text="Your Selected:",bg="orange",fg="green",font="Zapfino")
label_5.grid(row=4,column=1,pady=5)
label_6=Label(main_frame,text="Computer Selected:",bg="orange",fg="green",font="Zapfino")
label_6.grid(row=5,column=1,pady=5)
label_7=Label(main_frame,text="Your Score:",bg="orange",fg="blue",font="Zapfino")
label_7.grid(row=4,column=3,pady=5)
label_8=Label(main_frame,text="Computer Score:",bg="orange",fg="blue",font="Zapfino")
label_8.grid(row=5,column=3,pady=5)
user_won=0
comp_won=0
table=["rock","scissor","paper"]
def scoreboard(userchoice,compchoice):
    label_5.config(text=f'Your Selected:{userchoice}')
    label_6.config(text=f'Computer Selected:{compchoice}')
    if (userchoice=='rock' and compchoice=="scissor") or (userchoice=="scissor" and compchoice=="paper") or (userchoice=="paper" and compchoice=="rock"):
        label_2.config(text='User Win')
        global user_won
        user_won+=1
        label_7.config(text=f'Your Score:{user_won}')

    elif(compchoice=="rock" and userchoice=="scissor") or (compchoice=="scissor" and userchoice=="paper") or (compchoice=="paper" and userchoice=="rock"):
        label_2.config(text="Computer Win")
        global comp_won
        comp_won+=1
        label_8.configure(text=f'Computer Score:{comp_won}')
    else:
        label_2.config(text="Tie")


def rock(event=None):
    choice=random.choice(table)
    scoreboard("rock",choice)
def paper(event=None):
    choice=random.choice(table)
    scoreboard("paper",choice)
def scissor(event=None):
    choice=random.choice(table)
    scoreboard("scissor",choice)
scissor_button.configure(command=scissor)
rock_button.configure(command=rock)
paper_button.configure(command=paper)

window.mainloop()


























window.mainloop()