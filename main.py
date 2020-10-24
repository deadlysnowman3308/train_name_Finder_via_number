# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests as r
import os, sys, json, time
from os import system
from sys import exit


os.system("cls" if os.name == "nt" else "clear")


def load_animation():

    load_str = "starting train database console..."
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0
    while counttime != 44:
        time.sleep(0.1)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ""
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    load_animation()
os.system("cls" if os.name == "nt" else "clear")

a = r.get(
    "https://rawcdn.githack.com/deadlysnowman3308/train_name_Finder_via_number/6a26cbe905b92f9d1f2d2f725d1d5abd9bc5a17f/Train_names.json"
)

b = a.json()



class banner2:
    def __init__(self):
        pass
        print(
            r"""            
                  _______        _         _____        _        
                 |__   __|      (_)       |  __ \      | |       
                    | |_ __ __ _ _ _ __   | |  | | __ _| |_ __ _ 
                    | | '__/ _` | | '_ \  | |  | |/ _` | __/ _` |
                    | | | | (_| | | | | | | |__| | (_| | || (_| |
                    |_|_|  \__,_|_|_| |_| |_____/ \__,_|\__\__,_|
                                                 
            """
        )


banner2()


print("\n\n\n")

xy = str(input("\t$ Please enter TRAIN number: ") or "12312")

os.system("cls" if os.name == "nt" else "clear")

print("\n\n")

banner2()


def process_bar():
    pass
    system(
        "mode con: cols=78 lines=20"
        if os.name == "nt"
        else "resize -s 90 150 > /dev/null"
    )
    os.system("cls" if os.name == "nt" else "clear")
    print("\n\n\n\n\n\t\t\t  Searching Please WAIT...  ")
    print("\n\n\n\n")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = [
        "[■□□□□□□□□□]",
        "[■■□□□□□□□□]",
        "[■■■□□□□□□□]",
        "[■■■■□□□□□□]",
        "[■■■■■□□□□□]",
        "[■■■■■■□□□□]",
        "[■■■■■■■□□□]",
        "[■■■■■■■■□□]",
        "[■■■■■■■■■□]",
        "[■■■■■■■■■■]",
    ]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r\t\t\t\t" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


process_bar()


os.system("cls" if os.name == "nt" else "clear")
print("\n\n\n")
try:
    print("\n\tYour train Number/Name:  " + b[f"{xy}"])
except KeyError:
    print("    Sorry, " + os.getlogin() + " try again")
print("\n\n\n\n\n\n\n\n")

input("\t[ Press ENTER for exit ]")
os.system("cls" if os.name == "nt" else "clear")

# input("Please Press ENTER for exit")jkjhj
