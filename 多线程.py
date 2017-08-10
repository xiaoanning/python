#!/usr/bin/env python
#coding=utf-8


from threading import Thread
from time import sleep
'''

python 线程

Python提供了两个模块来实现多线程thread 和threading ，thread 有一些缺点，在threading 得到了弥补，为了不浪费时间，所以我们直接学习threading 就可以了

Threading用于提供线程相关的操作，线程是应用程序中工作的最小单元

'''


sleep(0.5)
print "sleep 0.5 "

def show(arg1,arg2):
    #sleep(0.5)
    print "thread :" + str(arg1) + " " + str(arg2) + " Thread name :" + str(t.getName())

for i in range(5): #创建10个线程
    t = Thread(target=show , args=(i,i))#创建线程t,使用threading.Thread()方法，在这个方法中调用show方法target=show，args方法对show进行传参。
    t.setDaemon(False)#将线程声明为后台线程，必须在start() 方法调用之前设置  如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止  如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
    t.setName(str(i)) #setName 为线程设置名称      getName　 获取线程名称

    t.start()#线程准备就绪，等待CPU调度

print "main thread stop"

'''
    
    join 　　　　　　  逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
    
    run 　　　　　　  线程被cpu调度后执行Thread类对象的run方法
    
上述代码创建了10个“前台”线程，然后控制器就交给了CPU，CPU根据指定算法进行调度，分片执行指令。



python中的多线程，有一个GIL（Global Interpreter Lock 全局解释器锁 ）在同一时间只有一个线程在工作，他底层会自动进行上下文切换.这个线程执行点，那个线程执行点！

'''



'''
    
    线程锁
    
    由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，CPU接着执行其他线程。所以，可能出现抢占屏幕打印问题，出现乱序问题，执行上面的代码可以直接看到效果.所以就出现了线程锁机制，专门解决这个问题.
    
    设置线程锁
    
    python的锁可以独立提取出来
    
'''

#锁的使用
#创建锁

lock = threading.Lock()

#锁定   锁定以后 下面执行要加锁的代码
lock.acquire()#锁定方法acquire可以有一个超时时间的可选参数timeout。如果设定了timeout，则在超时后通过返回值可以判断是否得到了锁，从而可以进行一些其他的处理。 lock.acquire(10)

#执行完加锁的代码后 释放锁
lock.release()

























