import sqlite3

def insert_round(score, date):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO rounds (score, date) VALUES (?, ?)", (score, date))
    con.commit()
    con.close()

def insert_range_session(club, distance):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO average_distance (club, range) VALUES (?, ?)", (club, distance))
    con.commit()
    con.close()

def get_club_average():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    res = cur.execute("SELECT club, AVG(range) FROM club_range GROUP BY club") 
    return res.fetchall()

#res = cur.execute("SELECT * FROM rounds")

#print(res.fetchone())