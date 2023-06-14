from Initalization.serever_initalziation_original import *

class Insert2DB():
    def __init__(self,views):
        self.dbName = "lung_cancer"
        self.cursor, self.con = connect2serverDB(database=self.dbName)
        self.views = views
        self.index=0

    def get_val(self,w):

        return w.get()

    def InsertPatient(self,app, patient_id, first_name, last_name, gender, date_of_birth, Cities, BMI, BP_SYS, BP_Dia, COPD,
               smoking, Cardiovascular, Tuberculosis, Pulmonary_fibrosis, sick):
        date_of_birth = datetime.strptime(str(date_of_birth), '%Y-%m-%d').strftime('%Y-%m-%d')
        # Assuming that the database connection has already been established
        # elsewhere in the code
        try:
             sql = f"INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
             val = (patient_id, first_name, last_name, gender, date_of_birth, Cities, BMI, BP_SYS, BP_Dia, COPD, smoking,
                  Cardiovascular, Tuberculosis, Pulmonary_fibrosis, sick)
             self.cursor.execute(sql, val)
             self.con.commit()
             app.views.mssg_box("Success", "Patient created successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to create patient.")


    def delete_patient(self,app, patient_id):
        # Assuming that the database connection has already been established
        # elsewhere in the code
        x = str(patient_id)
        try:
            sql = "DELETE FROM patients WHERE patient_id='%s';" % x
            self.cursor.execute(sql)
            self.con.commit()
            app.views.mssg_box("Success", "Patient removed successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to remove patient.")

    def InsertDoctor(self,app, doctor_id, first_name, last_name, start_work_date, date_of_birth, gender):
        # Assuming that the database connection has already been established
        # elsewhere in the code
        date_of_birth = datetime.strptime(str(date_of_birth), '%Y-%m-%d').strftime('%Y-%m-%d')
        start_work_date = datetime.strptime(str(start_work_date), '%Y-%m-%d').strftime('%Y-%m-%d')
        try:
            sql = f"INSERT INTO doctors VALUES (%s, %s, %s, %s, %s, %s)"
            val = (doctor_id, first_name, last_name, start_work_date, date_of_birth, gender)
            self.cursor.execute(sql, val)
            self.con.commit()
            app.views.mssg_box("Success", "Doctor created successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to create doctor.")


    def delete_doctor(self,app, doctor_id):
        # Assuming that the database connection has already been established
        # elsewhere in the code
        x = str(doctor_id)
        try:
            sql = "DELETE FROM doctors WHERE doctor_id='%s';" % x
            self.cursor.execute(sql)
            self.con.commit()
            app.views.mssg_box("Success", "Doctor removed successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to remove doctor.")

    def InsertPrecedure(self,app, patient_id, doctor_id, id_procedure, procedure_date, sick):
        procedure_date = datetime.strptime(str(procedure_date), '%Y-%m-%d').strftime('%Y-%m-%d')
        patient_id=str(patient_id)
        doctor_id=str(doctor_id)
        id_procedure=str(id_procedure)
        sick=str(sick)
        try:
            sql = f"INSERT INTO patients_procedures VALUES (%s, %s, %s, %s, %s)"
            val = (patient_id, doctor_id, id_procedure, procedure_date, sick)
            self.cursor.execute(sql, val)
            self.con.commit()
            app.views.mssg_box("Success", "Procedure created successfully.")
        except:
            app.views.mssg_box("Failed", "Failed to create procedure.")