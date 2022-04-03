#!/usr/bin/env python3
from module import *
#############
#edumast,inc.
#############
from databased.database import *
import os
import time

#err1=error

os.system("tput bold")

time.sleep(0.1)
print("checking system status")
time.sleep(0.1)
if ( name == "" ):
    print("name=ERROR!")
    err1=True
else:
    print("name=OK")
time.sleep(0.1)
if ( age == "" ):
    print("age=ERROR!")   
    err1=True
else:
    print("age=OK")
time.sleep(0.1)
press_space=input("press space!")
os.system("clear")
os.system("./term.py")

