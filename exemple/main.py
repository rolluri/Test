from tkinter import *
from tkinter import ttk
import json
import createAllItem

root = Tk()
root.geometry("900x500")


with open("colorItem.json", "r") as colors:
    colorMap = json.load(colors)

root.configure(bg = colorMap["White"])
startFrame = createAllItem.crateFrame()


root.mainloop()