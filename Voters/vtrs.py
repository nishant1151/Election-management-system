import sqlite3

from Server import ser
def vot_fp():
    ser.fp.heading()
    print("1)Vote")
    print("2)Election Result")
    print("2)Exit")
    for r in range(2):
        vt_ip=int(input("Enter Your Choice"))
        if vt_ip==1:
            ser.datetime.str_dd()
            break
        elif vt_ip==2:
            ser.admin_login.election_result()
            break
        elif vt_ip==3:
            ser.fp.eit()
def votte():
    file_name=sqlite3.connect("data")
    cur=file_name.cursor()

    qu=f'select * from in_fo'
    cur.execute(qu)
    dt=cur.fetchall()
    file_name.close()
    print("Id  Name")
    for i in dt:

        print(f'{i[5]})  {i[1]} {i[2]}')
    ad_vt()


def ad_vt():

    inptt = int(input("Enter Candidate Id You Want To Vote="))
    file_name = sqlite3.connect("data")
    csr = file_name.cursor()
    selet = f'SELECT * FROM in_fo where voter_id=={inptt};'
    csr.execute(selet)
    dd = csr.fetchall()
    a =dd[0][0]+1
    upda = f'UPDATE  in_fo SET vt={a} WHERE voter_id={inptt};'
    csr.execute(upda)
    file_name.commit()
    file_name.close()
    ser.fp.first_page()



