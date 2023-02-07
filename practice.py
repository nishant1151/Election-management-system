import datetime

def dtm():
    yer=int(input("Enter Year="))
    mon=int(input("Enter Month="))
    dy=int(input("Enter Election start day="))
    dd=int(input("Enter Election End day="))
    global ele_d
    ele_d = datetime.datetime(yer, mon, dy)
    global el_dy
    el_dy = datetime.datetime(yer, mon, dd)
    global el_nw
    el_nw = datetime.datetime.now()
    print(ele_d)
    print(el_dy)
    print(el_nw)





def str_dd():
    dtm()
    if el_nw>ele_d and el_nw<el_dy:
        print("hii")
    else:
        print("exit")






str_dd()