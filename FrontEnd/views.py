import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

bg_color = "lightsteelblue"
fg_color = "black"
lbl_color = "blue"


# superinit
# homepage(tk.tk)

class HomePage(tk.Tk):
    def __init__(self, app):
        super().__init__()

        # self.inputs = Insert2DB(self)
        # self.queries = DataQueries(self)
        self.wm_title("Home Page")
        self.bg_color = "white"
        self.fg_color = "black"
        self.lbl_color = "blue"

        self.background_image = tk.PhotoImage(
            file="C:\\Users\\Yuval\\HealthCareApp\\FrontEnd\\61803.png")

        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                 text="Welcome To The Lung Cancer Information System", font=("arial", 25, "bold"),
                 width=60, height=6).pack(pady=20)

        tk.Button(self, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Patient Administration", font=("arial", 15, "bold"),
                  command=lambda: self.open_patient_window(app)).pack(pady=15)

        tk.Button(self, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Doctor Administration", font=("arial", 15, "bold"),
                  command=lambda: self.open_doctor_window(app)).pack(pady=15)

        tk.Button(self, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Sorting and Queries", font=("arial", 15, "bold"),
                  command=lambda: self.open_statistics_window(app)).pack(pady=15)

    def open_patient_window(self, app):
        patient_window = tk.Toplevel(self)
        patient_window.wm_title("Patient Administration")
        bg_color = "lightsteelblue"
        fg_color = "black"
        lbl_color = "blue"
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Add Patient", font=("arial", 15, "bold"), command=lambda: self.open_add_patient(app)).grid(
            pady=15, column=1,
            row=1)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Remove Patient", font=("arial", 15, "bold"), command=lambda: self.remove_patient(app)).grid(
            pady=15,
            column=1, row=2)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Search Patient", font=("arial", 15, "bold"), command=lambda: self.search_patient(app)).grid(
            pady=15,
            column=1, row=3)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Change Patient Status", font=("arial", 15, "bold"),
                  command=lambda: self.change_patient_status(app)).grid(
            pady=15, column=1, row=4)
        tk.Button(patient_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Add Patient Procedure", font=("arial", 15, "bold"),
                  command=lambda: self.add_procedure(app)).grid(
            pady=15, column=1, row=5)

    def search_patient(self, app):
        self.searchPatientWindow = tk.Toplevel()
        self.searchPatientWindow.wm_title("Search Patient ")
        self.searchPatientWindow.geometry("400x200")

        # Create and place the patient data input widgets
        tk.Label(self.searchPatientWindow, text="Patient ID").grid(row=0, column=0)
        self.patient_id_entry = tk.Entry(self.searchPatientWindow)
        self.patient_id_entry.grid(row=0, column=1)
        search_button = tk.Button(self.searchPatientWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Search Patient", font=("arial", 12, "bold"),
                                  command=lambda: self.show_patientSearch_results(app))
        search_button.grid(row=18, column=1)

    # Add a search button to trigger the search
    def show_patientSearch_results(self, app):
        # Create a new window
        results_window = tk.Toplevel()
        results_window.title("Search Results")
        text_area = scrolledtext.ScrolledText(results_window, width=200, height=50)
        patient_id = app.model_input.get_val(self.patient_id_entry)
        app.queries.search_patient(patient_id,app)
        text_area.pack()
        # Insert the dataframe into the text widget
        text_area.insert(tk.END, app.queries.df_patient.to_string(index=False))

        # Disable editing of the text widget
        text_area.configure(state="disabled")

    def change_patient_status(self, app):
        changeStatusWindow = tk.Toplevel()
        changeStatusWindow.wm_title("Change patient status")
        changeStatusWindow.geometry("400x200")

        # Create and place the patient data input widgets
        tk.Label(changeStatusWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(changeStatusWindow)
        patient_id_entry.grid(row=0, column=1)

        # Add a search button to trigger the search
        tk.Label(changeStatusWindow, text="Change Status").grid(row=1, column=0)
        status_entry = tk.StringVar(changeStatusWindow)
        status_entry.set("1")
        status_dropdown = tk.OptionMenu(changeStatusWindow, status_entry, "1", "2", "3")
        status_dropdown.grid(row=1, column=1)

        def status_button_clicked():
            app.queries.update_status(app.model_input.get_val(status_entry), app.model_input.get_val(patient_id_entry),app)

        status_button = tk.Button(changeStatusWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Commit Change", font=("arial", 12, "bold"), command=status_button_clicked)
        status_button.grid(row=2, column=1)

    def search_Doctor(self, app):
        self.searchDoctorWindow = tk.Toplevel()
        self.searchDoctorWindow.wm_title("Search Doctor ")
        self.searchDoctorWindow.geometry("400x200")
        tk.Label(self.searchDoctorWindow, text="Doctor ID").grid(row=0, column=0)
        self.doctor_id_entry = tk.Entry(self.searchDoctorWindow)
        self.doctor_id_entry.grid(row=0, column=1)
        search_button = tk.Button(self.searchDoctorWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Search Doctor", font=("arial", 12, "bold"), command=lambda: self.show_searchDoctor_results(app))
        search_button.grid(row=18, column=1)
        print(app.queries.df_doctor)
    def show_searchDoctor_results(self,app):
        # Create a new window
        results_window = tk.Toplevel()
        results_window.title("Search Results")
        # Create a label to display the results
        text_area = scrolledtext.ScrolledText(results_window, width=200, height=50)
        doctor_id = app.model_input.get_val(self.doctor_id_entry)
        app.queries.search_doctor(doctor_id, app)
        text_area.pack()
        text_area.insert(tk.END, app.queries.df_doctor.to_string(index=False))
        print("hii"+app.queries.df_doctor)
        # Disable editing of the text widget
        text_area.configure(state="disabled")
        # Call the function to display results in a new window
        # Create the search button


    def remove_patient(self, app):
        removePatientWindow = tk.Toplevel()
        removePatientWindow.wm_title("Remove Patient")
        removePatientWindow.geometry("400x200")

        # Create and place the patient ID input widgets
        tk.Label(removePatientWindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(removePatientWindow)
        patient_id_entry.grid(row=0, column=1)

        # Create and place the "Remove" button
        remove_button = tk.Button(removePatientWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Remove Patient", font=("arial", 12, "bold"),
                                  command=lambda: app.model_input.delete_patient(app,
                                      app.model_input.get_val(patient_id_entry)))
        remove_button.grid(row=18, column=1)

    def remove_doctor(self, app):
        removeDoctorWindow = tk.Toplevel()
        removeDoctorWindow.wm_title("Remove Doctor")
        removeDoctorWindow.geometry("400x200")

        # Create and place the patient ID input widgets
        tk.Label(removeDoctorWindow, text="Enter Doctor ID").grid(row=0, column=0)
        doctor_id_entry = tk.Entry(removeDoctorWindow)
        doctor_id_entry.grid(row=0, column=1)

        # Create and place the "Remove" button
        remove_button = tk.Button(removeDoctorWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Remove Doctor", font=("arial", 12, "bold"),
                                  command=lambda: app.model_input.delete_doctor(app,
                                      app.model_input.get_val(doctor_id_entry)))
        remove_button.grid(row=18, column=1)

    def open_add_patient(self, app):
        addPatientWindow = tk.Toplevel()
        addPatientWindow.wm_title("Add Patient Window")
        addPatientWindow.geometry("400x400")

        # Create and place the patient data input widgets
        tk.Label(addPatientWindow, text="Patient ID").grid(row=0, column=0)
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

        tk.Label(addPatientWindow, text="City").grid(row=5, column=0)
        city_entry = tk.Entry(addPatientWindow)
        city_entry.grid(row=5, column=1)

        tk.Label(addPatientWindow, text="BMI").grid(row=6, column=0)
        bmi_entry = tk.Entry(addPatientWindow)
        bmi_entry.grid(row=6, column=1)

        tk.Label(addPatientWindow, text="BP Sys").grid(row=7, column=0)
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

        tk.Label(addPatientWindow, text="Cardiovascular").grid(row=11, column=0)
        cvd_entry = tk.IntVar()
        cvd_checkbox = tk.Checkbutton(addPatientWindow, variable=cvd_entry)
        cvd_checkbox.grid(row=11, column=1)

        tk.Label(addPatientWindow, text="Tuberculosis").grid(row=12, column=0)
        Tuberculosis_entry = tk.IntVar()
        Tuberculosis_checkbox = tk.Checkbutton(addPatientWindow, variable=Tuberculosis_entry)
        Tuberculosis_checkbox.grid(row=12, column=1)

        tk.Label(addPatientWindow, text="Pulmonary Fibrosis").grid(row=13, column=0)
        Pulmonary_fibrosis_entry = tk.IntVar()
        Pulmonary_fibrosis_checkbox = tk.Checkbutton(addPatientWindow, variable=Pulmonary_fibrosis_entry)
        Pulmonary_fibrosis_checkbox.grid(row=13, column=1)

        tk.Label(addPatientWindow, text="Sick").grid(row=14, column=0)
        sick_entry = tk.IntVar()
        sick_checkbox = tk.Checkbutton(addPatientWindow, variable=sick_entry)
        sick_checkbox.grid(row=14, column=1)
        #  ok_button = tk.Button(addPatientWindow, text="assign patient")
        ok_button = tk.Button(addPatientWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                              text="Add Patient", font=("arial", 12, "bold"),
                              command=lambda: app.model_input.InsertPatient(app,app.model_input.get_val(patient_id_entry),
                                                                     app.model_input.get_val(first_name_entry),
                                                                     app.model_input.get_val(last_name_entry),
                                                                     app.model_input.get_val(gender_entry),
                                                                     app.model_input.get_val(dob_entry),
                                                                     app.model_input.get_val(city_entry),
                                                                     app.model_input.get_val(bmi_entry),
                                                                     app.model_input.get_val(bp_sys_entry),
                                                                     app.model_input.get_val(bp_dia_entry),
                                                                     app.model_input.get_val(copd_entry),
                                                                     app.model_input.get_val(smoking_entry),
                                                                     app.model_input.get_val(copd_entry),
                                                                     app.model_input.get_val(Tuberculosis_entry),
                                                                     app.model_input.get_val(Pulmonary_fibrosis_entry),
                                                                     app.model_input.get_val(sick_entry)))
        ok_button.grid(row=17, column=1)
        # Tuberculosis,Pulmonary_fibrosis,sick
        # Add a label for displaying the success message

    def open_add_doctor(self, app):
        addDoctorWindow = tk.Toplevel()
        addDoctorWindow.wm_title("Add Doctor")
        addDoctorWindow.geometry("400x400")

        # Create and place the patient data input widgets
        tk.Label(addDoctorWindow, text="Doctor ID").grid(row=0, column=0)
        doctor_id_entry = tk.Entry(addDoctorWindow)
        doctor_id_entry.grid(row=0, column=1)

        tk.Label(addDoctorWindow, text="First Name").grid(row=1, column=0)
        first_name_entry = tk.Entry(addDoctorWindow)
        first_name_entry.grid(row=1, column=1)

        tk.Label(addDoctorWindow, text="Last Name").grid(row=2, column=0)
        last_name_entry = tk.Entry(addDoctorWindow)
        last_name_entry.grid(row=2, column=1)

        tk.Label(addDoctorWindow, text="Gender").grid(row=3, column=0)
        gender_entry = tk.StringVar(addDoctorWindow)
        gender_entry.set("Male")
        gender_dropdown = tk.OptionMenu(addDoctorWindow, gender_entry, "Male", "Female", "Other")
        gender_dropdown.grid(row=3, column=1)

        tk.Label(addDoctorWindow, text="Date of Birth").grid(row=4, column=0)
        dob_entry = DateEntry(addDoctorWindow, date_pattern="yyyy-mm-dd")
        dob_entry.grid(row=4, column=1)

        tk.Label(addDoctorWindow, text="Start Work Date").grid(row=5, column=0)
        Startwork_entry = DateEntry(addDoctorWindow, date_pattern="yyyy-mm-dd")
        Startwork_entry.grid(row=5, column=1)

        ok_button = tk.Button(addDoctorWindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                              text="Add Doctor", font=("arial", 12, "bold"),
                              command=lambda: app.model_input.InsertDoctor(app,app.model_input.get_val(doctor_id_entry),
                                                                           app.model_input.get_val(first_name_entry),
                                                                           app.model_input.get_val(last_name_entry),
                                                                           app.model_input.get_val(Startwork_entry),
                                                                           app.model_input.get_val(dob_entry),
                                                                           app.model_input.get_val(gender_entry)))
        ok_button.grid(row=18, column=1)

    def add_procedure(self, app):
        addprocedurewindow = tk.Toplevel()
        addprocedurewindow.wm_title("Add Patient Procedure")
        addprocedurewindow.geometry("400x200")

        # Create and place the patient data input widgets
        tk.Label(addprocedurewindow, text="Patient ID").grid(row=0, column=0)
        patient_id_entry = tk.Entry(addprocedurewindow)
        patient_id_entry.grid(row=0, column=1)

        tk.Label(addprocedurewindow, text="Doctor ID").grid(row=1, column=0)
        doctor_id = tk.Entry(addprocedurewindow)
        doctor_id.grid(row=1, column=1)

        tk.Label(addprocedurewindow, text="Procedure ID").grid(row=2, column=0)
        id_procedure = tk.Entry(addprocedurewindow)
        id_procedure.grid(row=2, column=1)

        tk.Label(addprocedurewindow, text="Procedure Date").grid(row=3, column=0)
        procedure_date = DateEntry(addprocedurewindow, date_pattern="yyyy-mm-dd")
        procedure_date.grid(row=3, column=1)

        tk.Label(addprocedurewindow, text="Sick").grid(row=4, column=0)
        sick = tk.StringVar(addprocedurewindow)
        sick.set("1")
        sick_dropdown = tk.OptionMenu(addprocedurewindow, sick, "1", "2", "3")
        sick_dropdown.grid(row=4, column=1)

        def combined_function():
            app.model_input.InsertPrecedure(app,app.model_input.get_val(patient_id_entry),
                                            app.model_input.get_val(doctor_id),
                                            app.model_input.get_val(id_procedure),
                                            app.model_input.get_val(procedure_date),
                                            app.model_input.get_val(sick))

            app.queries.update_status(app.model_input.get_val(sick), app.model_input.get_val(patient_id_entry),app)

        ok_button = tk.Button(addprocedurewindow, width=20, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                              text="Add Patient Procedure", font=("arial", 12, "bold"),
                              command=combined_function)
        ok_button.grid(row=18, column=1)

    def open_doctor_window(self, app):
        doctor_window = tk.Toplevel(self)
        doctor_window.wm_title("Doctor Administration")
        bg_color = "lightsteelblue"
        fg_color = "black"
        lbl_color = "blue"
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Add Doctor", font=("arial", 15, "bold"), command=lambda: self.open_add_doctor(app)).grid(
            pady=15, column=1,
            row=1)
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Remove Doctor", font=("arial", 15, "bold"), command=lambda: self.remove_doctor(app)).grid(
            pady=15, column=1,
            row=2)
        tk.Button(doctor_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Search Doctor", font=("arial", 15, "bold"), command=lambda: self.search_Doctor(app)).grid(
            pady=15, column=1,
            row=3)

    def open_statistics_window(self, app):
        self.statistics_window = tk.Toplevel(self)
        self.statistics_window.wm_title("Statistics")
        bg_color = "lightsteelblue"
        fg_color = "black"
        lbl_color = "blue"

        #  tk.Button(statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
        #           text="Sorting", font=("arial", 15, "bold")).grid(pady=15, column=1, row=1)

        sort_button = tk.Button(self.statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                text="Sorting",
                                font=("arial", 15, "bold"),
                                command=lambda : self.show_Sorting_results(app))
        sort_button.grid(pady=15, column=1, row=1)
        search_button = tk.Button(self.statistics_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                                  text="Patients With Most Treatments", font=("arial", 15, "bold"),
                                  command=lambda :self.show_most_procedure_results(app))
        search_button.grid(pady=15, column=1, row=2)
        search_button = tk.Button(self.statistics_window, text="Busiest Month", width=30, relief=tk.GROOVE, fg=fg_color,
                                  bg=bg_color,
                                  font=("arial", 15, "bold"), command=lambda: self.show_busyMonth_results(app))
        search_button.grid(pady=15, column=1, row=5)

        # search_button = tk.Button(statistics_window, text="Most efficient treatment", width=30, relief=tk.GROOVE, fg=fg_color,
        #                         bg=bg_color,
        #                        font=("arial", 15, "bold"), command=precedure_button_clicked)
        # search_button.grid(pady=15, column=1, row=3)

    def show_most_procedure_results(self,app):
        # Create a new window
        app.queries.query_most_procedure(app)
        self.results_window = tk.Toplevel()
        self.results_window.title("Top Treatments Results")
        self.results_window.geometry("400x400")
        # Create a label to display the results

        text_area = scrolledtext.ScrolledText(self.results_window, width=200, height=50)
        text_area.pack()

        # Insert the dataframe into the text widget
        text_area.insert(tk.END, app.queries.df_proc.to_string(index=False))

        # Disable editing of the text widget
        text_area.configure(state="disabled")

    def show_busyMonth_results(self,app):
        # Create a new window
        app.queries.queryBusyMonth(app)
        results_window = tk.Toplevel()
        results_window.title("The Busiest Months")
        results_window.geometry("400x400")
        # Create a label to display the results

        text_area = scrolledtext.ScrolledText(results_window, width=200, height=50)
        text_area.pack()
        # Insert the dataframe into the text widget
        text_area.insert(tk.END, app.queries.df_busyMonth.to_string(index=False))
        # Disable editing of the text widget
        text_area.configure(state="disabled")


    def show_Sorting_results(self,app):
        # Create a new window
        self.results_window = tk.Toplevel()
        self.results_window.geometry("800x500")
        tk.Label(self.results_window, text="Gender").grid(row=3, column=0)
        self.gender_entry = tk.StringVar(self.results_window)
        self.gender_entry.set(None)
        self.gender_dropdown = tk.OptionMenu(self.results_window, self.gender_entry, "Male", "Female", "Other", None)
        self.gender_dropdown.grid(row=3, column=1)

        self.status_entry = tk.StringVar(self.results_window)
        self.status_entry.set("Over")
        self.status_dropdown = tk.OptionMenu(self.results_window, self.status_entry, "Over", "Under", "Between")
        self.status_dropdown.grid(row=4, column=3)

        self.dob_entry1 = tk.StringVar(self.results_window)
        self.dob_entry1.set(None)
        self.dob_entry1_dropdown = tk.OptionMenu(self.results_window, self.dob_entry1, "Yes", None)
        self.dob_entry1_dropdown.grid(row=4, column=1)

        tk.Label(self.results_window, text="Age Range").grid(row=4, column=0)
        self.dob_entry = DateEntry(self.results_window, date_pattern="yyyy-mm-dd")
        self.dob_entry.grid(row=4, column=2)
        self.dob_entry.delete(0, "end")

        self.date_started = DateEntry(self.results_window, locale='en_US', date_pattern='yyyy-mm-dd')
        self.date_started.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.date_started.grid(row=4, column=4)

        self.city_entry1 = tk.StringVar(self.results_window)
        self.city_entry1.set(None)
        self.city_entry1_dropdown = tk.OptionMenu(self.results_window, self.city_entry1, "yes", None)
        self.city_entry1_dropdown.grid(row=5, column=1)

        tk.Label(self.results_window, text="City").grid(row=5, column=0)
        self.city_entry = tk.Entry(self.results_window)
        self.city_entry.grid(row=5, column=2)

        self.bmi_entry1 = tk.StringVar(self.results_window)
        self.bmi_entry1.set(None)
        self.bmi_entry1dropdown = tk.OptionMenu(self.results_window, self.bmi_entry1, "yes", None)
        self.bmi_entry1dropdown.grid(row=6, column=1)

        tk.Label(self.results_window, text="BMI").grid(row=6, column=0)
        self.bmi_entry = tk.Entry(self.results_window)
        self.bmi_entry.grid(row=6, column=2)

        self.bp_sys_entry1 = tk.StringVar(self.results_window)
        self.bp_sys_entry1.set(None)
        self.bp_sys_entry1dropdown = tk.OptionMenu(self.results_window, self.bp_sys_entry1, "yes", None)
        self.bp_sys_entry1dropdown.grid(row=7, column=1)

        tk.Label(self.results_window, text="BP Sys").grid(row=7, column=0)
        self.bp_sys_entry = tk.Entry(self.results_window)
        self.bp_sys_entry.grid(row=7, column=2)

        self.bp_dia_entry1 = tk.StringVar(self.results_window)
        self.bp_dia_entry1.set(None)
        self.bp_dia_entry1dropdown = tk.OptionMenu(self.results_window, self.bp_dia_entry1, "yes", None)
        self.bp_dia_entry1dropdown.grid(row=8, column=1)
        tk.Label(self.results_window, text="BP Dia").grid(row=8, column=0)
        self.bp_dia_entry = tk.Entry(self.results_window)
        self.bp_dia_entry.grid(row=8, column=2)

        tk.Label(self.results_window, text="COPD").grid(row=9, column=0)
        self.copd_entry = tk.StringVar(self.results_window)
        self.copd_entry.set(None)
        self.copd_checkbox = tk.OptionMenu(self.results_window, self.copd_entry, "1", "0", None)
        self.copd_checkbox.grid(row=9, column=1)

        tk.Label(self.results_window, text="Smoking").grid(row=10, column=0)
        self.smoking_entry = tk.StringVar(self.results_window)
        self.smoking_entry.set(None)
        self.smoking_checkbox = tk.OptionMenu(self.results_window, self.smoking_entry, "1", "0", None)
        self.smoking_checkbox.grid(row=10, column=1)
        tk.Label(self.results_window, text="Cardiovascular").grid(row=11, column=0)
        self.cvd_entry = tk.StringVar(self.results_window)
        self.cvd_entry.set(None)
        self.cvd_entry_dropdown = tk.OptionMenu(self.results_window, self.cvd_entry, "1", "0", None)
        self.cvd_entry_dropdown.grid(row=11, column=1)

        tk.Label(self.results_window, text="Tuberculosis").grid(row=12, column=0)
        self.tuberculosis_entry = tk.StringVar(self.results_window)
        self.tuberculosis_entry.set(None)
        self.Tuberculosis_checkbox = tk.OptionMenu(self.results_window, self.tuberculosis_entry, "1", "0", None)
        self.Tuberculosis_checkbox.grid(row=12, column=1)

        tk.Label(self.results_window, text="Pulmonary Fibrosis").grid(row=13, column=0)
        self.pulmonary_fibrosis_entry = tk.StringVar(self.results_window)
        self.pulmonary_fibrosis_entry.set(None)
        self.Pulmonary_fibrosis_checkbox = tk.OptionMenu(self.results_window, self.pulmonary_fibrosis_entry, "1", "0", None)
        self.Pulmonary_fibrosis_checkbox.grid(row=13, column=1)

        tk.Label(self.results_window, text="Sick").grid(row=14, column=0)
        self.sick_entry = tk.StringVar(self.results_window)
        self.sick_entry.set(None)
        self.sick_checkbox = tk.OptionMenu(self.results_window, self.sick_entry, "1", "0", None)
        self.sick_checkbox.grid(row=14, column=1)

        tk.Button(self.results_window, width=30, relief=tk.GROOVE, fg=fg_color, bg=bg_color,
                  text="Start Filter", font=("arial", 15, "bold"), command=lambda: self.show_Sortresults(app)).grid(
            pady=15, column=1,
            row=15)
        self.results_window.title("Sorting Filters")

    def show_Sortresults(self,app):
        # Get the sorting results
        gender = app.model_input.get_val(self.gender_entry)
        dob_value = app.model_input.get_val(self.dob_entry)
        dob_checkbox = app.model_input.get_val(self.dob_entry1)
        dob_status = app.model_input.get_val(self.status_entry)
        dob_value2 = app.model_input.get_val(self.date_started)
        city = app.model_input.get_val(self.city_entry)
        city_checkbox = app.model_input.get_val(self.city_entry1)
        bmi = app.model_input.get_val(self.bmi_entry)
        bmi_checkbox = app.model_input.get_val(self.bmi_entry1)
        bp_sys = app.model_input.get_val(self.bp_sys_entry)
        bp_sys_checkbox = app.model_input.get_val(self.bp_sys_entry1)
        bp_dia = app.model_input.get_val(self.bp_dia_entry)
        bp_dia_checkbox = app.model_input.get_val(self.bp_dia_entry1)
        copd = app.model_input.get_val(self.copd_entry)
        smoking = app.model_input.get_val(self.smoking_entry)
        cvd = app.model_input.get_val(self.cvd_entry)
        tuberculosis = app.model_input.get_val(self.tuberculosis_entry)
        pulmonary_fibrosis = app.model_input.get_val(self.pulmonary_fibrosis_entry)
        sick = app.model_input.get_val(self.sick_entry)

        print(
            f"Gender: {gender}, Date of Birth: {dob_value}, City: {city}, BMI: {bmi}, BP SYS: {bp_sys}, BP Dia: {bp_dia}, "
            f"COPD: {copd}, Smoking: {smoking}, Cardiovascular: {cvd}, Tuberculosis: {tuberculosis}, "
            f"Pulmonary Fibrosis: {pulmonary_fibrosis}, Sick: {sick}")

        # Call the sorting_val function with the selected values
        app.queries.sorting_val(app,
            gender=gender,
            date_of_birth_checkbox=dob_checkbox,
            date_of_birth=dob_value,
            date_of_birth_checkbox2=dob_status,
            date_of_birth2=dob_value2,
            city_checkbox=city_checkbox,
            Cities=city,
            bmi_checkbox=bmi_checkbox,
            BMI=bmi,
            bp_sys_checkbox=bp_sys_checkbox,
            BP_SYS=bp_sys,
            bp_Dia_checkbox=bp_dia_checkbox,
            BP_Dia=bp_dia,
            COPD=copd,
            smoking=smoking,
            Cardiovascular=cvd,
            Tuberculosis=tuberculosis,
            Pulmonary_fibrosis=pulmonary_fibrosis,
            sick=sick
        )

        # Create a new window to display the results
        self.results_window = tk.Toplevel()
        self.results_window.title("Sorting Results")
        # Create a text widget with a scrollbar
        text_area = scrolledtext.ScrolledText(self.results_window, width=200, height=50)
        text_area.pack()

        # Insert the dataframe into the text widget
        text_area.insert(tk.END, app.queries.df_sorting_patient.to_string(index=False))

        # Disable editing of the text widget
        text_area.configure(state="disabled")

    def mssg_box(self,*args):
        tk.messagebox.showinfo(title = "",message=f"{args}")
    def run(self):
        self.mainloop()
