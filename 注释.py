
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


'''
    脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单
    
    #!/usr/bin/Python是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器；
    #!/usr/bin/env python这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作。
    #!/usr/bin/python相当于写死了python路径;
    #!/usr/bin/env python会去环境设置寻找python目录,推荐这种写法
'''
