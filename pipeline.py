import pandas as pd
import sqlite3 
#use openpyxl to make it presentable 
from openpyxl import load_workbook
from openpyxl.styles import Font 

#connect to database 
conn=sqlite3.connect('sql_data.db')
#sql query

query= """
SELECT
    student_report.*,

    CASE
        WHEN absence_percentage >= 20 THEN 'High'
        WHEN absence_percentage >= 10 THEN 'Medium'
        ELSE 'Low'
    END AS risk_level

FROM (

    SELECT
        s.student_id,
        s.gender,
        s.class_id,

        COUNT(a.date) AS total_sessions,

        COUNT(
            CASE
                WHEN LOWER(TRIM(a.status)) = 'absent'
                THEN 1
            END
        ) AS total_absences,

        ROUND(
            COUNT(
                CASE
                    WHEN LOWER(TRIM(a.status)) = 'absent'
                    THEN 1
                END
            ) * 100.0 / COUNT(a.date),
            2
        ) AS absence_percentage

    FROM students s

    JOIN attendance a
        ON TRIM(s.student_id) = TRIM(a.student_id)

    WHERE a.date >= date('now', '-30 days')
      AND a.date <= date('now')

    GROUP BY
        s.student_id,
        s.gender,
        s.class_id

) AS student_report

ORDER BY absence_percentage DESC;   
"""

#excute and load into pandas,
at_risk_students = pd.read_sql_query(query, conn)

conn.close()


print("--top students with highest absence rate")
print(at_risk_students.head(10))

#export to excel
at_risk_students.to_excel('Risk_Warning_Report.xlsx',index=False)

#format the excel 
workbook= load_workbook('Risk_Warning_Report.xlsx')

sheet=workbook.active
bold_font=Font(bold=True)

for cell in sheet [1:1]:
    cell.font= bold_font

# Target Column A and set its physical width to 15 so the 'student_id' text fits without squishing.
sheet.column_dimensions['A'].width = 15

# Target Column B and set its width to 15 so 'total_absences' fits cleanly.
sheet.column_dimensions['B'].width = 15

# Target Column C and set its width to 12 for the 'class_id'.
sheet.column_dimensions['C'].width = 12

# Target Column D and set its width to 10 for the 'gender'.
sheet.column_dimensions['D'].width = 10

workbook.save('Risk_Warning_Report.xlsx') 

print("\nSUCCESS! Formatting applied. Open your Excel file to see the bold headers and wider columns.")





