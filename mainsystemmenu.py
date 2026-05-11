# MAIN SYSTEM RELEASE 2.1 MADE BY HASLY LICENSE GPL
# status : SUPPORT UNTIL MAY 5 2027

NEWS = "The Main system Menu Beta v.0.1 is out now for open source!! \n BETA 0.4 update What's new? \n BETA 0.4 add the TXT and.. We called it [WRITE txt] \n BETA 0.7 delete the [ area and cercumference of circle ] option from he menu 2. After it's here in the menu2 and BETA 0.6 just 5 days. \n This product is will End of live in [May 5 2027] \n update and support >> \n github Sep 5 2026 \n github Oct 5 2026 \n github Dec 26 2026 \n github Feb 28 2027 \n github May 1 2027"

Version = "RELEASE : 2.1"
LICENSE = "LICENSE : GPL"

R = 4

username = "user"
paswod = "1234"

import getpass
import os
import time
import sys
import signal
import psutil
import platform
import webbrowser

def link(url):
    print("Opening WEB GITHUB for Update...")
    time.sleep(2)
    webbrowser.open(url)
    print("TIME FOR UPDATE!")

name = "Unknow-User"

def save_log(user_name, status):
    with open("logs/login_history.txt", "a") as file:
        current_time = time.ctime()
        file.write(f"[{current_time}] User: {user_name} | status: {status}\n")

while R > 0:

    name = input("NAME : ")
    password = getpass.getpass("PASSWORD : ")

    def incorrent():
        print("Name or Password is incorrent try again")

    if name != username:
        incorrent()
    elif password != paswod:
        incorrent()
        time.sleep(5)
        R -= 1
        if R == 0:
            print("GET OUT!")
            save_log(name, "FAILED")

            exit()
        else:
            print(f"you have {R} time.")
    else:
        print("logged in!")
        print("WELCOME")
        save_log(name, "SUCCESS")
        break

print("WELCOME BACK HASLY")

def check_system():
    c = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    mu = mem.used / (1024 ** 3)
    mt = mem.total / (1024 ** 3)

    disk = psutil.disk_usage('/')
    DF = disk.free / (1024 ** 3)

    print("=" * 30)
    print(f"SYSTEM REPORT FOR {platform.node()}")
    print("=" * 30)
    print(f"CPU USAGE: {c} %")
    print(f" RAM : {mu:.2f} / {mt:.2f} GB")
    print(f"DSSK FREE : {DF:.2f} GB")
    print("=" * 30)

    usedcclt(name, "JUST CHECK COMPUTER")

    while True:
        gt = input("OUT? [Y]:  ")
        if gt.upper() == "Y":
            print("\n")
            break
        else:
            print("\n")

def usedcclt(user_name, status):
    with open("logs/MAIN_SYSTEM-history.txt", "a") as file:
        current_time = time.ctime()
        file.write(f"[{current_time}] User: {user_name} | {status}\n")


def cclt():

    gm = 1
    while gm > 0:
        n1 = int(input("number : "))
        print("=" * 30)
        print("\n 1. + \n 2. - \n 3. x \n 4. O|O")
        print("=" * 30)

        cm = input("SELECT :  ")
        n2 = int(input("number : "))

        if cm == "1":
            plus = n1 + n2
            print(f"= {plus}")
            usedcclt(name, "cclt-plus")
        elif cm == "2":
            if n1 > n2:
                minus = n1 - n2
                print(f"= {minus}")
            else:
                minus = n2 - n1
                print(f"= {minus}")

            usedcclt(name, "cclt-minus")

        elif cm == "3":
            multiply = n1 * n2
            print(f"= {multiply}")
            usedcclt(name, "cclt-multiply")

        elif cm == "4":
            divide = n1 / n2
            print(f"= {divide}")
            usedcclt(name, "cclt-divide")

        else:
            print("What? Again...")

        print("AGAIN?")
        choc = input(" [Y/n] :  ")

        if choc.upper() == "Y":
            print("okay")
        else:
            print("got it")
            time.sleep(1)
            break
    lp = 0
    while lp < 50:
        print("|")
        time.sleep(0.05)
        lp +=1
    print("CLEAR!!")
    time.sleep(2)

def v():
    print("\n " * 50)

def wdiary(wwwftxtDI):
    with open("txt/DIARY-user.txt", "a") as file:
        file.write(f"{wwwftxtDI}\n")

def wwork(wwwftxtW):
    with open("txt/WORKS-list.txt", "a") as file:
        file.write(f"{wwwftxtW}\n")

while True:
    print("\n " * 50)
    print(" ====================================")
    print("=- MAIN SYSTEM FOR RHEL[RELEASE v.2.1] -=")
    print(" ====================================")
    print("1. check_system")
    print("2. calculator")
    print("3. UPDATE -github-")
    print("4. write[.txt]")
    print("5. NEWS ABOUT THIS PROJECT")
    print("6. EXIT NOW")
    cho = input(" SELECT :  ")

    if cho == "1":
        v()
        check_system()

    elif cho == "2":
        v()
        cclt()

    elif cho == "3":
        v()
        lk = "https://github.com/HASLY95"
        link(lk)
        while True:
            print("BACK TO MENU")
            aww = input("[Y/n]:  ")
            if aww.upper() == "Y":
                break
            else:
                print("\n ")
        
    elif cho == "4":

        while True:
            v()
            print("1 DIARY")
            print("2 WORKS")
            print("3 EXIT")
            wwtxt = input("SELECT :  ")

            if wwtxt == "1":
                DIARYW = input("WRITE HERE >> ")
                wdiary(DIARYW)
                usedcclt(name, "JUST WRITE DIRAY")
                print("AGAIN? [Y/n]")
                ynn = input("SELECT :  ")
                if ynn.upper() == "Y":
                    print(" ")
                else:
                    break

            elif wwtxt == "2":
                WORKSW = input("WRITE HERE >> ")
                wwork(WORKSW)
                usedcclt(name, "JUST WRITE WORKS LIST")
                print("AGAIN? [Y/n]")
                ynn = input("SELECT :  ")
                if ynn.upper() == "Y":
                    print(" ")
                else:
                    break

            elif wwtxt == "3":
                break

        v()

    elif cho == "5":
        print(NEWS)
        print(f"VERSION >> {Version}")
        print(f"LICENSE >> {LICENSE}")
        while True:
            gt = input("OUT? [Y]:  ")
            if gt.upper() == "Y":
                print("\n")
                break
            else:
                print("\n")

    elif cho == "6":
        v()
        exit()
