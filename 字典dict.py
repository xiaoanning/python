
#coding=utf-8

'''
    
    字典是Python语言中唯一的映射类型。
    映射类型对象里哈希值（键，key）和指向的对象（值，value）是一对多的的关系，通常被认为是可变的哈希表。
    字典对象是可变的，它是一个容器类型，能存储任意个数的Python对象，其中也可包括其他容器类型。
    
    技巧：
    字典中包含列表：dict = {"ZhangSan" : ['23','IT'],"Lisi" : ['22','dota']}
    字典中包含字典：dict = {"Wangwu" : {"age" : 23,"job":"IT"},"Song" : {"age":22,"job":"dota"}}
    
    
    常用操作：
    索引
    新增
    删除
    键、值、键值对
    循环
    长度
    PS：循环，range，continue 和 break

'''
D = { "zhangsan" : [23 , "IT"] , "lisi":[24 , "dota"] , "long":[28 , "teacher"]}

print "D : " + str ( D )

print "keys : " + str(D.keys())

print "values : " + str(D.values())

D.popitem() #默认删除第一个键值
print "popitem : " + str(D)

del D["long"]
print "del : " + str(D)


print "has_key lisi : " + str(D.has_key('lisi'))

D["lisi"] = "lisichange"
D["wangwu"] = [22 , "wang"]
print "赋值 : " + str(D)


seq = ('name' , 'age' , 'sex')
dic = D.fromkeys(seq) #以元组的元素为KEY生成字典

print "fromKeys : " + str(dic)

dic = dict.fromkeys(seq , "wangwulong" )

print "fromKeys : " + str(dic) #以元组的元素为KEY生成字典 并批量赋值

print "cmp : " + str(cmp(dic["name"],dic["age"])) + "   " + str(cmp(D["lisi"] , D["wangwu"]))

dic.setdefault('father',None)
dic.setdefault('mother',"wangmei")
dic.setdefault('name',"xiaosan") #如果没有该键 则值取这里的默认值 如果有 还取原值
print "setdefault " + str(dic)
del dic['mother']
print "setdefault " + str(dic)
dic.clear()
print "clear " + str(dic)









