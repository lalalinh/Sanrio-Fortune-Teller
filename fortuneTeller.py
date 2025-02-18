from tkinter import *
from PIL import Image, ImageTk
import random

bagel = Tk()
bagel.title("Tarot Reading")
bagel.geometry("620x470+50+90")

cream = Canvas(bagel, width=620, height=470)
cream.config(bg="white")
cream.place(x=0, y=0)

# Variables of GIF
file = "fortuneTeller/twins.gif" 
info = Image.open(file)

frames = info.n_frames  
image_objects = []
for i in range(frames):
    obj = PhotoImage(file=file, format=f"gif -index {i}")
    image_objects.append(obj)

# List of fortune labels
bag = ["Today is a great day for you.", 
       "Bloom where you are planted.", 
       "Live this day as if\nit were your last.", 
       "Do it scared.", 
       "Don't dream for your success,\nwork for it.", 
       "It is never too late to be\nwhat you might have been."]

def powder():
    # Covering the prior fortune labels
    cover1 = Label(cream, text='', bg='white', fg='white')
    cover1.place(relx=0.5, y=300, anchor=CENTER, width=620, height=310)
    
    # Heading label
    water = Label(cream, text="The Fortune Teller is telling you that-", 
          font=("Arial", 17, "normal"), bg='light blue', fg='gray')
    water.place(x=250, y=205, anchor=CENTER)
    
    # Randomizes fortune text
    fortune = random.choice(bag)
    eat = Label(cream, text=str(fortune), font=("Times", 22, "italic"), bg='white', fg='pink')
    eat.place(relx=0.5, y=275, anchor=CENTER)

# CONTRIBUTION: Line 45-65 (excluding some modified parts accordingly to the program)
# -- Ritik Raj, Aug 13, 2023 on DevHub
def egg():
    # Covering the gif from prior clicks
    cover2 = Label(cream, text='', bg='white', fg='white')
    cover2.place(relx=0.5, y=290, anchor=CENTER, width=620, height=310)

    def animation(current_frame=0):
     global loop
     image = image_objects[current_frame]
     
     global gif
     gif = Label(cream, image=image)
     gif.place(relx=0.5, y=300, anchor=CENTER)
     gif.config(image=image, width=280, height=300)
     
     current_frame = current_frame + 1
     loop = bagel.after(70, lambda:animation(current_frame))
     
     # When gif reaches the final frame, cancels it and creates new fortune labels
     if current_frame == frames:
        bagel.after_cancel(loop)
        powder()
    
    animation(current_frame=0)
    
# Variables of image
open = Image.open("fortuneTeller/01.png" )
resize = open.resize((500, 350))
img = ImageTk.PhotoImage(resize)
update = cream.create_image(310, 80, image=img, anchor=CENTER)
cover3 = Label(cream, text='', bg='white', fg='white')
cover3.place(relx=0.5, y=210, anchor=CENTER, width=620, height=150)

# Title label 
title = Label(cream, text="Click to get a sign from the universe!", font=("Arial", 20))
title.place(relx=0.5, y=40, anchor=CENTER)

# Click label: Fortune Teller activating label    
cheese = Button(cream, text="Click", font=("Arial", 18), bg='pink', 
                activebackground="light blue", command=lambda:egg())
cheese.place(relx=0.5, y=100, anchor=CENTER, width=75, height=40)

bagel.mainloop()
