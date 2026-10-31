# Automated Attendance & Early Warning Dropout Pipeline

## Project Overview

A Python and SQL-based ETL pipeline designed to monitor student attendance and identify potential absenteeism risks in Tunisian public schools.

The pipeline processes student and attendance data from CSV files, stores the data in a SQLite database, calculates absence percentages over a rolling 30-day period, classifies students by risk level, and generates a formatted Excel report.

## Business Problem

In many public schools, attendance is recorded manually using paper registers and absence slips. Identifying students with recurring absences can be time-consuming, especially when records need to be consolidated manually.

This project aims to simplify the process by automating attendance analysis and providing school administrators with a report highlighting students who may require follow-up.

## Technologies Used

- **Python:** Pipeline development and data processing
- **Pandas:** CSV ingestion and SQL query results processing
- **SQLite:** Data storage and SQL transformations
- **SQL:** Data joining, filtering, aggregation and risk classification
- **Openpyxl:** Excel report generation and formatting
- **Windows Batch:** Pipeline execution automation
- **Windows Task Scheduler:** Scheduled execution

## Pipeline Workflow

### 1. Data Ingestion

The pipeline reads two CSV files:

- `students.csv`: Student information.
- `attendance_logs.csv`: Student attendance records.

The data is loaded into a SQLite database (`sql_data.db`) containing two tables: `students` and `attendance`.

### 2. Data Transformation

SQL queries are used to:

- Join student information with attendance records.
- Filter attendance records within the last 30 days.
- Calculate the total number of attendance sessions.
- Count student absences.
- Calculate absence percentages.
- Assign risk levels using conditional logic.

### 3. Risk Classification

Students are classified into three risk categories based on their absence percentages:

| Absence Percentage | Risk Level |
|---|---|
| Below 10% | Low |
| 10% to below 20% | Medium |
| 20% or higher | High |

These thresholds are project-defined rules for identifying attendance patterns that may require attention.

### 4. Report Generation

Python retrieves the SQL query results using Pandas and exports them to an Excel file.

The report includes:

- Student ID
- Gender
- Class ID
- Total attendance sessions
- Total absences
- Absence percentage
- Risk level

The Excel report is formatted using Openpyxl to improve readability.

## Project Structure

```text
Automated-Attendance-Pipeline/
│
├── data/
│   ├── students.csv
│   └── attendance_logs.csv
│
├── setup_db.py
├── pipeline.py
├── run_pipeline.bat
├── sql_data.db
├── Risk_Warning_Report.xlsx
└── README.md
