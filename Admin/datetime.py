from Server import ser
import datetime

def dtm():
    yer=input("Enter Year= ")
    mon=input("Enter month= ")

    dy=input("Enter Election start day=")
    dd=input("Enter Election End day= ")
    global ele_d
    ele_d = datetime.datetime(int(yer), int(mon), int(dy))
    global el_dy
    el_dy = datetime.datetime(int(yer), int(mon), int(dd))
    global el_nw
    el_nw = datetime.datetime.now()
    ser.admin_login.ad_fp()



def str_dd():
    if el_nw>ele_d and el_nw<el_dy:
        ser.vtrs.votte()
        print("hii")

    else:
        ser.fp.eit()
        print("Election has ended please check Results")




