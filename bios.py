from module import *
#############
#edumast,inc.
#############
from databased.database import *
import os
import time

#err1=dados error

os.system("tput bold")

time.sleep(0.1)
print("checking system status")
time.sleep(0.1)
if ( dados.name == "" ):
    print("dados.name=ERROR!")
    err1=True
else:
    print("dados.name=OK")
time.sleep(0.1)
if ( dados.age == "" ):
    print("dados.age=ERROR!")   
    err1=True
else:
    print("dados.age=OK")
time.sleep(0.1)
press_space=input("press space!")
os.system("clear")
os.system("./term.py")

