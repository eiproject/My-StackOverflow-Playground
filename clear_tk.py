import tkinter as tk
from tkinter.constants import BOTTOM
from typing import Text

root=tk.Tk()

root.resizable(False, False)

root.title('Pounds to Kilograms')

canvas=tk.Canvas(root, height=150, width=200, bg='teal')

frame=tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

entry1=tk.Entry(root)
canvas.create_window(200, 200, window=entry1)
entry1.place(x=40, y=50)

labelanswer=tk.Label(root, bg='teal')
labelanswer.place(x=45,y=45)

def to_kg():
    kg=float(entry1.get())/2.205
    labelanswer['text'] = kg

labeltext=tk.Label(root, text='lbs to kg', bg='white')

button1=tk.Button(root, text="convert", command=to_kg)

button1.pack(side=BOTTOM)
canvas.pack()
labelanswer.pack()
frame.pack()

root.mainloop()