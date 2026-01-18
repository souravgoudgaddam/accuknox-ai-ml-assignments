#importing required libraries
import requests,sqlite3

#creating a database to store book details
connection=sqlite3.connect('data/books_details.db')
#creating a cursor object to excute below query
cursor=connection.cursor()

#creating a table for book deatils in database
cursor.execute(""" CREATE TABLE IF NOT EXISTS BOOKS(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               TITLE TEXT,
               AUTHOR TEXT,
               PUBLICATION_YEAR INTEGER)
""")

connection.commit()

list_subjects=['science','math','computer','poetry']
for subject in list_subjects:
        

        #fetching api data
        response=requests.get(f'https://openlibrary.org/search.json?q={subject}&fields=title,author_name,first_publish_year')

        if response.status_code==200:
                data=response.json().get('docs',[])
                for book in data:
                        #cleaning the messy data
                        author=book.get('author_name',[])
                        author=','.join(author) if author else 'unknown'
                        publication_year=book.get('first_publish_year')
                        title=book.get('title')

                        #inserting data into books table that exisits in books_details database
                        cursor.execute('INSERT INTO BOOKS(TITLE,AUTHOR,PUBLICATION_YEAR) VALUES (?,?,?) ',(title,author,publication_year))
                       
        else:
                print(f'failed API call:{subject}')

connection.commit()

##Retrieve list of books from database
print("\list of  books retrieved from database:\n")

cursor.execute("SELECT TITLE, AUTHOR, PUBLICATION_YEAR FROM BOOKS LIMIT 11")

for record in cursor.fetchall():
        print(record)

#closing connection         
connection.close()

        
        