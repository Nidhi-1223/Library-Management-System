from email.mime import application
from tkinter import * 
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
from turtle import left
from matplotlib.pyplot import text

from numpy import pad
from pandas import DataFrame

class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "powder blue")


    #________________________framework___________________________________________
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, padx= 20, bd= 20, relief= RIDGE)
        TitleFrame.pack(side=TOP, expand="yes")
        self.lblTitle = Label(TitleFrame, width= 47, font=('arial', 40, 'bold'), text="\t Library Management System\t", padx = 12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width= 1350, height= 50, padx= 20, relief=RIDGE)
        ButtonFrame.pack(side= BOTTOM, fill="both", expand="yes")

        FrameDetail = Frame(MainFrame, bd=20, width= 1350, height= 100, padx= 20, relief=RIDGE)
        FrameDetail.pack(side= BOTTOM, fill="both", expand="yes")

        # DataFrame = Frame(MainFrame, bd= 20, width= 1350, height= 400, padx= 20, relief= RIDGE)
        # DataFrame.pack(side = BOTTOM)
        # # self.DataFrame = Label(DataFrame, font=('arial', 12, 'bold'), text="\t Library Management System\t", padx = 12)
        # # self.DataFrame.grid()

        # DataFrameLEFT = Frame(DataFrame, bd= 10, width= 800, height= 300, padx= 20, relief= RIDGE)
        # self.DataFrameLEFT = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="\t Library Management System\t", padx = 12, height= 10, width=30)
        # self.DataFrameLEFT.grid()
        # DataFrameLEFT.pack(side = LEFT)

        # DataFrameRIGHT = Frame(DataFrame, bd= 10, width= 800, height= 300, padx= 20, relief= RIDGE)
        # self.DataFrameRIGHT = Label(DataFrameRIGHT, font=('arial', 12, 'bold'), text="\t Library Management System\t", padx = 12, height= 10, width=30)
        # self.DataFrameLEFT.grid()
        # DataFrameRIGHT.pack(side = RIGHT)
        # # DataFrameRIGHT = Frame(DataFrame, bd= 10, width= 450, height= 300, padx= 20, relief= RIDGE, font=('arial', 12, 'bold'), text = 'Book Details:')
        # # DataFrameRIGHT.pack(side = LEFT)



        DataFrame = Frame(MainFrame, bd= 20, width= 1350, height= 400, padx= 20, relief= RIDGE)
        DataFrame.pack(fill="both", expand="yes")
        self.DataFrameLabel = Label(DataFrame, width= 47, font=('arial',40 , 'bold'), text="\t fkjflsajflksifasoifbisafuias\t",)



if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()