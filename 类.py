#coding=utf-8

import pickle
import json
'''


python的类和对象
1、类的继承（直接在类名后面括号里面写入要继承的类名）

        子类              父类
class DerivedClassName(BaseClassName)


注：如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性。


a、调用未绑定的父类方法
b、使用super函数（优点是不用给出任何基类的名字，python会自动一层层找到基类中对应的方法）


多重继承（容易代码混乱，应尽量避免使用） 使用组合：

'''


#类
class MyList (list):

    pass

list1 = MyList()

list1.append(1)

print list1


#组合
class JSONBaseClass():
    def jsonDic(self):
        return self.__dict__


#自定义类
#鱼
class Fish (JSONBaseClass):
    def __init__(self,dict):
        self.num = 0

        self.__dict__ = dict

#乌龟
class Turtle (JSONBaseClass):
    def __init__(self ,dict ):
        self.num = 0
        self.name = "0"

        self.__dict__ = dict

# 水池
class Pool (JSONBaseClass):
    def __init__(self ,dict):
        
        #复杂对象json数据解析
        self.att = ""

        self.__dict__ = dict

        self.fish = Fish( dict["fish"])
        self.turtle = Turtle( dict["turtle"])

    def jsonDic(self):
        dic = self.__dict__
        dic["fish"] = self.fish.jsonDic()
        dic["turtle"] = self.turtle.jsonDic()
        return dic

    size = 100

poolDic = {"fish":{"num":10},"turtle":{"num":10,"name":"test"},"att":"atttest"}
pool = Pool(poolDic)


#/Users/anning/Documents/python
filePath = "/Users/anning/Documents/python/json.json"

def writeFile():
    with open(filePath,"w") as f:
        
        poolDic = pool.jsonDic()
        
#        poolJson = pickle.dumps([poolDic])
#        pickle.dump(poolJson,f)

        poolJson = json.dumps([poolDic])
        json.dump(poolJson,f)

def readFile():
    with open(filePath, "r") as f:
#        poolJson = pickle.load(f)
#        poolList = pickle.loads(poolJson)

        poolJson = json.load(f)
        poolList = json.loads(poolJson)

        print "poolDic " + str(poolList)

        poolObj = Pool(poolList[0])

        print poolObj.turtle.num

writeFile()

readFile()

'''
    
类中的方法名与属性名重名时，类将被属性覆盖：

绑定：python严格要求方法需要有实例才能被调用，这种限制其实就是python所谓的绑定概念。

　　1、issubclass(class, classinfo)

　　　　a、一个类被认为是其自身的子类

　　　　b、classinfo可以是类对象组成的元组，只要class与其中任何一个候选子　　　类，则返回True

　　2、isinstance(object，classinfo）

　　　　a、如果第一个参数不是对象，则永远返回False

　　　　b、如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError　　异常。

　　3、hasattr(object,name)：测试一个对象是否有指定的属性

　　4、getattr（object, name[, default]）:返回对象指定的属性值

　　5、setattr(object，name，value):设置指定属性的值

　　6、delattr（object，name）：删除对象中指定的属性，如果属性不存在抛出　　异常。

2、多态（不同的对象对同一类方法的不同响应）

3、self（对象的方法中会传递一个self参数）

　　由一个类可以生成多个对象，对象之间都极为相似，来源于同一个类，不同的对象调用方法时传递self参数告诉python当前是哪个对象调用方法了。



4、python的魔法方法（总是被双下划线包围）

　　1、__init__(self, param1, param2, ...)：类似于java中的构造方法

ps：init方法不能有返回值

　　2、__new__(cls[,...]):对象实例化时调用的方法，返回一个类对象
'''

class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)

print CapStr("i am xiao")


'''
    
3、__del__(self)：当对象被销毁的时候（垃圾回收机制）自动调用    
'''



