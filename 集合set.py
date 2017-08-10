
#coding=utf-8

'''

set是一个无序且不重复的元素集合

a &b 交集
a | b 并集
a ^ b 取出非交集的数
a -b a里面有b里面没有
'''

a = set([1,2,1,4,3,5,3])
b = set([2,3,4,9])
list = list(a)
print "set " + str(a) + "   " + str(b) + "   " + str(list)

print "a&b " + str(a&b)
print "a|b " + str(a|b)
print "a^b " + str(a^b)
print "a-b " + str(a-b)
a.remove(1)
print "remove " + str(a)
