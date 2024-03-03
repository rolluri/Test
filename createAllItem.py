from tkinter import *
from tkinter import ttk
import json

with open("colorItem.json", "r") as colors:
    colorMap = json.load(colors)
    
def crateFrame():
    frameOne = Frame(width=450,height=250)
    frameOne.place(x = 0,y = 0)
    frameOne['bg'] = colorMap["Yellow"]

    frameTwo = Frame(width=450,height=250)
    frameTwo.place(x = 450,y = 0)
    frameTwo['bg'] = colorMap["Green"]

    frameThree = Frame(width=450,height=250)
    frameThree.place(x = 0,y = 250)
    frameThree['bg'] = colorMap["Blue"]

    frameFour = Frame(width=450,height=250)
    frameFour.place(x = 450,y = 250)
    frameFour['bg'] = colorMap["Pink"]
