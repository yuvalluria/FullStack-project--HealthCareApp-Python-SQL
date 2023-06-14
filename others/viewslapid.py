import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import sys


class Frame1(ttk.Frame):
    def __init__(self, app):
        ttk.Frame.__init__(self, master=app, relief=tk.RAISED, borderwidth=2, width=150, height=7)
        self.__create_widgets(app)
        return

    def __create_widgets(self, app):
        self.columnconfigure([1, 2, 3, 4, 5, 6], weight=1, minsize=10)
        self.rowconfigure([1, 2], weight=1, minsize=20)

        # Patient ID label
        self.labelPatientID = tk.Label(self,
                                       text="Patient ID",
                                       fg="black",  # Set the text color to white
                                       bg="grey",  # Set the background color to black
                                       width=12,
                                       height=1)
        self.labelPatientID.grid(column=1, row=1, padx=0, pady=1)
        # self.labelPatientID.pack(side=tk.LEFT)
        # Patient ID Entry
        self.PatientIDEntry = tk.Entry(self, width=22)
        self.PatientIDEntry.insert(0, "patient id")
        self.PatientIDEntry.grid(column=2, row=1, padx=0, pady=1)
        self.PatientIDEntry.bind("<Button-1>", lambda e: self.PatientIDEntry.delete(0, "end"))
        self.PatientIDEntry.bind("<Leave>", lambda e: app.inputs.set_val(self.PatientIDEntry, "PatientID"))

        # Patient first name label
        self.labelPatientFirstName = tk.Label(self,
                                              text="Patient's First Name",
                                              fg="black",  # Set the text color to white
                                              bg="grey",  # Set the background color to black
                                              width=20,
                                              height=1)
        self.labelPatientFirstName.grid(column=3, row=1, padx=1, pady=1)
        # self.labelPatientFirstName.pack(side=tk.LEFT)
        # Patient first name entry
        self.PatientFirstNameEntry = tk.Entry(self, width=20)
        self.PatientFirstNameEntry.insert(0, "patient's first name")
        self.PatientFirstNameEntry.grid(column=4, row=1, padx=2, pady=1)
        # self.PatientFirstNameEntry.pack(side=tk.LEFT)
        self.PatientFirstNameEntry.bind("<Button-1>", lambda e: self.PatientFirstNameEntry.delete(0, "end"))
        self.PatientFirstNameEntry.bind("<Leave>",
                                        lambda e: app.inputs.set_val(self.PatientFirstNameEntry, "PatientFirstName"))

        # Patient last name label
        self.labelPatientLastName = tk.Label(self,
                                             text="Patient's Last Name",
                                             fg="black",  # Set the text color to white
                                             bg="grey",  # Set the background color to black
                                             width=20,
                                             height=1)
        self.labelPatientLastName.grid(column=5, row=1, padx=1, pady=1)
        # self.labelPatientLastName.pack(side=tk.LEFT)
        # Patient last name entry
        self.PatientLastNameEntry = tk.Entry(self, width=20)
        self.PatientLastNameEntry.insert(0, "patient's last name")
        self.PatientLastNameEntry.grid(column=6, row=1, padx=0, pady=1)
        # self.PatientLastNameEntry.pack(side=tk.LEFT)
        self.PatientLastNameEntry.bind("<Button-1>", lambda e: self.PatientLastNameEntry.delete(0, "end"))
        self.PatientLastNameEntry.bind("<KeyRelease>",
                                       lambda e: app.inputs.set_val(self.PatientLastNameEntry, "PatientLastName"))
        self.errorMassage = tk.Label(self, text="", fg="red", width=50, height=2)
        self.errorMassage.grid(column=2, row=2, columnspan=5, padx=0, pady=0)
        # self.errorMassage.pack(side = tk.BOTTOM)

        return True

    def ID_error(self):
        self.errorMassage = tk.Label(self, text="ID error - numbers only please",
                                     fg="red", width=50, height=2)
        self.errorMassage.grid(column=1, row=2, columnspan=3, padx=5, pady=1)
        self.after(2000, self.errorMassage.destroy)
        return

    def clear_ID_error(self):
        self.errorMassage.destroy()
        return


class Frame2(ttk.Frame):
    def __init__(self, app):
        super().__init__(master=app, relief=tk.RAISED, borderwidth=5, width=200, height=10)
        self.__create_widgets(app)
        return

    def __create_widgets(self, app):
        self.labelDiagnosis = tk.Label(self,
                                       text="Enter Diagnosis",
                                       fg="black",  # Set the text color to white
                                       bg="grey",  # Set the background color to black
                                       width=13,
                                       height=1)
        self.labelDiagnosis.pack(side=tk.LEFT)

        self.diag = tk.Text(self, width=25, height=3)
        self.diag.pack(side=tk.LEFT)
        self.diag.bind("<Leave>", lambda e: app.inputs.set_val(self.diag, "Diagnosis"))

        self.rb_yes_var = tk.IntVar()
        self.rb_yes_var.set(0)
        self.rb_yes = tk.Radiobutton(self, text="Yes", variable=self.rb_yes_var, value=1,
                                     command=lambda: app.inputs.set_val(self.rb_yes_var, "DrugSensitivity"))
        self.rb_yes.pack(side=tk.LEFT)

        self.rb_no = tk.Radiobutton(self, text="No", variable=self.rb_yes_var, value=0,
                                    command=lambda: app.inputs.set_val(self.rb_yes_var, "DrugSensitivity"))
        self.rb_no.pack(side=tk.LEFT)

        self.labelCombo = tk.Label(master=self,
                                   text="Antigen",
                                   fg="black",  # Set the text color to white
                                   bg="grey",  # Set the background color to black
                                   width=8,
                                   height=1)
        self.labelCombo.pack(side=tk.LEFT)
        self.comboAnt = ttk.Combobox(self, values=["Ant1", "Ant2", "Ant3", "Ant4"])
        self.comboAnt.pack(side=tk.LEFT)
        self.comboAnt.bind("<<ComboboxSelected>>", lambda e: app.inputs.set_val(self.comboAnt, "Antigen"))
        return True


class Frame3(ttk.Frame):
    def __init__(self, app):
        ttk.Frame.__init__(self, master=app, relief=tk.RAISED, borderwidth=4, width=800, height=300)
        self.__create_widgets(app)
        return

    def __create_widgets(self, app):
        self.rowconfigure([8], weight=1, minsize=10)
        self.columnconfigure([6], weight=1, minsize=20)
        self.labelBeginDate = tk.Label(master=self,
                                       font=('Times New Roman', 14),
                                       text="begine date",
                                       fg="black",  # Set the text color to white
                                       bg="grey",  # Set the background color to black
                                       width=12,
                                       height=1)
        self.labelBeginDate.grid(column=2, row=1, padx=1, pady=1)
        self.labelEndDate = tk.Label(master=self,
                                     font=('Times New Roman', 14),
                                     text="end date",
                                     fg="black",  # Set the text color to white
                                     bg="grey",  # Set the background color to black
                                     width=12,
                                     height=1)
        self.labelEndDate.grid(column=3, row=1, padx=1, pady=1)
        self.beginDate = DateEntry(self, width=12, background='darkblue',
                                   foreground='white', borderwidth=1)
        self.beginDate.grid(column=2, row=2, padx=1, pady=1)
        self.beginDate.bind("<<CalendarSelected>>", lambda e: self.beginDate.get_date)
        self.endDate = DateEntry(self, width=12, background='darkblue',
                                 foreground='white', borderwidth=1)
        self.endDate.grid(column=3, row=2, padx=1, pady=1)
        self.endDate.bind("<<CalendarSelected>>", lambda e: self.endDate.get_date)

        style = ttk.Style(self)
        style.configure("TButton", font=('Times New Roman', 12))

        self.loadDataButton = ttk.Button(self, style="TButton",
                                         text="load admissions",
                                         command=lambda: self.showTable(app))
        self.loadDataButton.grid(column=4, row=1, padx=1, pady=1)

        self.resetFrameButton = ttk.Button(self, style="TButton",
                                           text="reset frame",
                                           command=lambda: self.deleteTable(app))
        self.resetFrameButton.grid(column=4, row=2, padx=1, pady=1)

    def showTable(self, app):
        app.queries.queryPatientDataByDate(str(self.beginDate.get_date()), str(self.endDate.get_date()))
        # app.queries.df_PatientAdmissions
        self.colwidths = [15, 10, 10, 15, 15, 20]
        try:
            for j in range(len(self.colwidths)):
                self.e = tk.Label(master=self, fg='black',
                                  text=app.queries.df_PatientAdmissions.columns[j],
                                  font=('Times New Roman', 14, 'bold'),
                                  width=self.colwidths[j],
                                  height=2)
                self.e.grid(row=3, column=j)
            for i in range(5):
                for j in range(app.queries.df_PatientAdmissions.shape[1]):
                    self.e = tk.Label(self, fg='black',
                                      text=app.queries.df_PatientAdmissions.iloc[i, j],
                                      font=('Times New Roman', 12),
                                      width=self.colwidths[j],
                                      height=1)

                    self.e.grid(row=i + 4, column=j)
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print("no data to show")

    def deleteTable(self, app):
        wig = self.grid_slaves()
        for l in wig:
            l.destroy()
        self.__create_widgets(app)
        return


class Frame4(ttk.Frame):
    def __init__(self, app):
        ttk.Frame.__init__(self, master=app, relief=tk.RAISED, borderwidth=2, width=120, height=60)
        self.createButton(app)

    def createButton(self, app):
        self.button = tk.Button(master=self,
                                text="Save&Exit",
                                bg="light green",
                                fg="black",
                                font=('Times New Roman', 12),
                                command=lambda: app.inputs.controlButton())
        self.button.pack(side=tk.BOTTOM)
        return
