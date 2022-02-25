#!/usr/bin/python
init_w=True
fixsplit="fix fix"
co_cut=(fixsplit.split)
from module import *

#os.system("tput setaf 2")
if ( dados.in_tela == 'True' ):
    init()
BOLD()
#init_style
if ( dados.in_tela == "UPDATE_DADOS" ):
    ini_tela()
while(init_w == True ):

    #command
    os.system("tput setaf 197")
    print(time.ctime()+" | "+dados.name)
    command=input(GREEN+"C:")
    if ( command == "" ):
        command="fix"
    co_cut=command.split()
    #command
    
    if ( co_cut[0] == "PROMPT"):
        PROMPT()
        color(GREEN)

    if ( co_cut[0] == "upd"):
        dados_up()

    if ( co_cut[0] == "clear" ):
        clear()
           
    if ( co_cut[0] == "shutdown" ):
        shutdown()
        exitn()
    
    if ( co_cut[0] == "reboot" ):
        clear()
        reboot()
        exitn()

    if ( brek == True ):
        break

    #comman
    if ( co_cut[0] == "comman" ):
        prin("enter | down | apps | change | VAL")
    #comman

    #enter
    if ( co_cut[0] == "enter" ):
        ts2()
        load_file(co_cut[1])
        #enter

    #down
    if ( co_cut[0] == "down" ):
        if ( co_cut[1] == "install" ):
            down_install(folder_apps,co_cut[2])       
    #down

    #change
    if ( co_cut[0] == "change" ):
        change_var="__err__"
        change_info=co_cut[1]
        valor_new=co_cut[2]
        change_var=change_info
        change(change_var,valor_new,aspa)

    #val 
    if ( co_cut[0] == "VAL" ):
        change_var=co_cut[1] 
        valor_new=co_cut[2]
        os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" databased/database.py')
    #val

    #apps
    if ( co_cut[0] == "apps" ):
        folder_apps_list="softwares/software_app/"
        os.system("ls softwares/software_app")
        os.system("tput setaf 197")
        os.system("tput bold")
    #apps    
