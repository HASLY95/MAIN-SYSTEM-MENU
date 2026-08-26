# MAIN SYSTEM RELEASE 2.1 MADE BY HASLY LICENSE GPL
# status : SUPPORT UNTIL MAY 5 2027

NEWS ="The Main system Menu Beta v.0.1 is out now for open source!! \n BETA 0.4 update What's new? \n BETA 0.4 add the TXT and.. We called it [WRITE txt] \n BETA 0.7 delete the [ area and circumference of circle ] option from menu 2. After it's here in the menu2 and BETA 0.6 just 5 days. \n This product will reach End of Life on [May 5 2027] \n BIG update and support >> \n github Sep 5 2026 \n github Oct 5 2026 \n github Dec 26 2026 \n github Feb 28 2027 \n github May 1 2027"

Version = "BETA    : 2.4.3"
LICENSE = "LICENSE : GPL"

R = 4
PW = 4
IC = 0

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
def v():
    os.system('cls' if os.name == 'nt' else 'clear')


def link(url):
    print("Opening WEB GITHUB for Update...")
    time.sleep(2)
    webbrowser.open(url)
    print("TIME FOR UPDATE!")

name = "Unknown-User"

def save_log(user_name, status):
    with open("logs/login_history.txt", "a") as file:
        current_time = time.ctime()
        file.write(f"[{current_time}] User: {user_name} | status: {status}\n")

while True:
    v() 
    print("//====================================--")
    print("||   PTMENU ----  MAIN OPTION..   =")
    print("//====================================---..")
    print("LOGIN [1]")
    print("EXIT NOW [E]")
    mmo = input("SELECT >>  ")

    if mmo == "1":
        break
    else:
        exit()

while True:
    v()
    if R == 0 or PW == 0:
        print(f"SORRY, IT'S INCORRECT {IC} TIMES")
        time.sleep(1)
        exit()
    name = input("USERNAME : ")
    if name != username:
        print("NAME IS INCORRECT!")
        IC += 1
        if R == 1:
            R -= 1
            if R == 0:
                print("SORRY,USERNAME IT'S INCORRECT 4 TIMES")
                time.sleep(1)
                save_log(username, "FAILED-USERNAME")
                exit()
        else:
            R -= 1
            if R == 1:
                print(f"ONLY {R} ROUND LEFT.")
            else:
                print(f"ONLY {R} ROUNDS LEFT.")
        time.sleep(1)
    else:
        password = getpass.getpass("PASSWORD : ")
        if password != paswod:
            IC += 1
            if PW == 1:
                R -= 1
                if PW == 0:
                    print("SORRY,PASSWORD IT'S INCORECT 4 TIMES")
                    time.sleep(1)
                    save_log(username, "FAILED-PASSWORD")
                    exit()
            else:
                PW -= 1
                if PW == 1:
                    print(f"ONLY {PW} ROUND LEFT.")
                else:
                    print(f"ONLY {PW} ROUNDS LEFT.")
        else:
            save_log(username, "SUCCESS")
            break


def usedcclt(user_name, status, elapsed_time=None):
    with open("logs/PTMENU-logs.txt", "a") as file:
        current_time = time.ctime()
        if elapsed_time is not None:
            file.write(f"[{current_time}] User: {user_name} | {status} | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)\n")
        else:
            file.write(f"[{current_time}] User: {user_name} | {status}\n")

def check_system():
    start_time = time.perf_counter()
    c = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    mu = mem.used / (1024 ** 3)
    mt = mem.total / (1024 ** 3)

    disk = psutil.disk_usage('/')
    DF = disk.free / (1024 ** 3)

    elapsed_time = time.perf_counter() - start_time

    print("=" * 30)
    print(f"SYSTEM REPORT FOR {platform.node()}")
    print("=" * 30)
    print(f"CPU USAGE: {c} %")
    print(f" RAM : {mu:.2f} / {mt:.2f} GB")
    print(f"DISK FREE : {DF:.2f} GB")
    print("=" * 30)
    print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")

    usedcclt(name, "JUST CHECK COMPUTER", elapsed_time)

    while True:
        gt = input("OUT? [Y]:  ")
        if gt.upper() == "Y":
            print("\n")
            break
        else:
            print("\n")


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
            start_time = time.perf_counter()
            plus = n1 + n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {plus}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-plus", elapsed_time)
        elif cm == "2":
            start_time = time.perf_counter()
            if n1 > n2:
                minus = n1 - n2
                print(f"= {minus}")
            else:
                minus = n2 - n1
                print(f"= {minus}")
            elapsed_time = time.perf_counter() - start_time
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-minus", elapsed_time)

        elif cm == "3":
            start_time = time.perf_counter()
            multiply = n1 * n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {multiply}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-multiply", elapsed_time)

        elif cm == "4":
            start_time = time.perf_counter()
            divide = n1 / n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {divide}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-divide", elapsed_time)

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

def wdiary(wwwftxtDI):
    with open("txt/DIARY-user.txt", "a") as file:
        file.write(f"{wwwftxtDI}\n")

def wwork(wwwftxtW):
    with open("txt/WORKS-list.txt", "a") as file:
        file.write(f"{wwwftxtW}\n")

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
DE = "\033[0m"

while True:
    v()
    print(f"{BLUE}nnnnnnnnnnn        ttt")
    print(f"{BLUE}nnnnnnnnnnnnn      ttt")
    print(f"{GREEN}nnn       nnn      ttt")
    print(f"{GREEN}nnn      nnnn   ttttttttt")
    print(f"{GREEN}nnnnnnnnnnn     ttttttttt")
    print(f"{YELLOW}nnnnnnnnnn         ttt")
    print(f"{YELLOW}nnn                ttt")
    print(f"{YELLOW}nnn                ttt    tttt")
    print(f"{YELLOW}nnn                tttt    ttt")
    print(f"{RED}nnn                 tttt  tttt")
    print(f"{RED}nnn        {DE}MENU{RED}      tttttttt{DE}")
    print(" ====================================")
    print(f"=- WELCOME TO PTMENU [{Version}] -=")
    print(" ====================================")
    print("[E] EXIT")
    print("1. check_system")
    print("2. calculator")
    print("3. UPDATE -github-")
    print("4. write[.txt]")
    print("5. NEWS ABOUT THIS PROJECT")
    print("[A] ADVANCED OPTIONS")
    cho = input(" SELECT :  ")

    if cho == "1":
        v()
        check_system()

    elif cho == "2":
        v()
        cclt()

    elif cho == "3":
        v()
        lk = "https://github.com/HASLY95/PTMENU"
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
                start_time = time.perf_counter()
                wdiary(DIARYW)
                elapsed_time = time.perf_counter() - start_time
                print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
                usedcclt(name, "JUST WRITE DIARY", elapsed_time)
                print("AGAIN? [Y/n]")
                ynn = input("SELECT :  ")
                if ynn.upper() == "Y":
                    print(" ")
                else:
                    break

            elif wwtxt == "2":
                WORKSW = input("WRITE HERE >> ")
                start_time = time.perf_counter()
                wwork(WORKSW)
                elapsed_time = time.perf_counter() - start_time
                print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
                usedcclt(name, "JUST WRITE WORKS LIST", elapsed_time)
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

    elif cho.upper() == "A":
        v()
        H = input("ARE YOU SURE? [y/N]>> ")
        if H.upper() == "Y":
            print("OPENING -- MENU 2 Advanced option -- ...")
            print("OPENED")
            time.sleep(1)
            print("username >> admin")
            print("password >> 12344321")
            time.sleep(3.2)
            os.system("python menu/Advanced.py")
        else:
            print("\n")
    elif cho.upper() == "E":
        v()
        exithah = input("ARE YOU SURE? [y/N] >> ")
        if exithah.upper() == "Y":
            exit()
        else:
            print("\n ")
    else:
        print("WANT TO DONATE!?")
        time.sleep(1)
        print("AWWWWW Did you juat say NO?")
        time.sleep(1)
        print("OK... :[ ")
        time.sleep(1)


