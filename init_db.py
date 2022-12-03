import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        port='8888',
        database="monopoly",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table

# Insert data into the table


conn.commit()

cur.close()
conn.close()