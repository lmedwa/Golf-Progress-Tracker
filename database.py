import sqlite3

def insert_round(score, date):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO rounds (score, date) VALUES (?, ?)", (score, date))
    con.commit()
    con.close()


#res = cur.execute("SELECT * FROM rounds")

#print(res.fetchone())