import time,sys,os
from datetime import datetime

name="Edu"

RED = '\033[91m' #RED

#print_slow
def print_slow(print_slow):
    m = str(print_slow)
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
#print_slow

def definy_time():
     time = datetime.now()
     return time
#set_time_day
def time_of_day():
    time=definy_time()
    if ( time.hour >= 5 ):
        time_day="dia"
    if ( time.hour >=12 ):
        time_day="tarde"
    if ( time.hour >= 18 ):
        time_day="noite"
    return time_day
#set_time_day

tarde=time_of_day()
if ( tarde == 'dia' ):
    adTarde="Bom"
else:
    adTarde="Boa"
os.system("tput bold")
print_slow(RED+adTarde+" "+tarde+" "+name+"!")
print("")

