from Server import ser
line = '-' * 110
ee = "Elections".center(95)


def heading():
    print(line)
    print(ee)
    print(line)


def first_page():
    heading()
    print("1)Admin")
    print("2)Voters")
    for i in range(2):
        ippt=int(input("Enter your choice="))
        if ippt==1:
            ser.admin_login.ad_fp()
            break
        elif ippt==2:
            ser.vtrs.vot_fp()
            break
        else:
            print("error")



def eit():
    first_page()


