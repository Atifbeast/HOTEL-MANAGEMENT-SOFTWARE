from tkinter import *
from tkinter import messagebox
from tkinter import font
from datetime import date
from PIL import Image, ImageTk
import sqlite3
import time
pay = ''

hour = time.strftime('%I')
min = time.strftime('%M')
sec = time.strftime('%S')
ampm = time.strftime('%p')

root = Tk()
root.title('www.Burj.RoomIn.com.org')
img = ImageTk.PhotoImage(Image.open("C:\\Users\\ATIF SHAIK\\Downloads\\wallpaperflare.com_wallpaper (2).jpg"))

login = Canvas(root, width=3000, height=2500, bg='#27408B')
login.pack()
login.create_image(20,50, image=img)

login.create_text(580, 320, text='HOME PAGE', font='comicsansms 30 bold',fill='#54FF9F')
login.create_line(600,340,600,1000, width=2)

login.create_text(250,370, text='ALREADY EXISTING CUSTOMER', font='comicsansms 20 bold', fill='red')

login.create_text(95,440, text='USERNAME : ', font='comicsansms 20 italic', fill='black')
entvar = StringVar()
userentry = Entry(login, textvariable=entvar, font='comicsansms 15 bold', fg='white', bg='black')
userentry.place(x=190, y=428)

login.create_text(95,500, text='PASSWORD : ', font='comicsansms 20 italic', fill='black')
pasvar = StringVar()
passentry = Entry(login, textvariable=pasvar, font='comicsansms 15 bold', fg='white', bg='black')
passentry.place(x=190, y=483)

login.create_text(918,370, text='NEW CUSTOMER', font='comicsansms 20 bold', fill='red')
login.create_text(700,370, text='(New Customer Sign-Up)', font = 'comicsnasms 9 bold')

login.create_text(700,440, text='USERNAME : ', font='comicsansms 20 italic', fill='black')
nentvar = StringVar()
nuserentry = Entry(login, textvariable=nentvar, font='comicsansms 15 bold', fg='white', bg='black')
nuserentry.place(x=800, y=428)

login.create_text(700,500, text='PASSWORD : ', font='comicsansms 20 italic', fill='black')
npasvar = StringVar()
npassentry = Entry(login, textvariable=npasvar, font='comicsansms 15 bold', fg='white', bg='black')
npassentry.place(x=800, y=483)

Butsign = Button(login, text='SIGN UP', font='comicsansms 20 bold', borderwidth=5, bg='#F0FFFF', fg='#FF1493', padx=20)
Butsign.place(x=850, y=555)


def Login():
    conn = sqlite3.connect('AlBurjHotel.db')
    c = conn.cursor()
    usernames = []
    passwords = []
    cur = c.execute("SELECT UserName FROM ALBURJROOMS")
    for ans in cur.fetchall():
        for op in ans:
            usernames.append(op)

    conn.commit()
    c.close()

    conn2 = sqlite3.connect('AlBurjHotel.db')
    c2 = conn2.cursor()

    cur2 = c2.execute("SELECT Password FROM ALBURJROOMS")
    for ans2 in cur2.fetchall():
        for op2 in ans2:
            passwords.append(op2)

    if entvar.get() in usernames and pasvar.get() in passwords:
        # from HotelManagement import HotelLogin
        # # login.create_text(300, 200, text='ERROR-404 GO BACK', fill='blue', font='comicsansms 15 bold')
        # login.destroy()
        # HotelLogin.wow()

        login.destroy()

        can = Canvas(root, width=3000, height=2500, bg='yellow')
        can.pack()

        conn = sqlite3.connect('AlBurjHotel.db')
        c = conn.cursor()

        today_date = date.today()
        can.create_text(55, 28, text=today_date, font='comicsansms 15 bold')

        def HotelInfo():
            new_root2 = Toplevel(root)
            can2 = Canvas(new_root2, height=2000, width=2000, background='#FFE4C4')
            can2.pack()
            new_root2.title('STATUS...')

            can2.create_text(620, 40, text='HOTEL-STATUS', font='comicsansms 30 bold', fill='#4D4D4D')

            can2.create_text(80, 100, text='TOTAL ROOMS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(70, 140, text='10', font='helivitica 40 bold', fill='blue')

            can2.create_text(270, 100, text='AVAILABLE ROOMS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(260, 140, text='10', font='helevitica 40 bold', fill='blue')

            can2.create_text(460, 100, text='RESERVATIONS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(450, 140, text='0', font='helevitica 40 bold', fill='blue')

            can2.create_text(650, 100, text='CUSTOMERS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(640, 140, text='0', font='helivitica 40 bold', fill='blue')

            can2.create_text(840, 100, text='STAFF', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(850, 140, text='50', font='helivitica 40 bold', fill='blue')

            can2.create_text(1030, 100, text='UNDER RENOVATION', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(1040, 140, text='5', font='helivitica 40 bold', fill='blue')

        def exit__():
            exit()

        def RoomsInfo():
            new_root1 = Toplevel(root)
            can1 = Canvas(new_root1, height=2000, width=2000, background='#FFE4C4')
            can1.pack()
            new_root1.title('ROOMS...')

            def room1():
                r1info = Label(new_root1, text='ROOM-1', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r1info.place(x=570, y=55)

                r1bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r1bed.place(x=100, y=100)
                l1 = Label(new_root1, text='5', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r1ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r1tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r1wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r1price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1price.place(x=960, y=100)
                l5 = Label(new_root1, text='$100000', font='comicsansms 20 bold', fg='#00008B')
                l5.place(x=960, y=140)

                r1re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room2():
                r2info = Label(new_root1, text='ROOM-2', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r2info.place(x=570, y=55)

                r2bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r2bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r2ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r2tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r2wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r2price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2price.place(x=960, y=100)
                l5 = Label(new_root1, text='$90000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r2re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room3():
                r3info = Label(new_root1, text='ROOM-3', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r3info.place(x=570, y=55)

                r3bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r3bed.place(x=100, y=100)
                l1 = Label(new_root1, text='5', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r3ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r3tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r3wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r3price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3price.place(x=960, y=100)
                l5 = Label(new_root1, text='$80000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r3re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room4():
                r4info = Label(new_root1, text='ROOM-4', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r4info.place(x=570, y=55)

                r4bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r4bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r4ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r4tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r4wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r4price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4price.place(x=960, y=100)
                l5 = Label(new_root1, text='$70000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r4re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room5():
                r5info = Label(new_root1, text='ROOM-5', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r5info.place(x=570, y=55)

                r5bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r5bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r5ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r5tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r5wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r5price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5price.place(x=960, y=100)
                l5 = Label(new_root1, text='$60000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r5re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room6():
                r6info = Label(new_root1, text='ROOM-6', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r6info.place(x=570, y=55)

                r6bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r6bed.place(x=100, y=100)
                l1 = Label(new_root1, text='3', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r6ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r6tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r6wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r6price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6price.place(x=960, y=100)
                l5 = Label(new_root1, text='$50000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r6re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room7():
                r7info = Label(new_root1, text='ROOM-7', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r7info.place(x=570, y=55)

                r7bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r7bed.place(x=100, y=100)
                l1 = Label(new_root1, text='2', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r7ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r7tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r7wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r7price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7price.place(x=960, y=100)
                l5 = Label(new_root1, text='$40000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r7re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room8():
                r8info = Label(new_root1, text='ROOM-8', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r8info.place(x=570, y=55)

                r8bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r8bed.place(x=100, y=100)
                l1 = Label(new_root1, text='2', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r8ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r8tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r8wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r8price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8price.place(x=960, y=100)
                l5 = Label(new_root1, text='$30000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r8re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room9():
                r9info = Label(new_root1, text='ROOM-9', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r9info.place(x=570, y=55)

                r9bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r9bed.place(x=100, y=100)
                l1 = Label(new_root1, text='1', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r9ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r9tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r9wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r9price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white', padx=10)
                r9price.place(x=960, y=100)
                l5 = Label(new_root1, text='$7000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=970, y=140)

                r9re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room10():
                r10info = Label(new_root1, text='ROOM-10', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r10info.place(x=565, y=55)

                r10bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r10bed.place(x=100, y=100)
                l1 = Label(new_root1, text='1', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r10ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r10tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10tv.place(x=500, y=100)
                l3 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=540, y=140)

                r10wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r10price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white', padx=10)
                r10price.place(x=960, y=100)
                l5 = Label(new_root1, text='$5000', font='comicsansms 20 bold', fg='#00008B', padx=10)
                l5.place(x=962, y=140)

                r10re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            R1 = Button(new_root1, text='ROOM-1', font='comicsansms 10 bold', borderwidth=4, command=room1)
            R1.place(x=10, y=70)

            R2 = Button(new_root1, text='ROOM-2', font='comicsansms 10 bold', borderwidth=4, command=room2)
            R2.place(x=10, y=110)

            R3 = Button(new_root1, text='ROOM-3', font='comicsansms 10 bold', borderwidth=4, command=room3)
            R3.place(x=10, y=150)

            R4 = Button(new_root1, text='ROOM-4', font='comicsansms 10 bold', borderwidth=4, command=room4)
            R4.place(x=10, y=190)

            R5 = Button(new_root1, text='ROOM-5', font='comicsansms 10 bold', borderwidth=4, command=room5)
            R5.place(x=10, y=230)

            R6 = Button(new_root1, text='ROOM-6', font='comicsansms 10 bold', borderwidth=4, command=room6)
            R6.place(x=10, y=270)

            R7 = Button(new_root1, text='ROOM-7', font='comicsansms 10 bold', borderwidth=4, command=room7)
            R7.place(x=10, y=310)

            R8 = Button(new_root1, text='ROOM-8', font='comicsansms 10 bold', borderwidth=4, command=room8)
            R8.place(x=10, y=350)

            R9 = Button(new_root1, text='ROOM-9', font='comicsansms 10 bold', borderwidth=4, command=room9)
            R9.place(x=10, y=390)

            R10 = Button(new_root1, text='ROOM-10', font='comicsansms 10 bold', borderwidth=4, command=room10)
            R10.place(x=10, y=430)

        def payment():
            new_root3 = Toplevel(root)
            can3 = Canvas(new_root3, height=2000, width=2000, background='#FFE4C4')
            can3.pack()
            new_root3.title('PAYMENTS...')
            can3.create_text(260, 100, text='YOUR TOTAL AMT FOR  :', font='comicsansms 30 bold')

            frame = Frame(new_root3, bd=10, relief=GROOVE)
            frame.place(x=850, y=250, width=350, height=400)

            for item in lbx.curselection():
                payget = lbx.get(item)
                # pay = True
                can3.create_text(670, 100, text=payget, font='comicsansms 30 bold')
                label1 = Label(frame, text='*' * 80, font='comicsansms 8 bold')
                label1.pack()
                label2 = Label(frame, text='*' * 80, font='comicsansms 8 bold')
                label2.pack()
                label3 = Label(frame, text='Atif, Nishan, Rathan BurjHotel Inc.\nISTANBUL, TURKEY')
                label3.pack()
                label4 = Label(frame, text='=' * 80)
                label4.pack()
                label5 = Label(frame, text='YOUR-ROOM')
                label5.place(x=10, y=120)
                label8 = Label(frame, text='AMOUNT')
                label8.place(x=230, y=120)
                payget = str(payget)
                label6 = Label(frame, text=payget[:7])
                label6.place(x=10, y=150)
                label7 = Label(frame, text=payget[8:])
                label7.place(x=200, y=150)
                print(payget)

            def paid():
                global asking
                asking = messagebox.askquestion('PAY', 'ARE YOU SURE')
                if asking == 'yes' and pay == True:
                    time.sleep(1)
                    messagebox.showinfo('IMPORTANT',
                                        'YOU HAVE SUCCESSFULLY PAID YOUR AMOUNT NOW YOU CAN ACCEPT THE ROOM')
                elif asking == 'no' and pay == True:
                    pass
                    messagebox.showerror('ERROR', 'YOU CANCELLED YOUR TRANSACTION\n  TRY AGAIN')
                else:
                    messagebox.showerror('ERROR', 'YOU HAVE NOT REGISTERED YOUR INFO')

            paybyt = Button(can3, text='PAY', font='comicsansms 23 bold', borderwidth=6, command=paid)
            paybyt.place(x=700, y=300)

        def reserve():
            name_get = var.get()
            mid_get = var1.get()
            last_get = var2.get()
            num_get = var3.get()
            em_get = var4.get()
            ga_get = var5.get()
            chil_get = var6.get()
            ad_get = var7.get()
            days_get = var8.get()
            room_get = var9.get()
            # suser_get = nentvar.get()
            # spas_get = npasvar.get()
            if len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(
                    ga_get) != 0 and num_get.isnumeric() and chil_get.isnumeric() and ad_get.isnumeric() and days_get.isnumeric() and len(
                num_get) == 10:
                quest = messagebox.askquestion('QUESTION???', 'Are You Sure???')
                if quest == 'yes':
                    data = [name_get, mid_get, last_get, num_get, em_get, ga_get, chil_get, ad_get, days_get, entvar.get(), pasvar.get(), today_date, f'{hour}:{min}:{sec} {ampm}']
                    c.executemany(
                        "INSERT INTO ALBURJROOMS ('FIRST_NAME','MIDDLE_NAME','LAST_NAME','CONTACT_NUMBER','EMAIL','GUEST_ADDRESS','NUMBER_OF_CHILDREN','NUMBER_OF_ADULTS','NUMBER_OF_DAYS_STAY','UserName','Password','DATE','TIME') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (data,))

                    messagebox.showinfo('REGISTERED',
                                        'Your Information Has Been Sucessfullly Registered With Us...Kindly Proceed Further')
                    messagebox.showinfo('INFO', 'Now You May Proceed To Apply Filters You Want To Get In Your Room')

                    def room():
                        ruum = {'Room-1': '$100000', 'Room-2': '$90000', 'Room-3': '$80000', 'Room-4': '$70000',
                                'Room-5': '$60000',
                                'Room-6': '$50000', 'Room-7': '$40000', 'Room-8': '$30000', 'Room-9': '$7000',
                                'Room-10': '$5000'}
                        lbx.insert(0, 'Room    :   Price')
                        for key in ruum:
                            tobeins = key, ':', ruum[key]
                            lbx.insert(END, tobeins)

                        messagebox.showinfo('INFO', 'For More Info About Rooms You Can Press Rooms Button To Check')

                        def lbxselect():
                            global pay
                            pay = True
                            for item in lbx.curselection():
                                got = lbx.get(item)
                                var9.set(got)
                                lastvar = var9.get()
                                try:
                                    if asking:
                                        c.execute('''INSERT INTO ALBURJROOMS ('Room_No') VALUES (?)''', (str(lastvar),))
                                        conn.commit()
                                        conn.close()
                                        messagebox.showinfo('REGISTERED',
                                                            'THANK YOU FOR BOOKING A ROOM WITH ALBURJHOTELS YOU CAN CHECK IN FROM THE SAME DAY \n  ENJOY YOUR DAY')

                                except Exception:
                                    messagebox.showwarning('WARNING',
                                                           'DEAR USER YOU FIRST NEED TO PAY AMOUNT FROM PAYMENT SECTION...')
                                    pay = True

                        accbut = Button(root, text='Accept Selected Room', borderwidth=4, command=lbxselect)
                        accbut.place(x=670, y=590)

                    finalRoom = Button(root, text='FIND ROOMS', font='comicsansms 17 bold', borderwidth=7, bg='grey',
                                       command=room)
                    finalRoom.place(x=600, y=440)

                elif quest == 'no':
                    pass

            elif len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(
                    ga_get) != 0 and num_get.isnumeric() and chil_get.isnumeric() and ad_get.isnumeric() and days_get.isnumeric() and len(
                num_get) != 10:
                messagebox.showwarning('WARNING', 'Contact Number Should Be Of 10 Digits')

            elif len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(
                    ga_get) != 0 and not num_get.isnumeric() or chil_get.isnumeric() or ad_get.isnumeric() or days_get.isnumeric():
                messagebox.showerror('ERROR', 'Expected Numbers In Some Of The Feilds')

            elif len(name_get) or len(mid_get) or len(last_get) or len(em_get) or len(em_get) or len(ga_get) or len(
                    num_get) or len(chil_get) or len(ad_get) or len(days_get) == 0:
                messagebox.showerror('ERROR', 'Please Fill Out All The Fields')

        def unreserveH():
            quest = messagebox.askquestion('QUESTION', 'Are You Sure...Coz The Information Entered By You Will Be Lost')
            if quest == 'yes':
                var.set('First Name*')
                var1.set('Middle Name*')
                var2.set('Last Name*')
                var3.set('Contact Number*')
                var4.set('Email*')
                var5.set('Guest Address*')
                var6.set('Number Of Children*')
                var7.set('Number Of Adults*')
                var8.set('Number Of Staying Days*')
            else:
                pass

        can.create_text(680, 30,
                        text='BURJ MANAGEMENT SYSTEM DEVELOPED BY "ATIF" AND CO-DEVELOPED BY "NISHAN" AND "RATHAN"',
                        font='comicsansms 16 bold', fill='black')

        imgHotelStatus = ImageTk.PhotoImage(Image.open('hotelstatuslogin.jpg'))
        can.create_image(80, 100, image=imgHotelStatus)
        butHotelStatus = Button(root, text='HOTEL STATUS', font='comicsansms 13 bold', borderwidth=5, command=HotelInfo)
        butHotelStatus.place(x=0, y=150)

        imgDoor = ImageTk.PhotoImage(Image.open('Door.jpg'))
        can.create_image(260, 100, image=imgDoor)
        butDoor = Button(root, text='ROOMS', font='comicsansms 13 bold', borderwidth=5, command=RoomsInfo)
        butDoor.place(x=220, y=150)

        imgReserve = ImageTk.PhotoImage(Image.open('Reserve.jpg'))
        can.create_image(490, 100, image=imgReserve)
        butReserve = Button(root, text='RESERVE', font='comicsansms 13 bold', borderwidth=5)
        butReserve.place(x=440, y=160)

        imgPayments = ImageTk.PhotoImage(Image.open('payments.jpg'))
        can.create_image(720, 100, image=imgPayments)
        # can.create_text(720,160,text='PAYMENTS INFO',fill='black',font='comicsansms 13 bold')
        butPayments = Button(root, text='PAYMENTS INFO', font='comicsansms 13 bold', borderwidth=5, command=payment)
        butPayments.place(x=650, y=150)

        imgContacts = ImageTk.PhotoImage(Image.open('contacts.png'))
        can.create_image(950, 100, image=imgContacts)
        butContacts = Button(root, text='CONTACTS', font='comicsansms 13 bold', borderwidth=5)
        butContacts.place(x=890, y=150)

        imgExit = ImageTk.PhotoImage(Image.open('exit.png'))
        can.create_image(1180, 100, image=imgExit)
        butExit = Button(root, text='EXIT', font='comicsansms 13 bold', borderwidth=5, command=exit__)
        butExit.place(x=1150, y=150)

        can.create_text(430, 230, text='PERSONAL INFORMATION', font='comicsansms 15 bold')

        var = StringVar()
        # var.set('First Name*')
        first_name = c.execute("SELECT FIRST_NAME FROM ALBURJROOMS WHERE Password = ? AND UserName = ?", [pasvar.get(), entvar.get()])
        F = [i for i in first_name.fetchone()]
        f = ''
        var.set(f.join(F))
        entry = Entry(root, textvariable=var, font='comicsansms 9 bold')
        can.create_window(100, 270, window=entry)

        var1 = StringVar()
        # var1.set('Middle Name*')
        mid_name = c.execute("SELECT MIDDLE_NAME FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                               [pasvar.get(), entvar.get()])
        M = [i for i in mid_name.fetchone()]
        m = ''
        var1.set(m.join(M))
        entry1 = Entry(root, textvariable=var1, font='comicsansms 9 bold')
        can.create_window(300, 270, window=entry1)

        var2 = StringVar()
        # var2.set('Last Name*')
        lst_name = c.execute("SELECT LAST_NAME FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                               [pasvar.get(), entvar.get()])
        L = [i for i in lst_name.fetchone()]
        l = ''
        var2.set(l.join(L))
        entry2 = Entry(root, textvariable=var2, font='comicsansms 9 bold')
        can.create_window(500, 270, window=entry2)

        can.create_text(450, 330, text='CONTACT INFORMATION', font='comicsansms 15 bold')

        var3 = StringVar()
        # var3.set('Contact Number*')
        cntnum = c.execute("SELECT CONTACT_NUMBER FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                               [pasvar.get(), entvar.get()])
        C = [i for i in cntnum.fetchone()]
        c = ''
        var3.set(c.join(C))
        entry3 = Entry(root, textvariable=var3, font='comicsansms 9 bold')
        can.create_window(100, 370, window=entry3)

        var4 = StringVar()
        # var4.set('Email*')
        try:
            email = c.execute("SELECT EMAIL FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            E = [i for i in email.fetchone()]
            e = ''
            var4.set(e.join(E))
        except Exception:
            var4.set('Email*')
        entry4 = Entry(root, textvariable=var4, font='comicsansms 9 bold')
        can.create_window(300, 370, window=entry4)

        var5 = StringVar()
        # var5.set('Guest Address*')
        try:
            adds = c.execute("SELECT GUEST_ADDRESS FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            A = [i for i in adds.fetchone()]
            a = ''
            var5.set(a.join(A))
        except Exception:
            var5.set('Guest Address*')
        entry5 = Entry(root, textvariable=var5, font='comicsansms 9 bold')
        can.create_window(500, 370, window=entry5)

        can.create_text(450, 430, text='RESERVE INFORMATION', font='comicsansms 15 bold')

        var6 = StringVar()
        # var6.set('Number of Children*')
        try:
            kids = c.execute("SELECT NUMBER_OF_CHILDREN FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            K = [i for i in kids.fetchone()]
            k = ''
            var6.set(k.join(K))
        except Exception:
            var6.set('Number of Children*')
        entry6 = Entry(root, textvariable=var6, font='comicsansms 9 bold')
        can.create_window(100, 480, window=entry6)

        var7 = StringVar()
        # var7.set('Number of Adults*')
        try:
            adults = c.execute("SELECT NUMBER OF ADULTS FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            AA = [i for i in adults.fetchone()]
            aa = ''
            var.set(aa.join(AA))
        except Exception:
            var7.set('Number of Adults*')
        entry7 = Entry(root, textvariable=var7, font='comicsansms 9 bold')
        can.create_window(300, 480, window=entry7)

        var8 = StringVar()
        # var8.set('Number of Staying Days*')
        try:
            days = c.execute("SELECT NUMBER_OF_DAYS_STAY FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            D = [i for i in days.fetchone()]
            d = ''
            var8.set(d.join(D))
        except Exception:
            var8.set('Number of Staying Days*')
        entry8 = Entry(root, textvariable=var8, font='comicsansms 9 bold')
        can.create_window(500, 480, window=entry8)

        var9 = StringVar()
        # var9.set('Know Room Number Here*')
        try:
            num = c.execute("SELECT Room_No FROM ALBURJROOMS WHERE Password = ? AND UserName = ?",
                                   [pasvar.get(), entvar.get()])
            N = [i for i in num.fetchone()]
            n = ''
            var9.set(n.join(N))
        except Exception:
            var9.set('Know Room Number Here*')
        entry9 = Entry(root, textvariable=var9, font='comicsansms 9 bold', width=25)
        can.create_window(700, 542, window=entry9)

        reserve = Button(root, text='RESERVE', font='comicsansms 12 bold', fg='blue', bg='black', borderwidth=8,
                         command=reserve)
        reserve.place(x=200, y=530)

        unreserve = Button(root, text='UNRESERVE', font='comicsansms 12 bold', fg='red', bg='black', borderwidth=8,
                           command=unreserveH)
        unreserve.place(x=370, y=530)

        can.create_text(1020, 220, text='FILTERS', font='comicsansms 15 bold')

        variety_beds = ['Twin', 'Twin XL', 'Full', 'Queen', 'King', 'DayBed', 'WaterBed', 'AirBed', 'Four-Poster Bed',
                        'Round Bed', 'Ottoman Bed', 'Divan', 'Hanging Bed', 'Triple Bed', 'Simple Bed']
        setter = StringVar()
        setter.set('Select')
        optionbed = OptionMenu(root, setter, *variety_beds)
        optionbed.config(font='comicsansms 10 bold')
        can.create_text(900, 260, text='BED(S)  :  ', font='comicsansms 15 bold')
        optionbed.place(x=1100, y=240)

        AC = ['Samsung', 'Panasonic', 'Sony', 'Bosch', 'LG', 'Haier']
        setterAC = StringVar()
        setterAC.set('Select')
        optionac = OptionMenu(root, setterAC, *AC)
        optionac.config(font='comicsansms 10 bold')
        can.create_text(900, 320, text='AC  :  ', font='comicsansms 15 bold')
        optionac.place(x=1100, y=300)

        TV = ['One plus', 'Sony Bravia Curved', 'Sony Bravia', 'MI', 'Samsung', 'TCL']
        setterTV = StringVar()
        setterTV.set('Select')
        optiontv = OptionMenu(root, setterTV, *TV)
        optiontv.config(font='comicsansms 10 bold')
        can.create_text(900, 380, text='TV  :  ', font='comicsansms 15 bold')
        optiontv.place(x=1100, y=360)

        wifi = ['Airtel', 'Jio', 'Hathway', 'Private Wifi(COST EXTRA)']
        setterwifi = StringVar()
        setterwifi.set('Select')
        optionwifi = OptionMenu(root, setterwifi, *wifi)
        optionwifi.config(font='comicsansms 10 bold')
        can.create_text(900, 440, text='WIFI  :  ', font='comicsansms 15 bold')
        optionwifi.place(x=1100, y=420)

        lbx = Listbox(root, bd=8, highlightthickness=20, width=70, height=5)
        bolded = font.Font(weight='bold')
        lbx.config(font=bolded)
        lbx.place(x=800, y=480)

        root.mainloop()









    elif len(entvar.get()) == 0:
        messagebox.showerror('ERROR', 'DEAR USER ENTER USERNAME')

    elif len(pasvar.get()) == 0:
        messagebox.showerror('ERROR', 'DEAR USER ENTER PASSWORD')

    else:
        messagebox.showwarning('WARNING', 'USERNAME OR PASSWORD IS INCORRECT')



def sign():
    if len(nentvar.get()) == 0:
        messagebox.showerror('ERROR', 'DEAR USER ENTER THE USERNAME BEFORE SIGNING-UP')
    elif len(npasvar.get()) == 0:
        messagebox.showerror('ERROR', 'DEAR USER ENTER THE PASSWORD BEFORE SIGNING-UP')
    elif nentvar.get() == npasvar.get():
        messagebox.showerror('ERROR', 'DEAR USER USERNAME AND PASSWORD CANNOT BE SAME')
    else:
        messagebox.showwarning('WARNING', 'DEAR USER PLEASE REMEMBER YOUR USERNAME AND PASSWORD TO LOGIN... FAILING WHICH YOU LOOSE YOUR MEMBERSHIP')
        # login.create_text(300,200,text='ERROR-404 GO BACK',fill='black', font='comicsansms 15 bold')
        login.destroy()
        can = Canvas(root,width=3000,height=2500,bg='yellow')
        can.pack()



        conn = sqlite3.connect('AlBurjHotel.db')
        c = conn.cursor()

        today_date = date.today()
        can.create_text(55,28,text= today_date,font='comicsansms 15 bold')

        def HotelInfo():
            new_root2 = Toplevel(root)
            can2 = Canvas(new_root2, height=2000, width=2000, background='#FFE4C4')
            can2.pack()
            new_root2.title('STATUS...')

            can2.create_text(620,40,text='HOTEL-STATUS',font='comicsansms 30 bold',fill='#4D4D4D')

            can2.create_text(80,100,text='TOTAL ROOMS',font='comicsansms 15 bold',fill='#4D4D4D')
            can2.create_text(70,140,text='10',font='helivitica 40 bold',fill='blue')

            can2.create_text(270, 100, text='AVAILABLE ROOMS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(260, 140, text='10', font='helevitica 40 bold', fill='blue')

            can2.create_text(460, 100, text='RESERVATIONS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(450, 140, text='0', font='helevitica 40 bold', fill='blue')

            can2.create_text(650, 100, text='CUSTOMERS', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(640, 140, text='0', font='helivitica 40 bold', fill='blue')

            can2.create_text(840, 100, text='STAFF', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(850, 140, text='50', font='helivitica 40 bold', fill='blue')

            can2.create_text(1030, 100, text='UNDER RENOVATION', font='comicsansms 15 bold', fill='#4D4D4D')
            can2.create_text(1040, 140, text='5', font='helivitica 40 bold', fill='blue')


        def exit__():
            exit()


        def RoomsInfo():
            new_root1 = Toplevel(root)
            can1 = Canvas(new_root1,height=2000,width=2000,background='#FFE4C4')
            can1.pack()
            new_root1.title('ROOMS...')

            def room1():
                r1info = Label(new_root1,text='ROOM-1',font='comicsansms 15 bold',bg='blue',fg='white')   #570,55
                r1info.place(x=570,y=55)

                r1bed = Label(new_root1,text='Total Bed(s)',font='comicsansms 12 bold',bg='blue',fg='white')
                r1bed.place(x=100,y=100)
                l1 = Label(new_root1,text='5',font='comicsansms 20 bold',fg='#00008B')
                l1.place(x=130,y=140)

                r1ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1ac.place(x=300, y=100)
                l2 = Label(new_root1,text='YES',font='comicsansms 20 bold',fg='#00008B')
                l2.place(x=330,y=140)

                r1tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r1wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r1price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1price.place(x=960, y=100)
                l5 = Label(new_root1, text='$100000', font='comicsansms 20 bold', fg='#00008B')
                l5.place(x=960, y=140)

                r1re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r1re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room2():
                r2info = Label(new_root1, text='ROOM-2', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r2info.place(x=570, y=55)

                r2bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r2bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r2ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r2tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r2wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r2price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2price.place(x=960, y=100)
                l5 = Label(new_root1, text='$90000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r2re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r2re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room3():
                r3info = Label(new_root1, text='ROOM-3', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r3info.place(x=570, y=55)

                r3bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r3bed.place(x=100, y=100)
                l1 = Label(new_root1, text='5', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r3ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r3tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r3wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r3price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3price.place(x=960, y=100)
                l5 = Label(new_root1, text='$80000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r3re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r3re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold',fg='#00008B')
                l6.place(x=1130, y=140)

            def room4():
                r4info = Label(new_root1, text='ROOM-4', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r4info.place(x=570, y=55)

                r4bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r4bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r4ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r4tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r4wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r4price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4price.place(x=960, y=100)
                l5 = Label(new_root1, text='$70000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r4re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r4re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room5():
                r5info = Label(new_root1, text='ROOM-5', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r5info.place(x=570, y=55)

                r5bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r5bed.place(x=100, y=100)
                l1 = Label(new_root1, text='4', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r5ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r5tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r5wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r5price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5price.place(x=960, y=100)
                l5 = Label(new_root1, text='$60000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r5re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r5re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room6():
                r6info = Label(new_root1, text='ROOM-6', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r6info.place(x=570, y=55)

                r6bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r6bed.place(x=100, y=100)
                l1 = Label(new_root1, text='3', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r6ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r6tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r6wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r6price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6price.place(x=960, y=100)
                l5 = Label(new_root1, text='$50000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r6re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r6re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room7():
                r7info = Label(new_root1, text='ROOM-7', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r7info.place(x=570, y=55)

                r7bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r7bed.place(x=100, y=100)
                l1 = Label(new_root1, text='2', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r7ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r7tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r7wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r7price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7price.place(x=960, y=100)
                l5 = Label(new_root1, text='$40000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r7re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r7re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room8():
                r8info = Label(new_root1, text='ROOM-8', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r8info.place(x=570, y=55)

                r8bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r8bed.place(x=100, y=100)
                l1 = Label(new_root1, text='2', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r8ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r8tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r8wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r8price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8price.place(x=960, y=100)
                l5 = Label(new_root1, text='$30000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r8re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r8re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)

            def room9():
                r9info = Label(new_root1, text='ROOM-9', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r9info.place(x=570, y=55)

                r9bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r9bed.place(x=100, y=100)
                l1 = Label(new_root1, text='1', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r9ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r9tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9tv.place(x=500, y=100)
                l3 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=530, y=140)

                r9wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r9price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white',padx=10)
                r9price.place(x=960, y=100)
                l5 = Label(new_root1, text='$7000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=970, y=140)

                r9re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r9re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)


            def room10():
                r10info = Label(new_root1, text='ROOM-10', font='comicsansms 15 bold', bg='blue', fg='white')  # 570,55
                r10info.place(x=565, y=55)

                r10bed = Label(new_root1, text='Total Bed(s)', font='comicsansms 12 bold', bg='blue', fg='white')
                r10bed.place(x=100, y=100)
                l1 = Label(new_root1, text='1', font='comicsansms 20 bold', fg='#00008B')
                l1.place(x=130, y=140)

                r10ac = Label(new_root1, text='AC Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10ac.place(x=300, y=100)
                l2 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l2.place(x=330, y=140)

                r10tv = Label(new_root1, text='TV Available?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10tv.place(x=500, y=100)
                l3 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l3.place(x=540, y=140)

                r10wifi = Label(new_root1, text='Wifi?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10wifi.place(x=750, y=100)
                l4 = Label(new_root1, text='YES', font='comicsansms 20 bold', fg='#00008B')
                l4.place(x=750, y=140)

                r10price = Label(new_root1, text='Price?', font='comicsansms 12 bold', bg='blue', fg='white',padx=10)
                r10price.place(x=960, y=100)
                l5 = Label(new_root1, text='$5000', font='comicsansms 20 bold', fg='#00008B',padx=10)
                l5.place(x=962, y=140)

                r10re = Label(new_root1, text='Reserved?', font='comicsansms 12 bold', bg='blue', fg='white')
                r10re.place(x=1100, y=100)
                l6 = Label(new_root1, text='NO', font='comicsansms 20 bold', fg='#00008B')
                l6.place(x=1130, y=140)


            R1 = Button(new_root1, text='ROOM-1', font='comicsansms 10 bold', borderwidth=4,command=room1)
            R1.place(x=10, y=70)

            R2 = Button(new_root1, text='ROOM-2', font='comicsansms 10 bold', borderwidth=4,command=room2)
            R2.place(x=10, y=110)

            R3 = Button(new_root1, text='ROOM-3', font='comicsansms 10 bold', borderwidth=4,command=room3)
            R3.place(x=10, y=150)

            R4 = Button(new_root1, text='ROOM-4', font='comicsansms 10 bold', borderwidth=4,command=room4)
            R4.place(x=10, y=190)

            R5 = Button(new_root1, text='ROOM-5', font='comicsansms 10 bold', borderwidth=4,command=room5)
            R5.place(x=10, y=230)

            R6 = Button(new_root1, text='ROOM-6', font='comicsansms 10 bold', borderwidth=4,command=room6)
            R6.place(x=10, y=270)

            R7 = Button(new_root1, text='ROOM-7', font='comicsansms 10 bold', borderwidth=4,command=room7)
            R7.place(x=10, y=310)

            R8 = Button(new_root1, text='ROOM-8', font='comicsansms 10 bold', borderwidth=4,command=room8)
            R8.place(x=10, y=350)

            R9 = Button(new_root1, text='ROOM-9', font='comicsansms 10 bold', borderwidth=4,command=room9)
            R9.place(x=10, y=390)

            R10 = Button(new_root1, text='ROOM-10', font='comicsansms 10 bold', borderwidth=4,command=room10)
            R10.place(x=10, y=430)

        def payment():
            new_root3 = Toplevel(root)
            can3 = Canvas(new_root3, height=2000, width=2000, background='#FFE4C4')
            can3.pack()
            new_root3.title('PAYMENTS...')
            can3.create_text(260,100,text='YOUR TOTAL AMT FOR  :',font='comicsansms 30 bold')

            frame = Frame(new_root3, bd=10, relief=GROOVE)
            frame.place(x=850,y=250,width=350,height=400)


            for item in lbx.curselection():
                payget = lbx.get(item)
                # pay = True
                can3.create_text(670,100,text=payget,font = 'comicsansms 30 bold')
                label1 = Label(frame, text='*' * 80, font='comicsansms 8 bold')
                label1.pack()
                label2 = Label(frame, text='*' * 80, font='comicsansms 8 bold')
                label2.pack()
                label3 = Label(frame, text='Atif, Nishan, Rathan BurjHotel Inc.\nISTANBUL, TURKEY')
                label3.pack()
                label4 = Label(frame, text='=' * 80)
                label4.pack()
                label5 = Label(frame, text='YOUR-ROOM')
                label5.place(x=10,y=120)
                label8 = Label(frame, text='AMOUNT')
                label8.place(x=230, y=120)
                payget = str(payget)
                label6 = Label(frame, text=payget[:9])
                label6.place(x=10,y=150)
                label7 = Label(frame, text=payget[8:])
                label7.place(x=240,y=150)
                print(payget)



            def paid():
                    global asking
                    asking = messagebox.askquestion('PAY','ARE YOU SURE')
                    if asking == 'yes' and pay == True:
                        time.sleep(1)
                        messagebox.showinfo('IMPORTANT','YOU HAVE SUCCESSFULLY PAID YOUR AMOUNT NOW YOU CAN ACCEPT THE ROOM')
                    elif asking == 'no' and pay == True:
                        pass
                        messagebox.showerror('ERROR','YOU CANCELLED YOUR TRANSACTION\n  TRY AGAIN')
                    else:
                        messagebox.showerror('ERROR','YOU HAVE NOT REGISTERED YOUR INFO')
            paybyt = Button(can3,text='PAY',font='comicsansms 23 bold',borderwidth=6,command=paid)
            paybyt.place(x=700,y=300)

        def reserve():
            name_get = var.get()
            mid_get = var1.get()
            last_get = var2.get()
            num_get = var3.get()
            em_get = var4.get()
            ga_get = var5.get()
            chil_get = var6.get()
            ad_get = var7.get()
            days_get = var8.get()
            room_get = var9.get()
            suser_get = nentvar.get()
            spas_get = npasvar.get()
            if len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(ga_get) !=0 and num_get.isnumeric() and chil_get.isnumeric() and ad_get.isnumeric() and days_get.isnumeric() and len(num_get) == 10:
                quest = messagebox.askquestion('QUESTION???','Are You Sure???')
                if quest == 'yes':
                    data = [name_get,mid_get,last_get,num_get,em_get,ga_get,chil_get,ad_get,days_get,suser_get,spas_get, today_date, f'{hour}:{min}:{sec} {ampm}']
                    c.executemany("INSERT INTO ALBURJROOMS ('FIRST_NAME','MIDDLE_NAME','LAST_NAME','CONTACT_NUMBER','EMAIL','GUEST_ADDRESS','NUMBER_OF_CHILDREN','NUMBER_OF_ADULTS','NUMBER_OF_DAYS_STAY','UserName','Password','DATE','TIME') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(data,))

                    messagebox.showinfo('REGISTERED','Your Information Has Been Sucessfullly Registered With Us...Kindly Proceed Further')
                    messagebox.showinfo('INFO','Now You May Proceed To Apply Filters You Want To Get In Your Room')

                    def room():
                        ruum = {'Room-1': '$100000', 'Room-2': '$90000', 'Room-3': '$80000', 'Room-4': '$70000',
                                'Room-5': '$60000',
                                'Room-6': '$50000', 'Room-7': '$40000', 'Room-8': '$30000', 'Room-9': '$7000',
                                'Room-10': '$5000'}
                        lbx.insert(0, 'Room    :   Price')
                        for key in ruum:
                            tobeins = key, ':', ruum[key]
                            lbx.insert(END, tobeins)

                        messagebox.showinfo('INFO', 'For More Info About Rooms You Can Press Rooms Button To Check')

                        def lbxselect():
                            global pay
                            pay = True
                            for item in lbx.curselection():
                                got = lbx.get(item)
                                var9.set(got)
                                lastvar = var9.get()
                                try:
                                    if asking:
                                        c.execute('''INSERT INTO ALBURJROOMS ('Room_No') VALUES (?)''',(str(lastvar),))
                                        conn.commit()
                                        conn.close()
                                        messagebox.showinfo('REGISTERED','THANK YOU FOR BOOKING A ROOM WITH ALBURJHOTELS YOU CAN CHECK IN FROM THE SAME DAY \n  ENJOY YOUR DAY')

                                except Exception :
                                    messagebox.showwarning('WARNING','DEAR USER YOU FIRST NEED TO PAY AMOUNT FROM PAYMENT SECTION...')
                                    pay = True

                        accbut = Button(root,text='Accept Selected Room',borderwidth=4,command=lbxselect)
                        accbut.place(x=670,y=590)

                    finalRoom = Button(root, text='FIND ROOMS', font='comicsansms 17 bold', borderwidth=7, bg='grey',
                                       command=room)
                    finalRoom.place(x=600, y=440)

                elif quest == 'no':
                    pass

            elif len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(ga_get) !=0 and num_get.isnumeric() and chil_get.isnumeric() and ad_get.isnumeric() and days_get.isnumeric() and len(num_get) != 10:
               messagebox.showwarning('WARNING','Contact Number Should Be Of 10 Digits')

            elif len(name_get) and len(mid_get) and len(last_get) and len(em_get) and len(em_get) and len(ga_get) !=0 and not num_get.isnumeric() or chil_get.isnumeric() or ad_get.isnumeric() or days_get.isnumeric():
                messagebox.showerror('ERROR','Expected Numbers In Some Of The Feilds')

            elif len(name_get) or len(mid_get) or len(last_get) or len(em_get) or len(em_get) or len(ga_get) or len(num_get) or len(chil_get) or len(ad_get) or len(days_get) == 0:
                messagebox.showerror('ERROR', 'Please Fill Out All The Fields')

        def unreserveH():
            quest = messagebox.askquestion('QUESTION','Are You Sure...Coz The Information Entered By You Will Be Lost')
            if quest == 'yes':
                var.set('First Name*')
                var1.set('Middle Name*')
                var2.set('Last Name*')
                var3.set('Contact Number*')
                var4.set('Email*')
                var5.set('Guest Address*')
                var6.set('Number Of Children*')
                var7.set('Number Of Adults*')
                var8.set('Number Of Staying Days*')
            else:
                pass


        can.create_text(680,30,text='BURJ MANAGEMENT SYSTEM DEVELOPED BY "ATIF" AND CO-DEVELOPED BY "NISHAN" AND "RATHAN"',font='comicsansms 16 bold',fill='black')

        imgHotelStatus = ImageTk.PhotoImage(Image.open('hotelstatus.jpg'))
        can.create_image(80,100,image=imgHotelStatus)
        butHotelStatus = Button(root,text='HOTEL STATUS',font='comicsansms 13 bold',borderwidth=5,command=HotelInfo)
        butHotelStatus.place(x=0,y=150)

        imgDoor = ImageTk.PhotoImage(Image.open('Door.jpg'))
        can.create_image(260,100,image=imgDoor)
        butDoor = Button(root,text='ROOMS',font='comicsansms 13 bold',borderwidth=5,command=RoomsInfo)
        butDoor.place(x=220,y=150)

        imgReserve = ImageTk.PhotoImage(Image.open('Reserve.jpg'))
        can.create_image(490,100,image=imgReserve)
        butReserve = Button(root,text='RESERVE',font='comicsansms 13 bold',borderwidth=5)
        butReserve.place(x=440,y=160)

        imgPayments = ImageTk.PhotoImage(Image.open('payments.jpg'))
        can.create_image(720,100,image=imgPayments)
        #can.create_text(720,160,text='PAYMENTS INFO',fill='black',font='comicsansms 13 bold')
        butPayments = Button(root,text='PAYMENTS INFO',font='comicsansms 13 bold',borderwidth=5,command=payment)
        butPayments.place(x=650,y=150)

        imgContacts = ImageTk.PhotoImage(Image.open('contacts.png'))
        can.create_image(950,100,image=imgContacts)
        butContacts = Button(root,text='CONTACTS',font='comicsansms 13 bold',borderwidth=5)
        butContacts.place(x=890,y=150)

        imgExit = ImageTk.PhotoImage(Image.open('exit.png'))
        can.create_image(1180,100,image=imgExit)
        butExit = Button(root,text='EXIT',font='comicsansms 13 bold',borderwidth=5,command=exit__)
        butExit.place(x=1150,y=150)

        can.create_text(430,230,text='PERSONAL INFORMATION',font='comicsansms 15 bold')

        var = StringVar()
        var.set('First Name*')
        entry = Entry(root,textvariable=var,font = 'comicsansms 9 bold')
        can.create_window(100,270,window=entry)


        var1 = StringVar()
        var1.set('Middle Name*')
        entry1 = Entry(root,textvariable=var1,font = 'comicsansms 9 bold')
        can.create_window(300,270,window=entry1)


        var2 = StringVar()
        var2.set('Last Name*')
        entry2 = Entry(root,textvariable=var2,font = 'comicsansms 9 bold')
        can.create_window(500,270,window=entry2)


        can.create_text(450,330,text='CONTACT INFORMATION',font='comicsansms 15 bold')

        var3 = StringVar()
        var3.set('Contact Number*')
        entry3 = Entry(root,textvariable=var3,font = 'comicsansms 9 bold')
        can.create_window(100,370,window=entry3)


        var4 = StringVar()
        var4.set('Email*')
        entry4 = Entry(root,textvariable=var4,font = 'comicsansms 9 bold')
        can.create_window(300,370,window=entry4)


        var5 = StringVar()
        var5.set('Guest Address*')
        entry5 = Entry(root,textvariable=var5,font = 'comicsansms 9 bold')
        can.create_window(500,370,window=entry5)



        can.create_text(450,430,text='RESERVE INFORMATION',font='comicsansms 15 bold')

        var6 = StringVar()
        var6.set('Number of Children*')
        entry6 = Entry(root,textvariable=var6,font = 'comicsansms 9 bold')
        can.create_window(100,480,window=entry6)


        var7 = StringVar()
        var7.set('Number of Adults*')
        entry7 = Entry(root,textvariable=var7,font = 'comicsansms 9 bold')
        can.create_window(300,480,window=entry7)


        var8 = StringVar()
        var8.set('Number of Staying Days*')
        entry8 = Entry(root,textvariable=var8,font = 'comicsansms 9 bold')
        can.create_window(500,480,window=entry8)



        var9 = StringVar()
        var9.set('Know Room Number Here*')
        entry9 = Entry(root,textvariable=var9,font = 'comicsansms 9 bold',width=25)
        can.create_window(700,542,window=entry9)


        reserve = Button(root,text='RESERVE',font='comicsansms 12 bold',fg='blue',bg='black',borderwidth=8,command=reserve)
        reserve.place(x=200,y=530)

        unreserve = Button(root,text='UNRESERVE',font='comicsansms 12 bold',fg='red',bg='black',borderwidth=8,command=unreserveH)
        unreserve.place(x=370,y=530)


        can.create_text(1020,220,text='FILTERS',font='comicsansms 15 bold')

        variety_beds = ['Twin','Twin XL','Full','Queen','King','DayBed','WaterBed','AirBed','Four-Poster Bed','Round Bed','Ottoman Bed','Divan','Hanging Bed','Triple Bed','Simple Bed']
        setter = StringVar()
        setter.set('Select')
        optionbed = OptionMenu(root,setter,*variety_beds)
        optionbed.config(font='comicsansms 10 bold')
        can.create_text(900,260,text='BED(S)  :  ',font='comicsansms 15 bold')
        optionbed.place(x=1100,y=240)


        AC = ['Samsung','Panasonic','Sony','Bosch','LG','Haier']
        setterAC = StringVar()
        setterAC.set('Select')
        optionac = OptionMenu(root,setterAC,*AC)
        optionac.config(font='comicsansms 10 bold')
        can.create_text(900,320,text='AC  :  ',font='comicsansms 15 bold')
        optionac.place(x=1100,y=300)


        TV = ['One plus','Sony Bravia Curved','Sony Bravia','MI','Samsung','TCL']
        setterTV = StringVar()
        setterTV.set('Select')
        optiontv = OptionMenu(root,setterTV,*TV)
        optiontv.config(font='comicsansms 10 bold')
        can.create_text(900,380,text='TV  :  ',font='comicsansms 15 bold')
        optiontv.place(x=1100,y=360)


        wifi = ['Airtel','Jio','Hathway','Private Wifi(COST EXTRA)']
        setterwifi = StringVar()
        setterwifi.set('Select')
        optionwifi = OptionMenu(root,setterwifi,*wifi)
        optionwifi.config(font='comicsansms 10 bold')
        can.create_text(900,440,text='WIFI  :  ',font='comicsansms 15 bold')
        optionwifi.place(x=1100,y=420)


        lbx = Listbox(root,bd=8,highlightthickness=20,width=70,height=5)
        bolded = font.Font(weight='bold')
        lbx.config(font=bolded)
        lbx.place(x=800,y=480)


        root.mainloop()

But = Button(login, text='LOGIN', command=Login, font='comicsansms 20 bold', borderwidth=5, bg='#F0FFFF', fg='#FF1493', padx=20)
But.place(x=145, y=558)

Butsign = Button(login, text='SIGN UP', command=sign,  font='comicsansms 20 bold', borderwidth=5, bg='#F0FFFF', fg='#FF1493', padx=20)
Butsign.place(x=850, y=555)

root.mainloop()
