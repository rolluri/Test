from tkinter import *
from tkinter import ttk
import json
root = Tk()

with open('colorJson.json','r') as colors:
    colorMap = json.load(colors)

root.geometry("500x500")
print(colorMap)

#mainFrame = ttk.Frame(width=700,height=300,bg = colorMap)

root.mainloop()