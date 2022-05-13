#!/usr/bin/env python
from module import *

while(1==1):
    def day():
        os.system("python3 day.py")
    day()
    time_homi=up_time()
    rose()
    print("termking | "+str(time_homi))
    COMMAND_vit=input(GREEN+"C:")
    COMMAND_vit=(COMMAND_vit+" CONTRA_BUG")
    co=COMMAND_vit.split()
    os.system("echo '"+COMMAND_vit+"'>> rest")
    sed="sed -i 's/"+co[0]+"//g' rest"
    os.system(sed)
    meuArquivo = open('rest')
    rest= meuArquivo.read()
    ev=(co[0]+"('"+rest+"')")
    os.system("echo > rest")
    os.system("chmod 755 rest")
    ev=ev.replace("\n","")
    ev=ev.replace(",","','")
    ev=ev.replace(" CONTRA_BUG","")
    ev=ev.replace("''","")
    ev=ev.replace(co[0]+"(' ",co[0]+"('")
    dir(ev)
    eval(ev)
    
