local=`echo $PWD | rev | cut -d'/' -f 1 | rev`
dd if=/dev/zero of=~/$local/term.py bs=1 count=1 seek=10 conv=notrunc
