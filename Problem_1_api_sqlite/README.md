# Problem 1 – API Data Retrieval and Storage

## Objective
Fetch book data from an external REST API, store it in a local SQLite database, and display the retrieved records.

---

## Approach
A Python script was implemented to integrate an external REST API with a local SQLite database for storing and retrieving book information. The Open Library Search API was used to fetch book data based on multiple subject keywords such as **science**, **math**, **computer**, and **poetry**.

For each subject, an HTTP GET request was made, and the JSON response was parsed to extract relevant fields including **book title**, **author name**, and **first publication year**. Since the API returns author information as a list, multiple author names were combined into a single comma-separated string before storing the data.

A local SQLite database was created using the `sqlite3` module, and a table was defined to store the book records. The cleaned data from the API responses was inserted into the database row by row. After insertion, a `SELECT` query was executed to retrieve and display sample records, verifying that the data was stored successfully.

While processing the API responses, it was observed that some records contained incomplete metadata, which required basic validation before insertion into the database.

---

## Assumptions
- A public REST API (Open Library) was used since no proprietary book dataset was provided.
- Subject-based queries were used to organize and limit the API results.
- Some API records may contain missing fields; in such cases, missing author information was stored as **"unknown"**.
- Multiple authors for a single book were combined into a single string for simplicity.
- The publication year was assumed to be represented by the `first_publish_year` field from the API.
- The SQLite database was stored locally for ease of setup and demonstration.

---

## Result
Book records were successfully fetched from the external API, stored in the SQLite database, and retrieved using SQL queries to confirm correct insertion.




### Architecture
```
problem1_api_sqlite/
├── src/
│   └── fetch_books.py
└── data/
    └── books_details.db
```
