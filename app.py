import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            port='8888',
                            database='monopoly',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "played";')
    played = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', played=played)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form["name"]
        played = int(request.form['played'])
        won = int(request.form['won'])

        conn = get_db_connection()
        cur = conn.cursor()
        # need to generate a count for user 
        cur.execute('SELECT COUNT(*) FROM "user"')
        user_count = cur.fetchone()[0]
        id = user_count + 1000
        cur.execute('INSERT INTO "user" (userid, name, gamesplayed, gameswon)'
                    'VALUES (%s, %s, %s, %s)',
                    (id, name, played, won))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')