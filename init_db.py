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
cur.execute('DROP TABLE IF EXISTS "user" CASCADE;')
cur.execute('CREATE TABLE "user" (userid INTEGER UNIQUE,'
                                 'name TEXT NOT NULL,'
                                 'gamesplayed INTEGER,'
                                 'gameswon INTEGER,'
                                 'PRIMARY KEY (userid));'
                                 )

cur.execute('DROP TABLE IF EXISTS "game" CASCADE;')
cur.execute('CREATE TABLE "game" (gameid INTEGER UNIQUE,'
                                 'numberofplayers INTEGER,'
                                 'winnerid INTEGER,'
                                 'FOREIGN KEY (winnerid)'
                                 	'REFERENCES "user"(userid),'
                                 'PRIMARY KEY (gameid));'                               
                                 )                               
                                
cur.execute('DROP TABLE IF EXISTS "played" CASCADE;')
cur.execute('CREATE TABLE "played" (userid INTEGER,'
                                 'gameid INTEGER,'
                                 'money INTEGER,'
                                 'streetsowned TEXT,'
                                 'railroadsowned TEXT,'
                                 'utilitiesowned TEXT,'
                                 'numproperties INTEGER,'
                                 'PRIMARY KEY (userid, gameid),'
                         	 'FOREIGN KEY (userid) '
                         		'REFERENCES "user"(userid) ' 
                         		'ON DELETE CASCADE, '
                         	 'FOREIGN KEY (gameid)'
                         		'REFERENCES "game"(gameid)' 
                         		'ON DELETE CASCADE);'
                                 )
                           

# Insert data into the table
cur.execute('INSERT INTO "user" VALUES (%s, %s, %s, %s);', (1000, 'Luigi', 64, 64) )
cur.execute('INSERT INTO "user" VALUES (%s, %s, %s, %s);', (1001, 'Adele', 34, 1) )

cur.execute('INSERT INTO "game" VALUES (%s, %s, %s)', (2000, 6, 1000) )
cur.execute('INSERT INTO "game" VALUES (%s, %s, %s)', (2001, 3, 1001) )   

cur.execute('INSERT INTO "played" VALUES (%s, %s, %s, %s, %s, %s, %s)', (1000, 2000, 15842, 'Mediterranean Ave', '' , 'Water Works', 2))
cur.execute('INSERT INTO "played" VALUES (%s, %s, %s, %s, %s, %s, %s)', (1000, 2001, 18339, 'Baltic Ave, Vermont Ave', 'Reading, Short Line' , '', 2))


conn.commit()

cur.close()
conn.close()
