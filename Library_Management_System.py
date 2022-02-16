from email.headerregistry import Address
from email.mime import application
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
from turtle import left, right
from matplotlib.pyplot import text

from numpy import pad
from pandas import DataFrame


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        MType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        Postcode = StringVar()
        MobileNo = StringVar()
        BookID = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        Prescription = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iReset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            Postcode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.textDisplayR1.delete("1.0", END)
            self.textDisplayR.delete("1.0", END)

        def iDelete():
            iReset()
            self.textDisplayR.delete("1.0", END)

        def iDisplayData():
            self.textDisplayR1.insert(END, 'Member Type: \t\t' + MType.get() + "\n")
            self.textDisplayR1.insert(END, 'Ref No: \t\t' + Ref.get() + "\n")
            self.textDisplayR1.insert(END, 'Title: \t\t' + Title.get() + "\n")
            self.textDisplayR1.insert(END, 'Firstname: \t\t' + Firstname.get() + "\n")
            self.textDisplayR1.insert(END, 'Surname: \t\t' + Surname.get() + "\n")
            self.textDisplayR1.insert(END, 'Address 1: \t\t' + Address1.get() + "\n")
            self.textDisplayR1.insert(END, 'Address 2: \t\t' + Address2.get() + "\n")
            self.textDisplayR1.insert(END, 'Post code: \t\t' + Postcode.get() + "\n")
            self.textDisplayR1.insert(END, 'Mobile no: \t\t' + MobileNo.get() + "\n")
            self.textDisplayR1.insert(END, 'Book ID: \t\t' + BookID.get() + "\n")
            self.textDisplayR1.insert(END, 'Book Title: \t\t' + BookTitle.get() + "\n")
            self.textDisplayR1.insert(END, 'Author: \t\t' + Author.get() + "\n")
            self.textDisplayR1.insert(END, 'Date Borrowed: \t\t' + DateBorrowed.get() + "\n")

            # self.textDisplayR1.insert(END,"\n",MType.get()+"\n"+Ref.get()+"\n"+Title.get()+"\n"+
            # Firstname.get()+"\n"+Surname.get()+"\n"+Address1.get()+"\n"+Address2.get()+"\n"+
            # Postcode.get()+"\n"+BookTitle.get()+"\n"+DateBorrowed.get()+"\n"+DaysOnLoan.get()+"\n")

        def iReciept():
            self.textDisplayR.insert(END, 'Member Type: \t\t' + MType.get() + "\n")
            self.textDisplayR.insert(END, 'Ref No: \t\t' + Ref.get() + "\n")
            self.textDisplayR.insert(END, 'Title: \t\t' + Title.get() + "\n")
            self.textDisplayR.insert(END, 'Firstname: \t\t' + Firstname.get() + "\n")
            self.textDisplayR.insert(END, 'Surname: \t\t' + Surname.get() + "\n")
            self.textDisplayR.insert(END, 'Address 1: \t\t' + Address1.get() + "\n")
            self.textDisplayR.insert(END, 'Address 2: \t\t' + Address2.get() + "\n")
            self.textDisplayR.insert(END, 'Post code: \t\t' + Postcode.get() + "\n")
            self.textDisplayR.insert(END, 'Mobile no: \t\t' + MobileNo.get() + "\n")
            self.textDisplayR.insert(END, 'Book ID: \t\t' + BookID.get() + "\n")
            self.textDisplayR.insert(END, 'Book Title: \t\t' + BookTitle.get() + "\n")
            self.textDisplayR.insert(END, 'Author: \t\t' + Author.get() + "\n")
            self.textDisplayR.insert(END, 'Date Borrowed: \t\t' + DateBorrowed.get() + "\n")

        # ________________________framework___________________________________________
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP, expand="yes")
        self.lblTitle = Label(TitleFrame, width=47, font=('arial', 40, 'bold'), text="\t Library Management System\t",
                              padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM, fill="both", expand="yes")

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM, fill="both", expand="yes")

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(fill="both", expand="yes")

        DataFrameLEFT = Frame(DataFrame, bd=20, width=400, height=400, padx=20, relief=RIDGE)
        DataFrameLEFT.pack(fill="both", expand="yes", side=LEFT)
        self.DataFrameLabelLEFT = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="\t")
        self.DataFrameLabelLEFT.grid()

        DataFrameRIGHT = Frame(DataFrame, bd=20, width=400, height=400, padx=20, relief=RIDGE)
        DataFrameRIGHT.pack(fill="both", expand="yes", side=LEFT)
        self.DataFrameLabelRIGHT = Label(DataFrameRIGHT, font=('arial', 12, 'bold'), text="\t book list")
        self.DataFrameLabelRIGHT.grid()

        # _________________________________widget_________________________________________________
        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state='readonly',
                                          textvariable=MType, width=23)
        self.cboMemberType['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Book ID", padx=2, pady=2)
        self.lblBookID.grid(row=1, column=0, sticky=W)
        self.lblBookID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=BookID)
        self.lblBookID.grid(row=1, column=1)

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference no:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Ref)
        self.txtRef.grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=BookTitle)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state='readonly', width=23,
                                     textvariable=Title)
        self.cboTitle['value'] = ('', 'Mr', ',Miss', 'Mrs', 'Dr', 'Capt', 'Ms')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Author)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="First name:", padx=2, pady=2)
        self.lblFirstName.grid(row=3, column=0, sticky=W)
        self.txtFirstName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Firstname)
        self.txtFirstName.grid(row=3, column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=DateBorrowed)
        self.txtDateBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Surname:", padx=2, pady=2)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Surname)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=DateDue)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Address1)
        self.txtAddress1.grid(row=5, column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Days on loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=DaysOnLoan)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAddress2 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Address2)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Late Return Fine:", padx=2,
                                       pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=LateReturnFine)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Post code:", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        self.txtPostCode = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=Postcode)
        self.txtPostCode.grid(row=7, column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date overdue:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        self.txtDateOverDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=DateOverDue)
        self.txtDateOverDue.grid(row=7, column=3)

        self.lblMobileno = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="mobie no:", padx=2, pady=2)
        self.lblMobileno.grid(row=8, column=0, sticky=W)
        self.txtMobileno = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=MobileNo)
        self.txtMobileno.grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25, textvariable=SellingPrice)
        self.txtSellingPrice.grid(row=8, column=3)

        # ____________________________________________WIDGET__________________________________________
        self.textDisplayR = Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=32, height=13, padx=8, pady=20)
        self.textDisplayR.grid(row=0, column=2)
        # ____________________________________________LISTBOX__________________________________________
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky="ns")
        # scrollbar.pack(side= RIGHT, fill= Y)

        ListofBooks = ["In Search of Lost Time", "Ulysses", "Don Quixote", "The Great Gatsby", "Moby Dick", "War and Peace", "Hamlet", "Crime and Punishment", "The Grapes of Wrath","Invisible Man", "To Kill a Mockingbird", "The Trial", "Middlemarch", "Gulliver's Travels", "The Stranger", "Harry Potter"]

        def SelectedBook(evt):
            value = str(booklist.get(booklist.curselection()))
            w = value

            if (w == "In Search of Lost Time"):
                BookID.set("ISBN 75486321")
                BookTitle.set("In Search of Lost Time")
                Author.set("Marcel Proust")
                LateReturnFine.set("5.56")
                SellingPrice.set("789")
                DaysOnLoan.set(14)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Ulysses"):
                BookID.set("ISBN 697854")
                BookTitle.set("Ulysses")
                Author.set("James Joyce")
                LateReturnFine.set("3.97")
                SellingPrice.set("680")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Don Quixote"):
                BookID.set("ISBN 567894")
                BookTitle.set("Don Quixote")
                Author.set("Miguel de Cervantes")
                LateReturnFine.set("3.78")
                SellingPrice.set("566")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "The Great Gatsby"):
                BookID.set("ISBN 458621")
                BookTitle.set("The Great Gatsby")
                Author.set("F. Scott Fitzgerald")
                LateReturnFine.set("2.56")
                SellingPrice.set("480")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Moby Dick"):
                BookID.set("ISBN 754621")
                BookTitle.set("Moby Dick")
                LateReturnFine.set("3.25")
                SellingPrice.set("652")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "War and Peace"):
                BookID.set("ISBN 785421")
                BookTitle.set("War and Peace")
                Author.set("Leo Tolstoy")
                LateReturnFine.set("4.50")
                SellingPrice.set("890")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Hamlet"):
                BookID.set("ISBN 564213")
                BookTitle.set("Hamlet")
                Author.set("William Shakespeare")
                LateReturnFine.set("4.15")
                SellingPrice.set("690")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Crime and Punishment"):
                BookID.set("ISBN 985432")
                BookTitle.set("Crime and Punishment")
                Author.set("Fyodor Dostoyevsky")
                LateReturnFine.set("5.50")
                SellingPrice.set("780")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "The Grapes of Wrath"):
                BookID.set("ISBN 654213")
                BookTitle.set("The Grapes of Wrath")
                Author.set("John Steinbeck")
                LateReturnFine.set("3.32")
                SellingPrice.set("560")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Invisible Man"):
                BookID.set("ISBN 854621")
                BookTitle.set("Invisible Man")
                Author.set("Ralph Ellison")
                LateReturnFine.set("6.50")
                SellingPrice.set("750")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "To Kill a Mockingbird"):
                BookID.set("ISBN 564213")
                BookTitle.set("To Kill a Mockingbird")
                Author.set("Harper Lee")
                LateReturnFine.set("4.56")
                SellingPrice.set("480")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "The Trial"):
                BookID.set("ISBN 754621")
                BookTitle.set("The Trial")
                Author.set("Franz Kafka")
                LateReturnFine.set("4.32")
                SellingPrice.set("640")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Middlemarch"):
                BookID.set("ISBN 785462")
                BookTitle.set("Middlemarch")
                Author.set("George Eliot")
                LateReturnFine.set("1.25")
                SellingPrice.set("450")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Gulliver's Travels"):
                BookID.set("ISBN 785462")
                BookTitle.set("Gulliver's Travels")
                Author.set("Jonathan Swift")
                LateReturnFine.set("2.25")
                SellingPrice.set("350")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "The Stranger"):
                BookID.set("ISBN 756420")
                BookTitle.set("The Stranger")
                Author.set("Albert Camus")
                LateReturnFine.set("3.25")
                SellingPrice.set("290")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Harry Potter"):
                BookID.set("ISBN 696900")
                BookTitle.set("Harry Potter")
                Author.set("J.K. Rowling")
                LateReturnFine.set("6.9")
                SellingPrice.set("690")
                DaysOnLoan.set(7)
                iReciept()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

        booklist = Listbox(DataFrameRIGHT, width=20, height=12, font=('arial', 12, 'bold'))

        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        # # booklist.pack(side = LEFT)
        for items in ListofBooks:
            booklist.insert(END, items)

        # ____________________________________________________________________________________________

        self.lblLabel = Label(FrameDetail, font=('arial', 12, 'bold'), pady=8,
                              text=" Member type\t Refernce No.\t Title\t FirstName\t Surname\t Address 1\t Address 2\t Post Code\t Book Title\t Date Borrowed\t Days on Loan")
        self.lblLabel.grid(row=0, column=0)

        self.textDisplayR1 = Text(FrameDetail, font=('arial', 12, 'bold'), width=160, height=11, padx=2, pady=4)
        self.textDisplayR1.grid(row=1, column=0)

        # _____________________________________________BUTTON_________________________________________

        self.btnDisplayData = Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'), width=30, bd=4,
                                     command=iDisplayData)
        self.btnDisplayData.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=30, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=30, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=30, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=3)


if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()