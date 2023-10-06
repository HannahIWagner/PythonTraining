import pyodbc
connectionString = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'
sqlStr="""CREATE TABLE Student (
    StudentID int NOT NULL,
    FirstName nvarchar(40) NOT NULL,
    Surname nvarchar(30) NULL,
    Course nvarchar(30) NULL,
    City nvarchar(15) NULL)"""

insert_command = """INSERT INTO Student
VALUES (123, 'Jessica', 'Jones', 'Law', 'London')"""

updates = """UPDATE Student
SET StudentID = 124, City = 'Lincoln'"""
conn = pyodbc.connect(connectionString)
cur=conn.cursor()
#cur.execute(sqlStr)
#cur.execute(insert_command)
cur.execute(updates)
conn.commit()
conn.close()
