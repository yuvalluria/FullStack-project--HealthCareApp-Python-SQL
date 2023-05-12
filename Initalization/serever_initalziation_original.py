from Initalization.table import *
# from table import Table
from sqlalchemy import create_engine
import mysql.connector
import pymysql


user = ""
passward = ""
ip = '127.0.0.1'
port = 3306
host = "localhost"
db = ""
tables = []
cursor = ""
con = ""


# Create Connection, save user, password into privates
def connect2server(usr="root", passwd="12345", hst="localhost", prt=3306):
    global user, passward, host, port, cursor, con
    user = usr
    passward = passwd
    host = hst
    port = prt
    con = mysql.connector.connect(host=host, user=user, passwd=passward)
    cursor = con.cursor()
    return cursor


def showDBs():
    global cursor
    cursor.execute("SHOW DATABASES")
    print("Databases in server:")
    for x in cursor:
        print(x)
    return


def initDB(dbname):
    # this function enables communication with existing server
    # and initiation of a new DB
    global db, cursor
    db = dbname
    print(db)
    print(f"drop database if exists {db.lower()}")
    cursor.execute(f"drop database if exists {db.lower()}")
    # create a new database
    cursor.execute(f"CREATE DATABASE {db.upper()}")
    # showing that the database has been created
    showDBs()
    return


def connect2serverDB(database=db):
    # this function assumes existing connection to server
    # provided global connection specifications
    # and an existing DB.
    # it outputs the connection cursor to the db
    connect2server()
    global user, passward, host, port, cursor, db, con
    db = database
    # reconnect to database from server
    con = mysql.connector.connect(host=host,
                                  user=user,
                                  passwd=passward,
                                  database=db.upper())
    cursor = con.cursor()
    return cursor, con


def showTables():
    # this function assumes existing connection cursor to server DB
    global cursor
    cursor.execute("show tables")
    print(f"Tables in DB:")
    for i in cursor:
        print(i)


def createNewTable(table, headers=[], dbname=db):
    global db, cursor
    if dbname != db:
        connect2serverDB(dbname)
    if len(headers) == 0:
        headers = table.headers
    print(table.tableName.lower())
    cursor.execute(f"use {db}")
    cursor.execute(f"drop table if exists {table.tableName.lower()}")
    tbl_ftrs = f"CREATE TABLE {table.tableName.lower()} ("
    for i, k in enumerate(headers):  # [1:]:
        if i == 0:
            if "Timestamp" in k:
                tbl_ftrs += f"{k} TIMESTAMP"
            elif "DateTime" in k:
                tbl_ftrs += f"{k} DATETIME"
            elif "Date" in k:
                tbl_ftrs += f"{k} DATE"
            else:
                tbl_ftrs += f"{k} VARCHAR(255)"
        else:
            if "Timestamp" in k:
                tbl_ftrs += f", {k} TIMESTAMP"
            elif "Date" in k:
                tbl_ftrs += f", {k} DATE"
            else:
                tbl_ftrs += f", {k} VARCHAR(255)"
    tbl_ftrs += f")"
    print(tbl_ftrs)
    cursor.execute(tbl_ftrs)
    return


def insertData2Table(table):
    global user, passward, ip, port, db
    con = create_engine('mysql+pymysql://' + user + ':' + passward + '@' + ip + ':' + str(port) + '/' + db)
    table.data.to_sql(name=table.tableName.lower(), con=con, index=False, if_exists="append")
    return


def addPKs(table):
    global cursor, db
    # re-initiate cursor
    connect2serverDB(database=db)
    lst = table.pks
    # lst=list(getattr(table,'pks'))
    if len(lst) == 1:
        alter_table_com = f"ALTER TABLE {table.tableName.lower()} " \
                          f"ADD PRIMARY KEY ({lst[0]})"
        print(alter_table_com)
        cursor.execute(alter_table_com)
    elif len(lst) > 1:
        alter_table_com = f"ALTER TABLE {table.tableName.lower()} ADD PRIMARY KEY ("
        for j in lst[:-1]:
            alter_table_com += f"{j},"
        alter_table_com += f"{lst[-1]})"
        print(alter_table_com)
        cursor.execute(alter_table_com)


def addFKs(table):
    global cursor, db
    # re-initiate cursor
    connect2serverDB(database=db)
    for i, t in enumerate(table.ref_tables):
        if len(table.fks[i]) == 1:
            alter_table_com = f"ALTER TABLE {table.tableName.lower()} " \
                              f"ADD FOREIGN KEY ({table.fks[i][0]}) " \
                              f"REFERENCES {t}({table.refs[i][0]})"
            print(alter_table_com)
            cursor.execute(alter_table_com)
        elif len(table.fks[i]) > 1:
            alter_table_com = f"ALTER TABLE {table.tableName.lower()} " \
                              f"ADD FOREIGN KEY ("
            for j in range(len(table.fks[i]) - 1):
                alter_table_com += f"{table.fks[i][j]}, "
            alter_table_com += f"{table.fks[i][-1]}) REFERENCES {t}( "
            for j in range(len(table.refs[i]) - 1):
                alter_table_com += f"{table.refs[i][j]}, "
            alter_table_com += f"{table.refs[i][-1]})"
            print(alter_table_com)
            cursor.execute(alter_table_com)


# main execution from here:
# form a connection to server
def main():
    connect2server(usr='root', passwd='12345', hst="localhost", prt=3306)
    # initiate a database
    initDB("lung_cancer")
    # read csv file into table object
    tables = [Table("Doctors", "real_doctors.csv", pks=["doctor_id"]),
              Table("Patients", "patient_new.csv", pks=["patient_id"]),
              Table("proceadures", "procedures_new.csv", pks=["id_procedure"]),
              Table("patients_procedures", "patient_procedures.csv",
                    pks=["patient_id", "procedure_date", "id_procedure"],
                    fks=[["patient_id"], ["doctor_id"], ["id_procedure"]],
                    ref_tables=["Patients", "Doctors", "proceadures"],
                    refs=[["patient_id"], ["doctor_id"], ["id_procedure"]])]

    for t in tables:
        # create sql-table that corresponds to table object
        createNewTable(t, dbname="lung_cancer")
        # showTables()
        # inject table data into corresponding sql table
        insertData2Table(t)
        # add primary keys to table
        addPKs(t)
        # add foreign keys to table (make sure they're in order of appearance)
        addFKs(t)


if __name__ == "__main__":
    main()
