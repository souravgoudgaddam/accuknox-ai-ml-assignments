# Problem 3 – CSV Data Import to a Database

## Objective
Read user information from a CSV file using Python and store the data in a local SQLite database. This task demonstrates how structured data can be imported, validated, and persisted into a relational database for further querying and analysis.

---

## Approach
A Python script was developed to read Netflix user data from a CSV file and store it in a local SQLite database. The CSV file was loaded using the **Pandas** library, and a database table was created to store the user information.

Each record from the CSV file was inserted into the database row by row using SQL insert statements. After inserting the data, a sample of records was retrieved from the database using a `SELECT` query to verify that the data was successfully stored.

---

## Assumptions
- The CSV file contains clean and consistent user data.
- Column names in the CSV file align with the database table schema.
- Date values are stored in the database as they appear in the CSV file.
- A local SQLite database is sufficient for this task.
- Data is inserted row by row for simplicity and clarity.

---

## Result
The Netflix user data from the CSV file was successfully inserted into the SQLite database. Sample records were retrieved from the database to confirm that the data was stored correctly.

### Architecture
```
problem3_csv_sqlite/
├── src/
│   └── users_info.py
├── Data/
│   ├── users.csv
│   └── netflix_users.db
└── README.md

```
