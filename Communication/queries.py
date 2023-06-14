# -- coding: utf-8 --
"""
Omer ,Doron, Yuval lung_cancer information system

"""

from Initalization.serever_initalziation_original import *
import pandas as pd


class DataQueries:
    def __init__(self,dbName):
        self.df_sorting_patient = pd.DataFrame()
        self.df_doctor = pd.DataFrame()
        self.cursor, self.con = connect2serverDB(database=dbName)
        self.patients = pd.DataFrame()
        self.doctors = pd.DataFrame()
        self.proceadures = pd.DataFrame()
        self.patients_procedures = pd.DataFrame()
        self.df_busyMonth = pd.DataFrame()
        self.df_proc = pd.DataFrame()
        self.df_patient = pd.DataFrame()

    def queryBusyMonth(self,app):
        self.df_busyMonth = pd.DataFrame()
        self.cursor.execute(f"USE {app.dbName};")
        self.cursor.execute("SELECT month(procedure_date) as Month, count(*) as Number_of_Procedures\n"
                            "FROM patients_procedures \n"
                            "GROUP BY month(procedure_date)\n"
                            "ORDER BY count(*) DESC LIMIT 5;\n")

        self.df_busyMonth = pd.DataFrame(self.cursor.fetchall(), columns=["Month", "Number of procedures"])
        self.df_busyMonth = self.df_busyMonth.reset_index(drop=True)

    def query_most_procedure(self,app):
        self.df_proc = pd.DataFrame()
        self.cursor.execute(f"USE {app.dbName};")
        self.cursor.execute("SELECT(patient_id) as patient_ID , count(patient_id) as Number_of_procedure\n"
                            "FROM patients_procedures \n"
                            "GROUP BY (patient_id)\n"
                            "ORDER BY count(patient_id) DESC LIMIT 5;\n")

        self.df_proc = pd.DataFrame(self.cursor.fetchall(), columns=["patient ID", "Number of procedure"])
        self.df_proc = self.df_proc.reset_index(drop=True)

    def search_patient(self, patient_id,app):
        self.df_patient = pd.DataFrame()
        self.cursor.execute(f"USE {app.dbName};")
        # Assuming that the database connection has already been established
        # elsewhere in the code
        x = str(patient_id)
        sql = "SELECT * FROM patients WHERE patient_id LIKE '%s';" % x
        self.cursor.execute(sql)
        self.df_patient = pd.DataFrame(self.cursor.fetchall(),
                                       columns=['patient_id', 'first_name', 'last_name', 'gender', 'date_of_birth',
                                                'Cities',
                                                'BMI', 'BP_SYS', 'BP_Dia', 'COPD', 'smoking',
                                                'Cardiovascular',
                                                'Tuberculosis', 'Pulmonary_fibrosis', 'sick'])
        self.df_patient = self.df_patient.reset_index(drop=True)

    def search_doctor(self, doctor_id,app):
        self.df_doctor = pd.DataFrame()
        self.cursor.execute(f"USE {app.dbName};")
        x = str(doctor_id)
        sql = "SELECT * FROM doctors WHERE doctor_id LIKE '%s';" % x
        self.cursor.execute(sql)
        self.df_doctor = pd.DataFrame(self.cursor.fetchall(),
                                  columns=["doctor_id", "first_name", "last_name", "start_work_date", "date_of_birth",
                                           "gender"])
        self.df_doctor = self.df_doctor.reset_index(drop=True)


    def sorting_val(self,app, **kwargs):
        # Create an SQL query based on the selected values
        query1 = f"USE {app.dbName};"
        query = "SELECT * FROM patients WHERE 1=1"  # Initial query
        lst = ['date_of_birth', "City", "BMI", "BP_SYS", "BP_Dia"]
        checkbox = ['gender', "date_of_birth_checkbox", "city_checkbox", "bmi_checkbox", "bp_sys_checkbox",
                    "bp_Dia_checkbox", 'COPD', 'smoking', 'Cardiovascular', 'Tuberculosis', 'Pulmonary_fibrosis',
                    'sick']
        for key, value in kwargs.items():
            #     if key =='date_of_birth_checkbox':
            #        pass
            if key in checkbox:
                if value != 'None':
                    if key == 'city_checkbox':
                        val = kwargs.get('Cities')
                        query += f" AND Cities = '{val}'"


                    elif key == 'bmi_checkbox':
                        val = kwargs.get('BMI')
                        query += f" AND BMI > '{val}'"

                    elif key == 'bp_sys_checkbox':
                        val = kwargs.get('BP_SYS')
                        query += f" AND BP_SYS > '{val}'"

                    elif key == 'bp_Dia_checkbox':
                        val = kwargs.get('BP_Dia')
                        query += f" AND BP_Dia > '{val}'"

                    elif key == 'date_of_birth_checkbox':
                        val = kwargs.get('date_of_birth')
                        if kwargs.get('date_of_birth_checkbox2') == 'over':
                            query += f" AND DATEDIFF(date_of_birth, '{val}') > 0"
                        elif kwargs.get('date_of_birth_checkbox2') == 'under':
                            query += f" AND DATEDIFF(date_of_birth, '{val}') < 0"
                        else:
                            val1 = kwargs.get('date_of_birth2')
                            query = query + f" AND date_of_birth BETWEEN '{val}' AND '{val1}'"


                    else:
                        query += f" AND {key} = '{value}'"

        self.cursor.execute(query1)
        self.cursor.execute(query)
        self.df_sorting_patient = pd.DataFrame(self.cursor.fetchall(),
                                  columns=["id", "first_name", "last_name", "gender", "date_of_birth", "Cities",
                                           "BMI",
                                           "BP_SYS", "BP_Dia", "COPD",
                                           "smoking", "Cardiovascular", "Tuberculosis", "Pulmonary_fibrosis",
                                           "sick"])
        self.df_sorting_patient =self.df_sorting_patient.reset_index(drop=True)

    def update_status(self, sick_status, patient_id,app):
        patient_id = str(patient_id)
        try:
            sql = f"UPDATE patients SET sick ={sick_status} WHERE patient_id={patient_id};"
            self.cursor.execute(sql)
            self.con.commit()
            app.views.mssg_box("Success", "Status updated successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to update status.")


