

import pandas as pd
import mysql.connector

class PatientModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )

    def get_patients(self):
        # Retrieve all patients from the database
        query = "SELECT * FROM your_table_name"
        patients_df = pd.read_sql(query, self.conn)
        return patients_df

    def filter_patients(self, selected_columns):
        # Retrieve the selected columns
        query = "SELECT " + ", ".join(selected_columns) + " FROM your_table_name"
        filtered_df = pd.read_sql(query, self.conn)
        return filtered_df

    def close_connection(self):
        self.conn.close()

class PatientQueries:
    def __init__(self, model):
        self.model = model
        self.patients_df = None

    def load_patients(self):
        # Load the patients DataFrame
        self.patients_df = self.model.get_patients()

    def filter_patients(self, selected_columns):
        # Filter the patients DataFrame using the selected columns
        filtered_df = self.model.filter_patients(selected_columns)
        return filtered_df

    def close_connection(self):
        self.model.close_connection()

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
