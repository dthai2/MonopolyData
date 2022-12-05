import os
import psycopg2
from flask import Flask, render_template, flash, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
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

@app.route('/userinfo')
def userStats():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "user";')
    user = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('userinfo.html', user=user)

@app.route('/userinfo', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        userid = int(request.form["Search"])
        conn = get_db_connection()
        cur = conn.cursor()
        query = 'select * from "user" where userid = %s'
        cur.execute(query, (userid,))
        user = cur.fetchall()
        cur.close()
        conn.close()
    return render_template('userinfo.html', user=user)


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

@app.route('/games/', methods=('GET', 'POST'))
def createGame():
    if request.method == 'POST':
        gameid = int(request.form["gameid"])
        players = int(request.form['players'])
        winner = int(request.form['winner'])

        conn = get_db_connection()
        cur = conn.cursor()

        #check if game id already exists/checks if game id
        query = 'select COUNT(*) from "game" where gameid = %s'
        cur.execute(query, (gameid,))
        count = cur.fetchone()[0]

        query1 = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query1, (winner,))
        user_count = cur.fetchone()[0]

        if count == 0 and user_count ==1 :
            #insert into game
            cur.execute('INSERT INTO "game" (gameid, numberofplayers, winnerid)'
                    'VALUES (%s, %s, %s)',
                    (gameid, players, winner))
            #update count of winner
            query2 = 'UPDATE "user" SET gameswon = gameswon + 1 WHERE userid = %s'
            cur.execute(query2, (winner,))
      
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('games.html')

@app.route('/played/', methods=('GET', 'POST'))
def createPlayed():
    if request.method == 'POST':
        userid = int(request.form["userid"])
        gameid = int(request.form["gameid"])
        Money = int(request.form["Money"])
        streetsowned = request.form["streetsowned"]
        railroadsowned = request.form["railroadsowned"]
        utilitiesowned = request.form["utilitiesowned"]
        numofproperties = int(request.form["numofproperties"])

        conn = get_db_connection()
        cur = conn.cursor()
        
         #check if game id exists
        query = 'select COUNT(*) from "game" where gameid = %s'
        cur.execute(query, (gameid,))
        count = cur.fetchone()[0]

        query1 = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query1, (userid,))
        user_count = cur.fetchone()[0]

        if count == 1 and user_count >0:
            cur.execute('INSERT INTO "played" (userid, gameid, money, streetsowned, railroadsowned, utilitiesowned, numproperties)'
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (userid, gameid, Money, streetsowned, railroadsowned, utilitiesowned, numofproperties))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('played.html')

@app.route('/deletegame/', methods=('GET', 'POST'))
def gamedelete():
    if request.method == 'POST':
        gameid = int(request.form["gameid"])

        conn = get_db_connection()
        cur = conn.cursor()
        
	#check if game id exists
        query = 'select COUNT(*) from "game" where gameid = %s'
        cur.execute(query, (gameid,))
        game_count = cur.fetchone()[0]

        if game_count == 1:
            query3 = 'DELETE FROM "game" WHERE gameid = %s'
            cur.execute(query3, (gameid,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('deletegame.html')

@app.route('/deleteplayer/', methods=('GET', 'POST'))
def playerdelete():
    if request.method == 'POST':
        userid = int(request.form["userid"])

        conn = get_db_connection()
        cur = conn.cursor()

        #check if user id exists
        query = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query, (userid,))
        count = cur.fetchone()[0]

        if count == 1:
            query = 'DELETE FROM "user" WHERE userid = %s'
            cur.execute(query, (userid,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('deleteplayer.html')

@app.route('/edit/', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        userid = int(request.form["userid"])
        name = int(request.form["name"])

        conn = get_db_connection()
        cur = conn.cursor()

        #check if user id exists
        query = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query, (userid,))
        count = cur.fetchone()[0]

        if count == 1:
            query = 'UPDATE "user" SET name = %s WHERE userid = %s'
            cur.execute(query, (name, userid,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html')

@app.route('/winner/', methods=('GET', 'POST'))
def winner():
    if request.method == 'POST':
        gameid = int(request.form["gameid"])
        winnerid = int(request.form["winnerid"])

        conn = get_db_connection()
        cur = conn.cursor()

        #check if game id exists
        query = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query, (gameid,))
        count = cur.fetchone()[0]

        #check if winner id exists
        query = 'select COUNT(*) from "user" where userid = %s'
        cur.execute(query, (winnerid,))
        count1 = cur.fetchone()[0]

        if count == 1 and count1 == 1:
            query = 'UPDATE "game" SET winnerid = %s WHERE gameid = %s'
            cur.execute(query, (winnerid, gameid,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('winner.html')
