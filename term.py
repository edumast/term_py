#!/usr/bin/env python3

#init
init_w=True
#init

#fix
fixsplit="fix fix"
co_cut=(fixsplit.split)
#fix

#module_base
from module import *
#module_base

#time
timeN = datetime.now()
#time

#init_tela
if ( dados.init_window == True ):
    if ( dados.in_tela == 'True' ):
        init()
    if ( dados.in_tela == 'tarde' ):
        tarde=time_of_day()
        if ( tarde == 'dia' ):
            adTarde="Bom"
        else:
            adTarde="Boa"
        print_slow(RED+adTarde+" "+tarde+" "+dados.name+"!")
        print("")
BOLD()
#init_tela

#init_style
if ( dados.init_window == False ):
    ini_tela()
while(init_w == True ):
    
    #command
    command=Read_command()
    co_cut=command.split()

    #command

    #update
    if ( co_cut[0] == "update" ):
        os.system("./update/update_software")
    #update

    #PROMPT
    if ( co_cut[0] == "PROMPT"):
        PROMPT()
        color(GREEN)
    #PROMPT
    
    #upd
    if ( co_cut[0] == "upd"):
        dados_up()
    #upd

    #clear
    if ( co_cut[0] == "clear" ):
        clear()
    #clear

    #shutdown
    if ( co_cut[0] == "shutdown" ):
        shutdown()
        exitn()
    #shutdown

    #reboot
    if ( co_cut[0] == "reboot" ):
        clear()
        reboot()
        exitn()
    #reboot

    #brek
    if ( brek == True ):
        break
    #brek

    #comman
    if ( co_cut[0] == "comman" ):
        prin("enter | down | apps | change | VAL | PROMPT | upd | clear | shutdown | color")
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
        VAL(change_var,valor_new)      
    #val

    #apps
    if ( co_cut[0] == "apps" ):
        apps_list()
        rose()
        BOLD()
    #apps 

    #color_text
    if ( co_cut[0] == "color" ):
        color=co_cut[1]
        os.system('sed -i "s/color_text=.*#end/color_text='+co_cut[1]+' #end/g" databased/init_data.py')
    #color_text
