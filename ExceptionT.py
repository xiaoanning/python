
#coding=utf-8

'''

1 AttributeError        　　　　 试图访问一个对象没有的属性，比如foo.x,但是foo没有属性x
2 IOError        　　　　　　　　 输入\输出异常，基本上是无法打开文件
3 ImportError        　　　　　　无法引入模块或包，基本上是路径问题或名称错误
4 IndentationError    　　　　  语法错误(的子类)；代码没有正确对齐
5 IndexError        　　　　　　 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
6 KeyError        　　　　　　　　试图访问字典里不存在的键
7 KeyboardInterrupt    　　　　　Ctrl+C被按下
8 NameError        　　　　　　　使用一个还未被赋予对象的变量
9 SyntaxError        　　　　　 Python代码非法，代码不能编译(语法错误)
10 TypeError        　　　　　　 传入对象类型与要求的不符合
11 ValueError        　　　　　　传入一个调用者不期望的值，即使值得类型是正确的
12 UnboundLocalError    　　　　试图访问一个还未被设置的局部变量，基本上是由于另有一个名的全局变量，导致你以为正在访问他.
    Exception as e : 捕获全部类型的错误

'''


try :
    import s

except Exception as e :
    
    #输出格式
    import traceback
    print 'Exception as e  e.message : ' + e.message
    print 'Exception as e  str ( e ) : ' + str ( e )  # 等同与e.message
    print 'Exception as e  repr ( e ) : ' + repr ( e )  #给出的异常信息比较详细
    print 'Exception as e  traceback.print_exc() : '
    traceback.print_exc()
    print 'Exception as e  traceback.format_exc() : ' + traceback.format_exc()


finally :

    print 'ImportError          ------------------ finally'


import time
for i in range(1 , 4) :

    try :
        time.sleep(0.5)
        print i

    except KeyboardInterrupt :
        print 'please do not interupt me , i am doing the importtant task here'


#手动触发异常
try :
    
    MyException = Exception
    MyException.message = '手动触发异常'

    raise MyException

except MyException :
    print 'raise : ' + str ( MyException )

finally :
    
    print 'raise      ===== finally'








    
