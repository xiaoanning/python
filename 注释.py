
'''
   如果开头不声明保存编码的格式是什么，那么会默认使用ASKII码保存文件，这时如果代码中有中文就会出错了，即使中文是包含在注释里面的 
   
   #coding=utf-8
   或者：
   #coding=gbk
'''
#coding=utf-8


#如果要加汉语注释必须 要加 语句#coding=utf-8 单词之间不能有空格

#单行注释

'''
        多行注释  三个引号中间写注释
'''


str = "hello world"

str = "str = " + str

print "str = " + str
