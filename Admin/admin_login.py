import sqlite3
import datetime

from Server import ser
infoo={'password':'1234','username':'nishant'}

def ad_fp():
    ser.fp.heading()
    print('1)Login')
    print('2)Exit')
    for h in range(2):
        ad_inpt=int(input("Enter your Choice="))
        if ad_inpt==1:

            logn()
            break
        else:
            print("Invalid Input")
            ser.fp.eit()
def logn():
    ser.fp.heading()
    for r in range(2):
        usrnm=input("Enter username=")
        psd=input("Enter Password=")
        if usrnm in infoo['username'] and psd in infoo['password']:
            selet()
            break
        else:
            print("Wrong Username or Password")

def selet():
    ser.fp.heading()
    print('1)Candidate Information')
    print('2)Voters Information')
    print("3)Start Election")
    print('4)Election Result')
    print('5)Exit')
    for r in range(2):
        se_inpt=int(input("Enter your choice="))
        if se_inpt==1:
            candidate_data()
            return
        elif se_inpt==2:
            voter_data()
            return
        elif se_inpt==3:
            strt_ele()
            return
        elif se_inpt==4:
            election_result()
            return

        elif se_inpt==5:
            ser.fp.eit()
            return
        else:
            print("Invalid Choice")
        return False
def candidate_data():
    ser.fp.heading()
    fnna=input("Enter Candidate First Name=")
    lnna=input("Enter Candidsate Last name=")
    agg=int(input("Enter Age="))
    global cyt
    cty = input("Enter Candidate City=")


    ser.database.data_base(fnna,lnna,agg,cty)
    selet()

def voter_data():
    ser.fp.heading()
    fna = input("Enter Voters First Name=")
    lna = input("Enter Voters Last Name=")
    ag = int(input("Enter Voters Age="))
    usrname = f'{fna}{lna}'
    cty = input("Enter Voters City")
    paswrd = f'{cty}{ag}'
    ser.Voter_database.vot_data(fna,lna,ag,usrname,cty,paswrd)
    selet()

def strt_ele():
    ser.datetime.dtm()


def election_result():
    file = sqlite3.connect('data')
    cr = file.cursor()
    se = "select * from in_fo"
    cr.execute(se)
    dt = cr.fetchall()
    elrr=max(dt)
    liel=list(elrr)
    print(f'{elrr[1]} {elrr[2]}')


