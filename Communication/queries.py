# -- coding: utf-8 --
"""
Omer ,Doron, Yuval lung_cancer information system

"""
dbName = "lung_cancer"
from serever_initalziation_original import *
import pandas as pd
from datetime import datetime


class DataQueries:
    def __init__(self, dbName):
        self.cursor = connect2server()
        self.cursor, self.con = connect2serverDB(database=dbName)
        self.patients = pd.DataFrame()
        self.doctors = pd.DataFrame()
        self.proceadures = pd.DataFrame()
        self.patients_procedures = pd.DataFrame()

    def queryBusyMonth(self):
        global dbName
        connect2serverDB(database=dbName)
        self.cursor.execute(f"USE {dbName};")
        self.cursor.execute("SELECT month(procedure_date), count(*)\n"
                            "FROM patients_procedures \n"
                            "GROUP BY month(procedure_date)\n"
                            "ORDER BY count(*) DESC LIMIT 5;\n")

        df_busyMonth = pd.DataFrame(self.cursor.fetchall(), columns=["month(procedure_date)", "count(*)"])
        return df_busyMonth

    def query_most_procedure(self):
        global dbName
        connect2serverDB(database=dbName)
        self.cursor.execute(f"USE {dbName};")
        self.cursor.execute("SELECT(patient_id), count(patient_id)\n"
                            "FROM patients_procedures \n"
                            "GROUP BY (patient_id)\n"
                            "ORDER BY count(patient_id) DESC LIMIT 5;\n")

        df_proc = pd.DataFrame(self.cursor.fetchall(), columns=["patient_id", "num_of_procedure"])
        return df_proc

    def querySuccessRate(self):
        global dbName
        connect2serverDB(database=dbName)
        self.cursor.execute(f"USE {dbName};")
        self.cursor.execute("SELECT p.sick,\
        COUNT(*) AS total_procedures,ROUND(count(*) * 100.0 / sum(count(*)) over()) AS success_rate\
        FROM patients_procedures AS pp\
        JOIN patients AS p ON pp.patient_id = p.patient_id\
        WHERE pp.id_procedure= '3'\
        GROUP BY p.sick,\
        pp.id_procedure")
        res2 = self.cursor.fetchall()
        df_success_chemo = pd.DataFrame(res2, columns=["sick", "total_procedures", "success_rate"])
        return df_success_chemo

    def Insert(self, patient_id, first_name, last_name, gender, date_of_birth, Cities, BMI, BP_SYS, BP_Dia, COPD,
               smoking, hereditary_retinoblastoma, Tuberculosis, Pulmonary_fibrosis, sick):
        global dbName
        date_of_birth = datetime.strptime(str(date_of_birth), '%Y-%m-%d').strftime('%Y-%m-%d')
        # Assuming that the database connection has already been established
        # elsewhere in the code
        sql = f"INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (patient_id, first_name, last_name, gender,   date_of_birth, Cities, BMI, BP_SYS, BP_Dia, COPD, smoking,
               hereditary_retinoblastoma, Tuberculosis, Pulmonary_fibrosis, sick)
        self.cursor.execute(sql, val)
        self.con.commit()

    def InsertDoctor(self, doctor_id,first_name,last_name,start_work_date,date_of_birth,gender):
        global dbName
        # Assuming that the database connection has already been established
        # elsewhere in the code
        date_of_birth = datetime.strptime(str(date_of_birth), '%d-%m-%Y').strftime('%Y-%m-%d')
        start_work_date = datetime.strptime(str(start_work_date), '%d-%m-%Y').strftime('%Y-%m-%d')
        sql = f"INSERT INTO doctors VALUES (%s, %s, %s, %s, %s, %s)"
        val = (doctor_id,first_name,last_name,start_work_date,  date_of_birth,gender)
        self.cursor.execute(sql, val)
        self.con.commit()

def main():
    q = DataQueries('lung_cancer')
    print(q.queryBusyMonth())
    print(q.querySuccessRate())
    print(q.query_most_procedure())
    #q.Insert(1345, 'Eli', 'Khalifa', 'male', '1987-10-10', 'Haifa', 15, 104, 58, 0, 0, 0, 0, 0, 0)
 #   q.InsertDoctor(12345, 'dr','yuvk', '11-10-1987', '11-10-2000', 'male')


if __name__ == "__main__":
    main()
