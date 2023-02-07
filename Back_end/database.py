from Server import ser
import sqlite3
def data_base(fna,lna,ag,ct):
    file_name = sqlite3.connect("data")
    cursr = file_name.cursor()
    global aa
    aa = ct

    crt = f'''CREATE TABLE IF NOT EXISTS in_fo(
    vt int,
    f_name varchar(255) not null,
    l_name varchar(255),
    age int,
    city varchar(255),
    
    voter_id INTEGER PRIMARY KEY AUTOINCREMENT
    );'''
    cursr.execute(crt)

    dta=f"insert into in_fo(f_name,l_name,age,city,vt) values ('{fna}','{lna}','{ag}','{ct}',{0});"
    cursr.execute(dta)
    file_name.commit()
    file_name.close()



