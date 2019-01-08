import os;
import sys;
import tkinter
from tkinter import *;

class ConvertSettingApp:
    def __init__(self):
        subRoot = Tk();
        status_bar_frame = Frame(subRoot)
        status_bar_frame.grid(row=3, column=0, columnspan=2)

        subRoot.mainloop();