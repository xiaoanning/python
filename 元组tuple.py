
#coding=utf-8

'''
    不可变序列-----元组 tuple
    元组通过圆括号中用逗号分隔的项目定义,不可以添加和删除元组.
    
    
    基本操作：
    索引
    切片
    循环
    长度
    包含
    PS：循环，range，continue 和 break
    
'''

name_tuple = ('a' , 'b' , 1 , 'a' )

print 'type : ' + str(type(name_tuple))

print 'count : ' + str(name_tuple.count('a'))

print 'index : ' + str(name_tuple.index('a'))
