import pandas as pd
import sqlite3

#loading existing files

df_attendance=pd.read_csv('attendance_logs.csv')
df_students=pd.read_csv('students.csv')

#creating connection

conn=sqlite3.connect('sql_data.db')
#pushing tables into sql 
df_attendance.to_sql('attendance', conn,if_exists='replace',index=False)
df_students.to_sql('students', conn,if_exists='replace',index=False)

#closing connection
conn.close()

print("SUCCESS! SQL Database 'school_data.db' has been created.")