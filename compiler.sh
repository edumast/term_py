sed ':a;N;s/\n/(),/g;ta' t.py > tt.py
cat tt.py
sed -i 's/)()/)/g' tt.py
cat tt.py
sed -i 's/,;(),/\n/g' tt.py
sed -i 's/;(),/\n/g' tt.py
sed -i 's/;()/\n/g' tt.py
sed -i '1s/^/from module import *\n/g' tt.py
