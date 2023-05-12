"""
Omer ,Doron, Yuval lung_cancer information system
"""
import pandas as pd
import random
#import numpy as np

files = ['real_doctors.csv', 'patienet_new.csv', 'patients_procedures.csv', 'procedures_new.csv']
patient = pd.read_csv("patienet_new.csv")
procedures = pd.read_csv("procedures_new.csv")
patients_procedures = pd.read_csv("patients_procedures.csv")
doctors = pd.read_csv("real_doctors.csv")

cities = ["Jerusalem", "Tel Aviv-Yafo", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod", "Netanya", "Be'er Sheva",
          "Holon", "Bnei Brak"]
kibbutzim = ["Kibbutz Beit HaEmek", "Kibbutz Ein Gev", "Kibbutz Ein Harod", "Kibbutz Givat Brenner",
             "Kibbutz Ma'agan Michael", "Kibbutz Nahsholim", "Kibbutz Sde Boker", "Kibbutz Sde Eliyahu",
             "Kibbutz Sde Nahum", "Kibbutz Yotvata"]
names_mens = ["Noam", "Yosef", "David", "Eitan", "Daniel", "Moshe", "Avi", "Avraham", "Shlomo", "Yitzhak", "Yehuda",
              "Yitzchak", "Netanel", "Shmuel", "Dov", "Yigal", "Amir", "Shimon", "Omer", "Eli", "Meir", "Yehoshua",
              "Aviad", "Yair", "Reuven", "Yisrael", "Binyamin", "Yaakov", "Gershon", "Mordechai", "Natan", "Itai",
              "Yaniv",
              "Nir", "Uri", "Nadav", "Gadi", "Haim", "Yoni", "Zvi", "Shai", "Menachem", "Ariel", "Zohar", "Hillel",
              "Aharon",
              "Yotam", "Eran", "Doron", "Zeev"]
names_womens = ["Tamar", "Leah", "Avigail", "Adi", "Shira", "Liora", "Noa", "Michal", "Rivka", "Ruth", "Yael",
                "Malka", "Noga", "Chana", "Yifat", "Maya", "Galit", "Hila", "Rachel", "Nurit", "Dafna", "Gali",
                "Tali", "Sigal", "Shaked", "Keren", "Orly", "Batya", "Lilach", "Tzipora", "Orit", "Nira",
                "Gila", "Yiska", "Miri", "Hagit", "Dalit", "Hodaya", "Einat", "Yifat", "Hadar", "Efrat", "Dana",
                "Limor", "Yonit", "Dikla", "Natalie", "Anat", "Neta", "Eden", "Tova"]
israeli_last_names = ['Cohen', 'Levi', 'Mizrachi', 'Peretz', 'Biton', 'Avraham', 'Alouf', 'Shoshan', 'Amir', 'Shitrit',
                      'Efrati', 'Hasson', 'Azoulay', 'Ohana', 'Amsalem', 'Kadosh', 'Kahlon', 'Timsit', 'Sason',
                      'Sarusi', 'Yosef', 'Sabbag', 'Shamama', 'Elbaz', 'Dayan', 'Nissan', 'Dahan', 'Yehudai', 'Shabi',
                      'Gavriel', 'Zrihan', 'Abuhatzira', 'Saidoff', 'Moyal', 'Ohayon', 'Amram', 'Biran', 'Basson',
                      'Elmaliah', 'Alfasi', 'Yehuda', 'Sabag', 'Ayalon', 'Saada', 'Shiloni', 'Kahana', 'Malka', 'Yaron',
                      'Kaslassi', 'Bokobza', 'Kasirer', 'Golan', 'Carmeli', 'Yerushalmi', 'Lavie', 'Shemesh', 'Sharabi',
                      'Darmon', 'Salomon', 'Hakim', 'Kamisa', 'Gross', 'Rosenberg', 'Asulin', 'Marom', 'Kfir',
                      'Davidov', 'Yishai', 'Sulimani', 'Kohn', 'Huri', 'Eliyahu', 'Kaplan', 'Khalifa', 'Lerner']
# removing spaces from cities names
for i, city in enumerate(cities):
    cities[i] = city.replace(" ", "_")
# assigning to patients cities and kibbutz randomly
for i in range(0, 850):
    patient.iloc[i, 5] = random.choice(cities)
for i in range(850, 1000):
    patient.iloc[i, 5] = random.choice(kibbutzim)
# assigning to patients israeli names,id,gender  randomly to patients and doctors
for i in range(0, 1000):
    if i % 2 == 0:
        patient.iloc[i, 0] = random.randint(200000000, 399999999)
        patient.iloc[i, 1] = random.choice(names_mens)
        patient.iloc[i, 2] = random.choice(israeli_last_names)
        patient.iloc[i, 3] = "male"
        if i < 10:
            doctors.iloc[i, 0] = random.randint(200000000, 399999999)
            doctors.iloc[i, 1] = random.choice(names_mens)
            doctors.iloc[i, 2] = random.choice(israeli_last_names)
            doctors.iloc[i, 5] = "male"
    elif i % 2 != 0:
        patient.iloc[i, 0] = random.randint(200000000, 399999999)
        patient.iloc[i, 1] = random.choice(names_womens)
        patient.iloc[i, 2] = random.choice(israeli_last_names)
        patient.iloc[i, 3] = "female"
        if i < 10:
            doctors.iloc[i, 0] = random.randint(200000000, 399999999)
            doctors.iloc[i, 1] = random.choice(names_womens)
            doctors.iloc[i, 2] = random.choice(israeli_last_names)
            doctors.iloc[i, 5] = "female"
for i in range(0, 1000):
    patients_procedures.iloc[i, 1] = random.choice(doctors.iloc[:, 0].tolist())
# getting the id's list of the sick people and assign them to patient_procedures table
sick_id = patient.loc[patient['sick'] == 1, 'patient_id'].tolist()
#print(sick_id)
# assign the id of the sick patient to treatments log
for i in range(0, 1000):
    patients_procedures.iloc[i, 0] = random.choice(sick_id)
# make sure that patient that do tumor removal does not make it a lot of times
patients_procedures['id_procedure'].replace(4, 3)
sessions_per_patient = patients_procedures.groupby('patient_id')['id_procedure'].nunique()
single_session_patients = sessions_per_patient[sessions_per_patient == 1].index
patients_procedures.loc[patients_procedures['patient_id'].isin(single_session_patients), 'id_procedure'] = '4'
#print(doctors)
print(patients_procedures.head(10))
# print(patients_procedures.head(20))
# print(patients_procedures.iloc[:, 0:3].tail(100))
doctors.to_csv(r'C:\Users\user\PycharmProjects\python_medical_information system\real_doctors.csv', index=False)
patients_procedures.to_csv(r'C:\Users\user\PycharmProjects\python_medical_information system\patient_procedures.csv',
                           index=False)
patient.to_csv(r'C:\Users\user\PycharmProjects\python_medical_information system\patient_new.csv.', index=False)
print(doctors.iloc[:, 0])