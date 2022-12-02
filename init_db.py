import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="monopoly",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('insert into "game" (gameid, numberofplayers)'
                'values (%s, %s)',
                (2005, 5))

conn.commit()

cur.close()
conn.close()
