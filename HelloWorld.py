
#coding=utf-8

'''
    代码的缩紧
同一个代码块中的每一行都必须和其他所有行缩进相同的制表符或是空格；这是语言强制规定的。换句话说，不要混合使用制表符和空格
'''


#变量

#整型(integers)

x = 5

print 'x = ' + str(x)

x = x + 5

print 'x = ' + str(x)

print '==================================== 整型(integers) 结束'

#字符串型(strings)
strTemp = "hello world"

print "strTemp = " + strTemp

print '==================================== 字符串型(strings) 结束'

#整数和字符串互换

x = 5

print 'x = ' + str(x)

strTemp = '15'

x = int(strTemp)

print 'x = ' + str(x)

print '==================================== 整数和字符串互换 结束'

#布尔类型(boolean) True False

boolTemp = True

print '布尔 = ' + str(boolTemp)

print '==================================== 布尔类型(boolean) True False 结束'


#if 语句

if x == 15 :
    print 'x == 15'
if x != 15 :
    print 'x != 15'

print '==================================== if 语句 结束'


#操作符

'''
        ==
        !=
        >
        <
        >=
        <=
'''

#for循环
for x in range(2 , 4) : #range(2) 0 1  range(2,4) 2 3
    print x


print '==================================== for循环 结束'


#while循环

x = 0

while (x < 3) :

    print 'while : x = ' + str(x)
    x += 1

    if x == 2 :
        break

print '==================================== while循环 结束'


#函数


def add(a,b):

    return a + b

print 'add(2,1)+3 = ' + str(add(2,1) + 3)

print '==================================== 函数 结束'


#捕获用户输入

name = raw_input('what is your name ? ') #控制台输入

print 'hello , ' + name

print '==================================== 捕获用户输入 结束'


#导入 模块

import random

print random.randint(0,3)

print '==================================== 导入 模块 结束'


#创建 打开py文件

'''
    创建 touch guess.py
    打开 open -t guess.py
'''








