import pandas as pd
import tkinter as tk
from time import gmtime, strftime

from Initalization.serever_initalziation_original import *


class Insert2DB():
    def _init_(self, app):
        self.cols = ["DateTime", "PatientID", "PatientFirstName", \
                     "PatientLastName", "Diagnosis", "DrugSensitivity", \
                     "Antigen"]
        self.df = pd.DataFrame(columns=self.cols, dtype=str)
        self.tableName = 'vaccines'
        self.dbName = "emr"
        self.cursor = connect2server()
        self.cursor, self.con = connect2serverDB(database=self.dbName)
        self.index = 0
        self.table_init()
        self.views = app


def table_init(self):
    self.cursor.execute(f"SHOW TABLES LIKE '{self.tableName}'")
    temp = False
    for i in self.cursor:
        if "vaccines" in i:
            temp = True
            break
    if not temp:
     self.vaccines = Table("vaccines", None, pks=["PatientID", "DateTime"],
                          ref_tables=["patients"],
                          refs=[["patientID"]])
    print(self.vaccines.headers)
    createNewTable(self.vaccines, headers=self.cols, dbname=self.dbName)
    print("vaccines table created")
    insertData2Table(self.vaccines)
    addPKs(self.vaccines)
    addFKs(self.vaccines)
    return


def get_val(self, w):
    if isinstance(w, tk.Text):
        return w.get("1.0", 'end-1c')
    else:
        return w.get()


def set_val(self, w, col):
    # important notice - here you can add constrains
    # or raise error-alerts if needed
    # for example - test your input type
    if col == "PatientID":
        if not self.get_val(w).isnumeric():
            self.views.frame1.ID_error()
            return


#   elif col=="Diagnosis":
#      temp = self.get_val(w)
#     if len(temp):
#        temp = temp.split(',')
#       self.df.loc[self.index,col] = temp
#     else:
#        self.views.frame1.clear_ID_error()

#   if self.get_val(w) or self.get_val(w)==0:
#      self.df.loc[self.index,col] = self.get_val(w)
#     print(self.df.loc[self.index,col])
# else:
#   self.df.loc[self.index, col] = None
# return
def refreshDBvals(self):
    # refresh db values to current in views
    #     self.df.loc[self.index,"DateTime"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    self.set_val(self.views.frame1.PatientIDEntry, "patientid")


#     self.set_val(self.views.frame1.PatientFirstNameEntry,"PatientFirstName")
#    self.set_val(self.views.frame1.PatientLastNameEntry,"PatientLastName")
#   self.set_val(self.views.frame2.diag,"Diagnosis")
#  self.set_val(self.views.frame2.rb_yes_var,"DrugSensitivity")
# self.set_val(self.views.frame2.comboAnt,"Antigen")

def insertData2Table(self):
    self.refreshDBvals()
    print(self.df)
    # add df as a new line to db
    command = f"INSERT INTO {self.tableName} ("
    for c in self.cols[:-1]:
        command += f"{c}, "
    command += f"{self.cols[-1]}) VALUES ("
    for v in self.df.iloc[self.index, :-1]:
        if v == None:
            command += f"NULL, "
        else:
            command += f"'{v}', "
    if self.df.iloc[self.index, -1] == None:
        command += f"'NULL')"
    else:
        command += f"'{self.df.iloc[self.index, -1]}')"
    print(command)
    self.cursor.execute(command)
    self.con.commit()
    return


def controlButton(self):
    # insert dataframe to sql table
    self.insertData2Table()
    fname = 'C://Hadas//courses//2023//Healthcare Informatics//app//FrontEnd//vaccines.csv'
    try:
        with open(fname, 'r') as f:
            f.close()
            self.df.to_csv(fname, sep=",", header=False, \
                           line_terminator="", index=False, mode='a')
    except FileNotFoundError:
        self.df.to_csv(fname, sep=",", header=True, \
                       line_terminator="", index=False)
    # update line index
    # self.index+=1
    print(self.df)
    self.views.destroy()
    return True
