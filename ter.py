#!/usr/bin/env python
from module import *

while(1==1):
    COMMAND_vit=input("C:")
    COMMAND_vit=COMMAND_vit
    co=COMMAND_vit.split()
    os.system("echo '"+COMMAND_vit+" CONTRA_BUG'>> rest")
    sed="sed -i 's/"+co[0]+"//g' rest"
    os.system("cat rest")
    os.system(sed)
    meuArquivo = open('rest')
    rest= meuArquivo.read()
    ev=(co[0]+"('"+rest+"')")
    os.system("echo > rest")
    ev=ev.replace("\n","")
    ev=ev.replace(",","','")
    ev=ev.replace(" CONTRA_BUG","")
    ev=ev.replace("''","")
    ev=ev.replace(co[0]+"(' ",co[0]+"('")
    print(ev)
    eval(ev)
    
