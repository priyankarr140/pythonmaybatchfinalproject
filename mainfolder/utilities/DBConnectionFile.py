import mysql.connector

class DBConnectionFile:
    def dbconnect(self):
        conn=mysql.connector.connect(host="localhost",
        user="root",password="123456",database="pythonmaybatch")
        mycursor=conn.cursor()
        mycursor.execute("select * from project")
        data=mycursor.fetchall()
        return data