# Importing Libraries
from tkinter import *
from tkinter import messagebox
import time,sys
from pygame import mixer
from PIL import Image, ImageTk

# Creating functions for the code

def alarm():
    alarm_time = user_input.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error Message","Please enter some value")
    else:
        while True:
            time.sleep(1)
            if (alarm_time==time.strftime("%H:%M")):
                playmusic()

def playmusic():
    mixer.init()
    mixer.music.load("tone.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(27)
        mixer.music.stop()
        sys.exit()

# Defining window size and setup background Image

root = Tk()
root.title("Alarm Clock")
root.geometry("600x380")
canvas = Canvas(root,width=600,height=380)
img = ImageTk.PhotoImage(Image.open("Img2.png"))
canvas.create_image(0,0,anchor=NW,image=img)
canvas.pack()
header = Frame(root)

# creating data entry field

box1 = Frame(root)
box1.place(x=250,y=180)
box2 = Frame(root)
box2.place(x=222,y=260)

# Taking input from the user

user_input = Entry(box1,font=('comic sans',20),width=6)
user_input.grid(row=1,column=2)
start_button = Button(box2,text="Set Alarm",font=('comic sans',20,'bold'),command=alarm)
start_button.grid(row=2,column=2)

root.mainloop()
