from Server import ser
import sqlite3
def vot_data(fm,lm,ae,usr,cyt,pas):

    fil_nam=sqlite3.connect("vote_data")
    db_cursr=fil_nam.cursor()

    crete=f'''CREATE TABLE IF NOT EXISTS in_fo(
    vtr_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fnam varchar(255) NOT NULL,
    lnam Varchar(255),
    age int,
    username varchar(255),
    city varchar(255),
    password varchar(255)
    );'''

    db_cursr.execute(crete)

    inset = f"insert into in_fo (fnam,lnam,age,username,city,password) values ('{fm}','{lm}','{ae}','{usr}','{cyt}','{pas}');"

    db_cursr.execute(inset)
    fil_nam.commit()
    fil_nam.close()


    