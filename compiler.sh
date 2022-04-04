arq1="t.py"
arq2="tt.py"
sed ':a;N;s/\n/(),/g;ta' $arq1 > $arq2
sed -i 's/)()/)/g' $arq2
sed -i 's/,;(),/\n/g' $arq2
sed -i 's/;(),/\n/g' $arq2
sed -i 's/;()/\n/g' $arq2
sed -i 's/;/\n/g' $arq2
sed -i '1s/^/from module import *\n/g' $arq2
sed -i '1s/^/#!\/usr\/bin\/env python3\n/g' $arq2
tput bold
tput setaf 1
cat tt.py
tput setaf 3
read space
if [ "$space" == "+" ];then
  tput setaf 2
  cat t.py
  read space
fi 
