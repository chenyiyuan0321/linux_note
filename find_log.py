#1.查询日志中含有某个关键字的信息
cat app.log |grep 'error'
#2.查询日志尾部最后10行的日志
tail  -n  10  app.log 
#3.查询10行之后的所有日志
tail -n +10 app.log  
#4.查询日志文件中的头10行日志
head -n 10  app.log  
#5.查询日志文件除了最后10行的其他所有日志
head -n -10  app.log 
#6.查询日志中含有某个关键字的信息,显示出行号(在1的基础上修改)
cat -n  app.log |grep 'error'
#7.显示102行,前10行和后10行的日志
cat -n app.log |tail -n +92|head -n 20
#8.根据日期时间段查询(前提日志总必须打印日期,先通过grep确定是否有该时间点)
sed -n '/2014-12-17 16:17:20/,/2014-12-17 16:17:36/p'  app.log
#9.使用more和less命令(分页查看,使用空格翻页)
cat -n app.log |grep "error" |more
#10.吧日志保存到文件
cat -n app.log |grep "error"  > temp.txt
