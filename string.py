
#coding=utf-8

#字符串格式输出对齐

strTemp = 'xiao-Tuan-a*b1c'

print '********************'
print 'center : ' + strTemp.center(20)        #生成20个字符长度，str排中间

print 'ljust : ' + strTemp.ljust(20)         #生成20个字符长度，str左对齐

print 'rjust : ' + strTemp.rjust(20)         #生成20个字符长度，str右对齐


#大小写转换

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


strTemp = "西服穿"

print 'decode : ' + str( strTemp.decode('utf-8') ) #解码过程，将utf-8解码为unicode
























