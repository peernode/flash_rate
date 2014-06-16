#! /usr/bin/env bash

export
PYTHONPATH=/media1/liubin/test/python:/usr/local/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg:/usr/local/lib/python2.7/
site-packages/pyparsing-2.0.1-py2.7.egg:/usr/local/lib/python2.7/site-packages/matplotlib-1.3.1-py2.7-linux-x86_64.egg:/usr/local/
lib/python2.7/site-packages/nose-1.3.0-py2.7.egg:/usr/local/lib/python2.7/site-packages/tornado-3.1.1-py2.7.egg:/usr/local/lib/pyt
hon2.7/site-packages/python_dateutil-2.1-py2.7.egg:/usr/local/lib/python2.7/site-packages/six-1.4.1-py2.7.egg:/usr/local/lib/pytho
n27.zip:/usr/local/lib/python2.7:/usr/local/lib/python2.7/plat-linux2:/usr/local/lib/python2.7/lib-tk:/usr/local/lib/python2.7/lib
-old:/usr/local/lib/python2.7/lib-dynload:/usr/local/lib/python2.7/site-packages

file_time=$(date -d "2day ago" +%Y%m%d)
#file_time=20140503
file_name=logdata_${file_time}.csv

echo ${file_name}
if [ -f $file_name ]
then
# echo "hello"
   rm -rf $file_name
fi

dir=http://oxeye.funshion.com/oxeye_new/webp2p/rate/1/${file_time:0:4}/${file_time:4:2}/${file_time:6:2}/${file_name}
wget -c -t0 -T5 -w5 $dir

for dir in $(ls)
do
    if [ -d $dir ]
    then
  	(cd $dir && bash ./start.sh $file_name $file_time)
    fi
done

# send email
python2.7 send_mail.py $file_time

old_file=logdata_$(date -d "3day ago" +%Y%m%d).csv
echo old_file
if [ -f $old_file ]
then
	rm -rf $old_file
fi
