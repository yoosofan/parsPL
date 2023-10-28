a=`date +%Y_%m_%d_%H_%M_%S`
mkdir $a
cp ../interpreter.py $a/interpreter.py
cp ../common.py $a/common.py
cp ../parser.py $a/parser.py
cp ../executer.py $a/executer.py
cp ../test1.psl $a/test1.psl
rsync -a --delete /home/ahmad/other/backup_dates/911205 /media/ayoosofan/
