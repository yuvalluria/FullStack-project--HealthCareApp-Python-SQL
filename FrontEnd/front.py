import tkinter as tk
from tkinter import ttk

import mysql.connector
from tkcalendar import Calendar, DateEntry
import sys
import app

"""
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
"""

import tkinter as tk
from tkcalendar import DateEntry


class HomePage:
    def __init__(self):
        self.homePageWindow = tk.Tk()
        self.homePageWindow.wm_title("Home Page")
        bg_color = "purple"
        fg_color = "white"
        lbl_color = 'blue'
        tk.Label(self.homePageWindow, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                 text="welcome to the lung cancer information system",
                 font=("arial", 20, "bold"), width=60, height=6).grid(pady=20, column=1, row=1)
        tk.Button(self.homePageWindow, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Patient administration", font=("arial", 15, "bold"), command=self.open_patient_window).grid(
            pady=15, column=1, row=3)
        tk.Button(self.homePageWindow, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Doctor administration", font=("arial", 15, "bold"), command=self.open_doctor_window).grid(
            pady=15, column=1, row=4)
        tk.Button(self.homePageWindow, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Statistics", font=("arial", 15, "bold"), command=self.open_statistics_window).grid(pady=15,
                                                                                                           column=1,
                                                                                                           row=5)

    def search_patient(self):
        searchPatientWindow = tk.Toplevel()
        searchPatientWindow.wm_title("Search Patient ")
        searchPatientWindow.geometry("400x400")

        # Create and place the patient data input widgets
        tk.Label(searchPatientWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(searchPatientWindow)
        patient_id_entry.grid(row=0, column=1)

        # Add a search button to trigger the search
        search_button = tk.Button(searchPatientWindow, text="Search")
        search_button.grid(row=1, column=0, columnspan=2)

    def change_patient_status(self):
        changeStatusWindow = tk.Toplevel()
        changeStatusWindow.wm_title("Change patient status")
        changeStatusWindow.geometry("400x400")

        # Create and place the patient data input widgets
        tk.Label(changeStatusWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(changeStatusWindow)
        patient_id_entry.grid(row=0, column=1)

        # Add a search button to trigger the search
        tk.Label(changeStatusWindow, text="change status").grid(row=1, column=0)
        status_entry = tk.StringVar(changeStatusWindow)
        status_entry.set("Same status")
        status_dropdown = tk.OptionMenu(changeStatusWindow, status_entry, "Same status", "2", "3")
        status_dropdown.grid(row=1, column=1)
        status_button = tk.Button(changeStatusWindow, text="commit change")
        status_button.grid(row=2, column=1, columnspan=2)

    def search_doctor(self):
        searchDoctorWindow = tk.Toplevel()
        searchDoctorWindow.wm_title("Search Doctor ")
        searchDoctorWindow.geometry("400x400")

        # Create and place the doctor data input widgets
        tk.Label(searchDoctorWindow, text="Doctor ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(searchDoctorWindow)
        patient_id_entry.grid(row=0, column=1)

        # Add a search button to trigger the search
        search_button = tk.Button(searchDoctorWindow, text="Search")
        search_button.grid(row=1, column=0, columnspan=2)

    def remove_patient(self):
        removePatientWindow = tk.Toplevel()
        removePatientWindow.wm_title("Remove Patient")
        removePatientWindow.geometry("400x200")

        # Create and place the patient ID input widgets
        tk.Label(removePatientWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(removePatientWindow)
        patient_id_entry.grid(row=0, column=1)

        # Create and place the "Remove" button
        remove_button = tk.Button(removePatientWindow, text="Remove")
        remove_button.grid(row=1, column=1)

    def remove_doctor(self):
        removeDoctorWindow = tk.Toplevel()
        removeDoctorWindow.wm_title("Remove Doctor")
        removeDoctorWindow.geometry("400x200")

        # Create and place the patient ID input widgets
        tk.Label(removeDoctorWindow, text="Enter Doctor ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(removeDoctorWindow)
        patient_id_entry.grid(row=0, column=1)

        # Create and place the "Remove" button
        remove_button = tk.Button(removeDoctorWindow, text="Remove")
        remove_button.grid(row=1, column=1)

    def open_add_patient(self):
        addPatientWindow = tk.Toplevel()
        addPatientWindow.wm_title("Add Patient Window")
        addPatientWindow.geometry("400x400")

        # Create and place the patient data input widgets
        tk.Label(addPatientWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(addPatientWindow)
        patient_id_entry.grid(row=0, column=1)
        #self.patient_id_entry.bind("<Button-1>", lambda e: self.patient_id_entry.delete(0, "end"))
        #self.patient_id_entry.bind("<Leave>", lambda e: app.inputs.set_val(self.patient_id_entry, "PatientID"))

        tk.Label(addPatientWindow, text="First Name").grid(row=1, column=0)
        first_name_entry = tk.Entry(addPatientWindow)
        first_name_entry.grid(row=1, column=1)

        tk.Label(addPatientWindow, text="Last Name").grid(row=2, column=0)
        last_name_entry = tk.Entry(addPatientWindow)
        last_name_entry.grid(row=2, column=1)

        tk.Label(addPatientWindow, text="Gender").grid(row=3, column=0)
        gender_entry = tk.StringVar(addPatientWindow)
        gender_entry.set("Male")
        gender_dropdown = tk.OptionMenu(addPatientWindow, gender_entry, "Male", "Female", "Other")
        gender_dropdown.grid(row=3, column=1)

        tk.Label(addPatientWindow, text="Date of Birth").grid(row=4, column=0)
        dob_entry = DateEntry(addPatientWindow, date_pattern="yyyy-mm-dd")
        dob_entry.grid(row=4, column=1)

        tk.Label(addPatientWindow, text="City").grid(row=5, column=0)
        city_entry = tk.Entry(addPatientWindow)
        city_entry.grid(row=5, column=1)

        tk.Label(addPatientWindow, text="BMI").grid(row=6, column=0)
        bmi_entry = tk.Entry(addPatientWindow)
        bmi_entry.grid(row=6, column=1)

        tk.Label(addPatientWindow, text="BP SYS").grid(row=7, column=0)
        bp_sys_entry = tk.Entry(addPatientWindow)
        bp_sys_entry.grid(row=7, column=1)

        tk.Label(addPatientWindow, text="BP Dia").grid(row=8, column=0)
        bp_dia_entry = tk.Entry(addPatientWindow)
        bp_dia_entry.grid(row=8, column=1)

        tk.Label(addPatientWindow, text="COPD").grid(row=9, column=0)
        copd_entry = tk.IntVar()
        copd_checkbox = tk.Checkbutton(addPatientWindow, variable=copd_entry)
        copd_checkbox.grid(row=9, column=1)

        tk.Label(addPatientWindow, text="Smoking").grid(row=10, column=0)
        smoking_entry = tk.IntVar(value=0)
        smoking_checkbox = tk.Checkbutton(addPatientWindow, variable=smoking_entry, onvalue=1, offvalue=0)
        smoking_checkbox.grid(row=10, column=1)

        tk.Label(addPatientWindow, text="Smoking").grid(row=11, column=0)
        smoking_choice = tk.StringVar()
        smoking_choice.set("No")  # Set default value to "No"

        # Create radio buttons for smoking option
        tk.Radiobutton(addPatientWindow, text="Yes", variable=smoking_choice, value="Yes").grid(row=11, column=1)
        tk.Radiobutton(addPatientWindow, text="No", variable=smoking_choice, value="No").grid(row=11, column=2)

        tk.Label(addPatientWindow, text="Cardiovascular").grid(row=12, column=0)
        cvd_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(addPatientWindow, variable=cvd_entry)
        cvd_checkbox.grid(row=12, column=1)

        tk.Label(addPatientWindow, text="Tuberculosis").grid(row=13, column=0)
        cvd_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(addPatientWindow, variable=cvd_entry)
        cvd_checkbox.grid(row=13, column=1)

        tk.Label(addPatientWindow, text="Pulmonary fibrosis").grid(row=14, column=0)
        cvd_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(addPatientWindow, variable=cvd_entry)
        cvd_checkbox.grid(row=14, column=1)

        tk.Label(addPatientWindow, text="sick").grid(row=15, column=0)
        cvd_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(addPatientWindow, variable=cvd_entry)
        cvd_checkbox.grid(row=15, column=1)

        # Tuberculosis,Pulmonary_fibrosis,sick
        patientid = patient_id_entry.get()
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        city = city_entry.get()
        bmi = bmi_entry.get()
        bp_sis = bp_sys_entry.get()
        bp_dia = bp_dia_entry.get()
        copd = copd_entry.get()
        smoke = smoking_entry.get()
        cvd = cvd_entry.get()
        connection = mysql.connector.connect(host='localhost', user='root', password='12345',
                                             port='3306', database='lung_cancer')
        c = connection.cursor()

        insert_query = "INSERT INTO patients(patientid,firstname,lastname,gender,dob,city,bmi,bp_sis,bp_dia,copd,smoke,cvd) VALUES( % s, % s, % s, % s)"
        vals = (patientid, firstname, lastname, gender, dob, city, bmi, bp_sis, bp_dia, copd, smoke, cvd)
        c.execute(insert_query, vals)
        connection.commit()

    def open_add_doctor(self):
        addPatientWindow = tk.Toplevel()
        addPatientWindow.wm_title("Add Doctor")
        addPatientWindow.geometry("500x500")

        # Create and place the patient data input widgets
        tk.Label(addPatientWindow, text="Doctor ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(addPatientWindow)
        patient_id_entry.grid(row=0, column=1)

        tk.Label(addPatientWindow, text="First Name").grid(row=1, column=0)
        first_name_entry = tk.Entry(addPatientWindow)
        first_name_entry.grid(row=1, column=1)

        tk.Label(addPatientWindow, text="Last Name").grid(row=2, column=0)
        last_name_entry = tk.Entry(addPatientWindow)
        last_name_entry.grid(row=2, column=1)

        tk.Label(addPatientWindow, text="Gender").grid(row=3, column=0)
        gender_entry = tk.StringVar(addPatientWindow)
        gender_entry.set("Male")
        gender_dropdown = tk.OptionMenu(addPatientWindow, gender_entry, "Male", "Female", "Other")
        gender_dropdown.grid(row=3, column=1)

        tk.Label(addPatientWindow, text="Date of Birth").grid(row=4, column=0)
        dob_entry = DateEntry(addPatientWindow, date_pattern="yyyy-mm-dd")
        dob_entry.grid(row=4, column=1)

        tk.Label(addPatientWindow, text="Start work date").grid(row=5, column=0)
        dob_entry = DateEntry(addPatientWindow, date_pattern="yyyy-mm-dd")
        dob_entry.grid(row=5, column=1)

    def open_patient_window(self):
        patient_window = tk.Toplevel(self.homePageWindow)
        patient_window.wm_title("Patient Administration")
        bg_color = "purple"
        fg_color = "white"
        lbl_color = 'blue'
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Add Patient", font=("arial", 15, "bold"), command=self.open_add_patient).grid(pady=15, column=1,
                                                                                                      row=1)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Remove Patient", font=("arial", 15, "bold"), command=self.remove_patient).grid(pady=15,
                                                                                                       column=1, row=2)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Search Patient", font=("arial", 15, "bold"), command=self.search_patient).grid(pady=15,
                                                                                                       column=1, row=3)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Change Patient Status", font=("arial", 15, "bold"), command=self.change_patient_status).grid(
            pady=15, column=1, row=4)

    def open_doctor_window(self):
        doctor_window = tk.Toplevel(self.homePageWindow)
        doctor_window.wm_title("Doctor Administration")
        bg_color = "purple"
        fg_color = "white"
        lbl_color = 'blue'
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Add Doctor", font=("arial", 15, "bold"), command=self.open_add_doctor).grid(pady=15, column=1,
                                                                                                    row=1)
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Remove Doctor", font=("arial", 15, "bold"), command=self.remove_doctor).grid(pady=15, column=1,
                                                                                                     row=2)
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Search doctor", font=("arial", 15, "bold"), command=self.search_doctor).grid(pady=15, column=1,
                                                                                                     row=3)

    def open_statistics_window(self):
        statistics_window = tk.Toplevel(self.homePageWindow)
        statistics_window.wm_title("Statistics")
        bg_color = "purple"
        fg_color = "white"
        lbl_color = 'blue'
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Sorting", font=("arial", 15, "bold")).grid(pady=15, column=1, row=1)
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Best doctor of the month", font=("arial", 15, "bold")).grid(pady=15, column=1, row=2)
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Most efficient treatment", font=("arial", 15, "bold")).grid(pady=15, column=1, row=3)
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Most efficient treatment", font=("arial", 15, "bold")).grid(pady=15, column=1, row=4)
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Busiest month", font=("arial", 15, "bold")).grid(pady=15, column=1, row=5)
        tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Duration of treatment", font=("arial", 15, "bold")).grid(pady=15, column=1, row=6)

    def run(self):
        self.homePageWindow.mainloop()


homePage = HomePage()
homePage.run()
