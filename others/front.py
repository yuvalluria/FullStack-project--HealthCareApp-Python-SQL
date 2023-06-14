import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkcalendar import Calendar, DateEntry
import sys
import app
from tkcalendar import DateEntry
from Communication.queries import *


class HomePage:
    def __init__(self):
        self.homePageWindow = tk.Tk()
        self.homePageWindow.wm_title("Home Page")
        self.__create_widgets(app)
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

    def __create_widgets(self, app):
        addPatientWindow = tk.Toplevel()
        addPatientWindow.wm_title("Add Patient Window")
        addPatientWindow.geometry("400x400")

    def addPatientWindow(self, app):
        # Create and place the patient data input widgets
        tk.Label(self.addPatientWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(self, width=22)
        patient_id_entry.insert(0, 'patient_id')
        patient_id_entry.grid(row=0, column=1)
        self.patient_id_entry.bind("<Button-1>", lambda e: self.patient_id_entry.delete(0, "end"))
        self.patient_id_entry.bind("<Leave>", lambda e: app.inputs.set_val(self.patient_id_entry, "patient_id"))
        tk.Label(self.addPatientWindow, text="First Name").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.addPatientWindow)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.addPatientWindow, text="Last Name").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.addPatientWindow)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.addPatientWindow, text="Gender").grid(row=3, column=0)
        self.gender_entry = tk.StringVar(self.addPatientWindow)
        self.gender_entry.set("Male")
        gender_dropdown = tk.OptionMenu(addPatientWindow, gender_entry, "Male", "Female", "Other")
        gender_dropdown.grid(row=3, column=1)

        tk.Label(self.addPatientWindow, text="Date of Birth").grid(row=4, column=0)
        self.dob_entry = DateEntry(self.addPatientWindow, date_pattern="yyyy-mm-dd")
        self.dob_entry.grid(row=4, column=1)
        self.dob_entry.bind("<<CalendarSelected>>", lambda e: self.dob_entry.get_date)

        tk.Label(self.addPatientWindow, text="City").grid(row=5, column=0)
        self.city_entry = tk.Entry(self.addPatientWindow)
        self.city_entry.grid(row=5, column=1)

        tk.Label(self.addPatientWindow, text="BMI").grid(row=6, column=0)
        self.bmi_entry = tk.Entry(self.addPatientWindow)
        self.bmi_entry.grid(row=6, column=1)

        tk.Label(self.addPatientWindow, text="BP SYS").grid(row=7, column=0)
        self.bp_sys_entry = tk.Entry(self.addPatientWindow)
        self.bp_sys_entry.grid(row=7, column=1)

        tk.Label(self.addPatientWindow, text="BP Dia").grid(row=8, column=0)
        self.bp_dia_entry = tk.Entry(self.addPatientWindow)
        self.bp_dia_entry.grid(row=8, column=1)

        tk.Label(self.addPatientWindow, text="COPD").grid(row=9, column=0)
        self.copd_entry = tk.IntVar()
        copd_checkbox = tk.Checkbutton(self.addPatientWindow, variable=self.copd_entry)
        copd_checkbox.grid(row=9, column=1)

        tk.Label(self.addPatientWindow, text="Smoking").grid(row=10, column=0)
        self.smoking_entry = tk.IntVar(value=0)
        smoking_checkbox = tk.Checkbutton(self.addPatientWindow, variable=self.smoking_entry, onvalue=1, offvalue=0)
        smoking_checkbox.grid(row=10, column=1)

        tk.Label(self.addPatientWindow, text="Smoking").grid(row=11, column=0)
        smoking_choice = tk.StringVar()
        smoking_choice.set("No")  # Set default value to "No"

        # Create radio buttons for smoking option
        tk.Radiobutton(self.addPatientWindow, text="Yes", variable=smoking_choice, value="Yes").grid(row=11, column=1)
        tk.Radiobutton(self.addPatientWindow, text="No", variable=smoking_choice, value="No").grid(row=11, column=2)

        tk.Label(self.addPatientWindow, text="hereditary_retinoblastoma").grid(row=12, column=0)
        self.hereditary_retinoblastoma_entry = tk.IntVar()
        hereditary_retinoblastoma_checkbox = tk.Checkbutton(self.addPatientWindow,
                                                            variable=self.hereditary_retinoblastoma_entry)
        hereditary_retinoblastoma_checkbox.grid(row=12, column=1)

        tk.Label(self.addPatientWindow, text="Tuberculosis").grid(row=13, column=0)
        self.Tuberculosis_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(self.addPatientWindow, variable=self.Tuberculosis_entry)
        cvd_checkbox.grid(row=13, column=1)

        tk.Label(self.addPatientWindow, text="Pulmonary_fibrosis").grid(row=14, column=0)
        self.Pulmonary_fibrosis_entry = tk.IntVar()
        Pulmonary_fibrosis_checkbox = tk.Checkbutton(self.addPatientWindow, variable=self.Pulmonary_fibrosis_entry)
        Pulmonary_fibrosis_checkbox.grid(row=14, column=1)

        tk.Label(self.addPatientWindow, text="sick").grid(row=15, column=0)
        self.sick_entry = tk.IntVar()
        sick_checkbox = tk.Checkbutton(self.addPatientWindow, variable=self.sick_entry)
        sick_checkbox.grid(row=15, column=1)

        ok_button = tk.Button(self.addPatientWindow, text="assign patient")
        ok_button.grid(row=18, column=1)
        loadDataButton = ttk.Button(self, style="TButton", text="show_table_patients",
                                    command=lambda: self.showTable(app))

    def showTable(self, app):
        app.queries.Insert(self.patient_id_entry.get(), self.first_name_entry.get(), self.last_name_entry.get(),
                           self.gender_entry.get(),
                           self.dob_entry.get(), self.city_entry.get(), self.bmi_entry.get(), self.bp_sys_entry.get(),
                           self.bp_dia_entry.get(),
                           self.copd_entry.get(), self.smoking_entry.get(), self.hereditary_retinoblastoma_entry.get(),
                           self.Tuberculosis_entry.get(), self.Pulmonary_fibrosis_entry.get(), self.sick_entry.get())
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
        tk.Label(addPatientWindow, text="Start work date").grid(row=5, column=0)
        dob_entry = DateEntry(addPatientWindow, date_pattern="yyyy-mm-dd")
        ok_button = tk.Button(addPatientWindow, text="assign doctor")
        ok_button.grid(row=18, column=1)

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
