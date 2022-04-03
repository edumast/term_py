source databased/database.py
source databased/init_data.py
data_file="databased"
while [ "$wh_tela" == true ];do
  info_blue_window=$( dialog --stdout --title "info_window" --menu "qual a informaçao" 0 0 0 "age" "$age" "name" "$name" "color_text" "$color_text")
   if [ "$info_blue_window" != " " ];then
   clear
  if [ "$tp_info" == "info" ];then
   echo -ne $info_blue_window=;eval echo '$'$info_blue_window
   wh_tela=false
   tp_info=" "
  fi
 if [ "$tp_info" == "change" ];then
echo diga o valor: |lolcat
   read change_resp
sed -i "s/$info_blue_window=.*#end/$info_blue_window=$change_resp #end/g" $data_file/database.py
tp_info=" "
wh_tela=false
  fi
   fi
   done
