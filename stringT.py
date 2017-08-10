
#coding=utf-8

'''
字符串常用功能
    移除空白
    分割
    长度
    索引
    切片
'''
import sys

#字符串比较

print "字符串比较 : " + str("" == "") + "    " + str("1" == "")

#字符串拼接
print "字符串拼接 " + str("1%s3 姓名"%1)
print "字符串拼接 " + str("1{}3 姓名{}").format(1,"肖湍")

#字符串格式输出对齐

strTemp = 'xiao-Tuan-a*b1c'

print '******************** 字符串格式输出对齐 '
print 'center : ' + strTemp.center(20)        #生成20个字符长度，str排中间

print 'ljust : ' + strTemp.ljust(20)         #生成20个字符长度，str左对齐

print 'rjust : ' + strTemp.rjust(20)         #生成20个字符长度，str右对齐


#大小写转换
print '******************** 大小写转换 '

print 'upper : ' + strTemp.upper()           #转大写

print 'lower : ' + strTemp.lower()           #转小写

print 'capitalize : ' + strTemp.capitalize()      #字符串首为大写，其余小写  是字符串首字母大写 不是单词首字母大写

print 'swapcase : ' + strTemp.swapcase()        #大小写对换

print 'title : ' + strTemp.title()          #以分隔符为标记，首字符为大写，其余为小写

#字符串条件判断

strTemp = 'zimushuzi1'
strTemp2 = 'bushizimushuzi*'

print 'isalnum : ' + str(strTemp.isalnum()) + ' ' + str(strTemp2.isalnum())  #是否全是字母和数字，并至少有一个字符

strTemp = '123'
strTemp2 = '00o'
print 'isdigit : ' + str(strTemp.isdigit()) + ' ' + str(strTemp2.isdigit()) #是否全是数字，并至少有一个字符


strTemp = 'ad'
strTemp2 = '12sf'
print 'isalpha : ' + str(strTemp.isalpha()) + ' ' + str(strTemp2.isalpha()) #是否全是字母，并至少有一个字符

strTemp = 'ad'
strTemp2 = '12sfA'
print 'islower : ' + str(strTemp.islower()) + ' ' + str(strTemp2.islower()) #是否全是小写，当全是小写和数字一起时候，也判断为True

strTemp = 'AF'
strTemp2 = '12sfA'
print 'isupper : ' + str(strTemp.isupper()) + ' ' + str(strTemp2.isupper()) #是否全是大写，当全是大写和数字一起时候，也判断为True

strTemp = '  '
strTemp2 = '12sfA'
print 'isspace : ' + str(strTemp.isspace()) + ' ' + str(strTemp2.isspace()) #是否全是空白字符，并至少有一个字符

strTemp = 'The World'
strTemp2 = '12sfA'
print 'istitle : ' + str(strTemp.istitle()) + ' ' + str(strTemp2.istitle()) #所有单词字首都是大写，标题

strTemp = 'str The World '
strTemp2 = '12sfA'
print 'startswith : ' + str(strTemp.startswith('str')) + ' ' + str(strTemp2.startswith('str')) #判断字符串以'str'开头

strTemp = 'sstr     The Worldstr 1ss'
strTemp2 = '12sfA'
print 'endswith : ' + str(strTemp.endswith('str'))  + ' ' + str(strTemp2.endswith('str')) #判断字符串以'str'结尾


#字符串搜索定位与替换

print 'find : ' + str( strTemp.find('t') ) #查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引

print 'rfind : ' + str( strTemp.rfind('t') ) #返回的索引是最后一次匹配的 不区分大小写


print 'index : ' + str( strTemp.index('t') ) #同find类似,返回第一次匹配的索引值

# print 'index : ' + str( strTemp.index('z') ) #如果没有匹配则报错  程序终止

print 'rindex : ' + str( strTemp.rindex('t') ) #返回的索引是最后一次匹配的 不区分大小写

print 'count : ' + str( strTemp.count('r') ) #字符串中匹配的次数

print 'replace : ' + str( strTemp.replace('The' , 'replace'))  #匹配替换  区分大小写
print 'replace : ' + str( strTemp.replace('r' , 'R' , 2 ))  #第一个被替换 第二个新内容 第三个替换的个数

print 'strip : ' + str( strTemp.strip('s') ) #删除字符串首尾匹配的字符(必须是开头和结尾的字符)，通常用于默认删除回车符
print 'lstrip : ' + str( strTemp.lstrip('s') ) #左匹配
print 'rstrip : ' + str( strTemp.rstrip('s') ) #右匹配


print 'expandtabs : ' + str( strTemp.expandtabs() ) #把制表符转为空格
print 'expandtabs : ' + str( strTemp.expandtabs(2) ) #制定空格数

#字符串编码与解码   编解码格式要一致

reload(sys) #没有这个方法  setdefaultencoding 这个方法会报错
sys.setdefaultencoding('utf-8')  #没有这个方法 下面的编码会报错

strTemp = "西服穿"

print strTemp

print 'decode : ' + str( strTemp.decode('utf-8') ) #解码过程，将utf-8解码为unicode

print 'encode : ' + str( strTemp.decode('utf-8').encode('gbk')) #编码过程，将unicode编码为gbk  乱码
print 'encode : ' + str( strTemp.decode('utf-8').encode('utf-8')) #编码过程，将unicode编码为utf-8

#字符串分割变换

strTemp = 'Learn string -!'

print 'join : ' + str( '-'.join(strTemp) )  #L-e-a-r-n- -s-t-r-i-n-g- ---!

li = ['learn','string']
print 'join : ' + str( '-'.join(li) )

print 'split : ' + str ( strTemp.split(' ') )
print 'split : ' + str ( strTemp.split(' ',1) )

print 'rsplit : ' + str ( strTemp.rsplit(' ') )
print 'rsplit : ' + str ( strTemp.rsplit(' ',1) )  #从右边开始分割

print 'splitlines : ' + str ( strTemp.splitlines() )  #string 转换为array

print 'partition : ' + str ( strTemp.partition(' ') )  #按字符串分割 分割的结果包含该分割符
print 'rpartition : ' + str ( strTemp.rpartition(' ') )



#字符串格式化
'''
Python的字符串格式化有两种方式: 百分号方式、format方式

百分号的方式相对来说比较老，而format方式则是比较先进的方式，企图替换古老的方式，目前两者并存。

1、百分号方式

(name)      可选，用于选择指定的key
flags          可选，可供选择的值有:width         可选，占有宽度
+       右对齐；正数前加正好，负数前加负号；
-        左对齐；正数前无符号，负数前加负号；
空格    右对齐；正数前加空格，负数前加负号；
0        右对齐；正数前无符号，负数前加负号；用0填充空白处
.precision   可选，小数点后保留的位数

typecode    必选
s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
o，将整数转换成 八  进制表示，并将其格式化到指定位置
x，将整数转换成十六进制表示，并将其格式化到指定位置
d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
F，同上
g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
%，当字符串中存在格式化标志时，需要用 %%表示一个百分号
注：Python中百分号格式化是不存在自动将整数转换成二进制表示的方式

常用格式化：

 tpl = "i am %s" % "alex"
   
 tpl = "i am %s age %d" % ("alex", 18)
   
 tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
 
 tpl = "percent %.2f" % 99.97623    #打印浮点数
  
 tpl = "i am %(pp).2f" % {"pp": 123.425556, }
 
 tpl = "i am %.2f %%" % {"pp": 123.425556, }    #打开百分比
 

示例：

1、%s 可以字符串拼接

1 msg='i am %s my hobby is %s' % ('lhf','alex')
2 print(msg)
执行结果：

1 i am lhf my hobby is alex
 

2、%s 可以按收任何类型（ 数字对应字符串）

1 msg='i am %s my hobby is %s' % ('lhf',1)
2 print(msg)
执行结果：

1 i am lhf my hobby is 1
 

3、%s 可以字符串接收列表

1 msg='i am %s my hobby is %s' % ('lhf',[1,2])
2 print(msg)
执行结果：

1 i am lhf my hobby is [1, 2]
 

4、%s传字符串或任何值， %d只能接收数字

1 name='lhf'
2 age=19
3 msg='i am %s my hobby is %d' % (name,age)  #age可以用%d or %s,但用%s程序可读性差
4 print(msg)
执行结果：

1 i am lhf my hobby is 19
 

5、%d 只能接收数字类型，不能接收列表

1 # %d 只能按收数字类型
2 msg='i am %s my hobby is %d' % ('lhf',1)
3 print(msg)
执行结果：

1 i am lhf my hobby is 1
 

6、%d 不能接收列表类型,会报错

1 msg='i am %s my hobby is %d' % ('lhf',[1,2])
2 print(msg)
执行结果：

1 Traceback (most recent call last):
2   File "D:/python/day5/format_type.py", line 14, in <module>
3     msg='i am %s my hobby is %d' % ('lhf',[1,2])
4 TypeError: %d format: a number is required, not list
 

7、打印浮点数

1 tpl = "percent %.2f" % 99.976234444444444444
2 print(tpl)
执行结果：

1 percent 99.98
 

8、打印百分比

1 tpl = 'percent %.2f %%' % 99.976234444444444444
2 print(tpl)
执行结果：

1 percent 99.98 %
 

9、左边打印空格

1 msg='i am %(name)+60s my hobby is alex' %{'name':'lhf'}
2 print(msg)
执行结果：

1 i am                                                          lhf my hobby is alex
 

10、打印空格加颜色(黄色）

1 msg='i am \033[43;1m%(name)+60s\033[0m my hobby is alex' %{'name':'lhf'}
2 print(msg)
执行结果：

1 i am                                                          lhf my hobby is alex
 

19、不用格式化的方式

1 print('root','x','0','0',sep=':')
2 print('root'+':'+'x'+':'+'0','0')
执行结果：

1 root:x:0:0
2 root:x:0 0
 

2、Format 方式

[[fill]align][sign][#][0][width][,][.precision][type]
fill           【可选】空白处填充的字符
align        【可选】对齐方式（需配合width使用）
<，内容左对齐
>，内容右对齐(默认)
＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
^，内容居中
sign         【可选】有无符号数字
+，正号加正，负号加负；
 -，正号不变，负号加负；
空格 ，正号空格，负号加负；
#            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
，            【可选】为数字添加分隔符，如：1,000,000
width       【可选】格式化位所占宽度
.precision 【可选】小数位保留精度
type         【可选】格式化类型
传入” 字符串类型 “的参数
s，格式化字符串类型数据
空白，未指定类型，则默认是None，同s
传入“ 整数类型 ”的参数
b，将10进制整数自动转换成2进制表示然后格式化
c，将10进制整数自动转换为其对应的unicode字符
d，十进制整数
o，将10进制整数自动转换成8进制表示然后格式化；
x，将10进制整数自动转换成16进制表示然后格式化（小写x）
X，将10进制整数自动转换成16进制表示然后格式化（大写X）
传入“ 浮点型或小数类型 ”的参数
e， 转换为科学计数法（小写e）表示，然后格式化；
E， 转换为科学计数法（大写E）表示，然后格式化;
f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
g， 自动在e和f中切换
G， 自动在E和F中切换
%，显示百分比（默认显示小数点后6位）
 常用格式化：

 1 tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')
 2   
 3 #必须一一对应，否则会报错
 4 tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
 5   
 6 
 7 tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
 8   
 9 
10 tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
11   
12 
13 tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
14   
15 
16 tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
17                                                      ** 代表传字典
18 
19 tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
20   
21 
22 tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
23              s 代表字符串 d 代表整数
24 
25 tpl = "i am {:s}, age {:d}".format(*["seven", 18])
26                                    * 代表列表
27 
28 tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
29   
30 
31 tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
32  
33 
34 tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
35                 2进制 8进制 10进制  x与X: 16进制 %：百分比
36 
37 tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
38  
39 
40 tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
41  
42 
43 tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

示例：

ps1:

1 tpl = "i am {0}, age {1}, really {2}".format("seven", '18','alex')
2 print(tpl)
执行结果：

1 i am seven, age 18, really alex
 

ps2:

1 tpl = "i am {2}, age {1}, really {0}".format("seven", '18','alex')
2 print(tpl)
执行结果：

1 i am alex, age 18, really seven
 

ps3: 传字典的方式

1 tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
2 print(tpl)
执行结果：

1 i am seven, age 18, really seven
 

ps4: ** 传字典的方式 (跟ps3的方式是一样的）

1 tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
2 print(tpl)
执行结果：

1 i am seven, age 18, really seven
 

ps5:  * 代表：列表

1 tpl = "i am {:s}, age {:d}".format(*["seven", 18])
2 print(tpl)
执行结果：

1 i am seven, age 18
 

ps6:

1 tpl = "i am {:s}, age {:d}".format("seven", 18) #["seven", 18]
2 print(tpl)
执行结果：

1 i am seven, age 18
 

ps7:

1 l=["seven", 18]
2 tpl = "i am {:s}, age {:d}".format('seven',18)
3 print(tpl)
执行结果：

1 i am seven, age 18
 

ps8:   2进制 8进制 10进制 x与X: 16进制 %：百分比

1 tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%},{}".format(15, 15, 15, 15, 15, 15.87623, 2)
2 print(tpl)
执行结果：

1 numbers: 1111,17,15,f,F, 1587.623000%,2

'''

