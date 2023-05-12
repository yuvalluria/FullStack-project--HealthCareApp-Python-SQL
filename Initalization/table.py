import pandas as pd
from datetime import datetime
import numpy as np

class Table:
    def __init__(self,tableName,csvFileName, pks = [], fks = [], ref_tables = [], refs = []):
        # allocate all relational tableName attributes from csvFile
        self.headers = []
        self.csvFileName = csvFileName
        self.tableName = tableName
        self.data = pd.DataFrame()
        self.pks = pks
        self.fks = fks
        self.ref_tables = ref_tables
        self.refs = refs
        try:
            # read csv file into table variable
            self.data = pd.read_csv(self.csvFileName)
            print(self.data)
            self.headers = self.data.columns.values
        except FileNotFoundError:
            print("incorrect file name")
        except:
            print("table importing went wrong")
        finally:
            # convert time-stamp format to mysql readable one
            if "Timestamp" in self.data.columns:
                for i in range(self.data.shape[0]):
                    self.data.loc[i,"Timestamp"] = datetime.strptime(self.data.loc[i,"Timestamp"][:-6], '%Y/%m/%d %I:%M:%S %p')
            if "DateTime" in self.data.columns:
                for i in range(self.data.shape[0]):
                    print(self.data.loc[i,"DateTime"])
                    self.data.loc[i,"DateTime"] = datetime.strptime(self.data.loc[i,"DateTime"], '%m/%d/%Y %H:%M')
            for i in self.data.columns:
                if 'Date' in i:
                    for j in range(self.data.shape[0]):
                        if isinstance(self.data.loc[j, i],str) :
                            self.data.loc[j, i] = datetime.strptime(self.data.loc[j, i],'%m/%d/%Y').strftime("%Y-%m-%d")

            # convert np.nan's to nones
            self.data = self.data.where(pd.notnull(self.data),None)
        return
