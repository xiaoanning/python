#coding=utf-8

'''
    List是处理和存放一组数据的列表
    
    基本操作：
    
    索引
    切片
    追加
    删除
    长度
    循环
    包含


PS：循环，range，continue 和 break
'''

list1 = [1,2]
list2 = [22,'23']

print 'cmp : ' + str ( cmp(list1, list2))    #比较两个列表的元素,两个元素相同返回0，前大后小返回1，前小后大返回-1

print 'len : ' + str ( len(list1) ) # 列表元素个数

print 'max : ' + str ( max(list2) )         #返回列表元素最大值
print 'min : ' + str(min(list2))              #返回列表元素最小值
print 'list : ' +str( list('var'))                #将元素转换为列表
del list1[1]                  # 删除指定下标的元素
del list2[0:2]                #删除指定下标范围的元素

print 'del : ' + str(list1) + ' ' + str(list2)



#List操作包含以下方法:

list2.append('2')        #append方法用于在列表的尾部追加元素，参数'var'是插入元素的值
print 'append : ' + str(list2)


list2.insert(1,'22')    #用于将对象插入到列表中，俩个参数，第一个是索引位置，第二个插入的元素对象.
print 'insert : ' + str(list2)

temp = list2.pop() #返回列表最后一个元素，并从List中删除.
print 'pop : ' + str(list2) + ' ' + temp

list2 = [1,'2',3,'22']

temp = list2.pop(0) #返回列表索引的元素，并删除.
print 'pop : ' + str(list2) + ' ' + str(temp)



print 'count : ' + str( list2.count(22)) #该元素在列表中出现的个数


print 'index : ' + str( list2.index('22')) #取出元素的位置(下标)，无则抛出异常.

list2.remove('22')
print 'remove : ' + str(list2) #remove方法用于从列表中移除第一次的值(值如果有重复则删除第一个)

list2 = [22,24,54,21,'23']
list2.sort()
print 'sort : ' + str(list2) #排序

list2.reverse()
print 'reverse : ' + str(list2) # 倒序

list2.extend(list1)
print 'extend : ' + str(list2) # extend方法用于将两个列表合并，将list1列表的值添加到L列表的后面。


#List 中 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

print 'list + : ' + str(list2 + list1) # 组合
print 'str + : ' + str('list2' + 'list1') # 组合

print 'list * : ' + str('1'*4) #重复
print 'str * : ' + str([1]*4) #重复

print 'in : ' + str(1 in list2) #元素是否存在于列表中

for x in list2 :
    print '遍历 ： ' + str(x)

#列表截取

strTemp = '1234567'
print '第几个元素 ： ' + str(list2[1]) + ' ' + str(strTemp[1])
print '倒数第几个元素 ： ' + str(list2[-1]) + ' ' + str(strTemp[-1])
print '从第几个元素开始 ： ' + str(list2[1:]) + ' ' + str(strTemp[1:])
print '第几个元素到第几个元素 ： ' + str(list2[0:2]) + ' ' + str(strTemp[0:2])



    
    
    
    
