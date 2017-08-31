#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from time import sleep
#traceback模块被用来跟踪异常返回信息
import traceback
import re
import time

from utils import GetBrowser
from utils import SendEmail
from utils import URL
from utils import FileData
from classes.AccountInfo import AccountInfo
from classes import AccountInfo
from classes.CustomerInfo import CustomerInfo
from classes import CustomerInfo

from threading import Thread

'''
    已实现：
    登录
    跳到查询页面 设置订票小助手 订票（无票轮询）
    对象
    json
    多线程 开辟多个线程 同时执行多个任务  （可以将程序启动多次 以开始多个任务）
    自动切换IP（用三方VPN解决）
    选择乘车人时 要先搜索再选中 （注意编码）
    将乘车人信息录入文件再读入 有问题：录入时的编码格式 （未实现）
    录入车站信息 (已录入热门车站)
    将成功的写入文件
    
    可以为每一份订单写一份代码运行日志  想法未实现

    怎么自动输入验证码
    
    
    
    
    
    
'''

#用到浏览器chrome，还没有安装的读者可以从这个下载地址下载chrome并进行安装：http://chromedriver.storage.googleapis.com/index.html?path=2.20/，大家可以根据自己的电脑系统选择下载包进行安装。如果你用的是MAC，可以直接通过 brew install chromedriver来安装
#Splinter是一个自动化测试网络应用的Python库。有了Splinter，就可以将打开浏览器、输入URL、填写表单、点击按钮等全部操作自动化。因此，我们需要引入这个库。通过sudo pip install splinter来安装


#定时
def timing():
    if currentCustomerInfo.bookingTime == "":
        return

    count = 0

    while True:
        currentTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print currentTime
        wait = currentTime < currentCustomerInfo.bookingTime
        print "wait : {}".format(wait)
        if wait :
            count += 1
            if count > 60*2: #控制多长时间刷新网页 避免账号登录失效
                count = 0
                buyTicket()
                break

            sleep(0.5)
            continue
        else :
            break

#登录
def login():

    try:
        print "前往登录页面"

        #到登录页面
        brow.visit(URL.login_url)
        print "当前页面 ： " + str(brow.url)

        #brow.find_by_id("username")[0].fill(username)
        brow.fill("loginUserDTO.user_name", currentAccountInfo.username)
        brow.fill("userDTO.password", currentAccountInfo.password)
        
        #自己手动输入验证码
        print "等待验证码，自行输入。。。"
        while True:
            if brow.url != URL.initmy_url:
                continue
            
            else:
                print "离开登录页面"
                break
    except Exception as e:
        print traceback.print_exc()
        print "退出浏览器"
        brow.quit()

#购票
def buyTicket():
    
    try:
        print "前往购票页面..."
        # 跳到购票页面
        brow.visit(URL.ticket_url)

        #设置查询信息
        setQueryInfo()

        #设置订票帮手
        ticketHelper()

        #订票帮手设置后 会自动选定 【开启自动查询】  关闭【开启自动查询】后，会自动关闭【自动提交】
        #brow.find_by_id("auto_query")[0].click()

        #定时 不到时间不轮询
        timing()

        #sleep(300)

        #点击查询自动提交
        click()
        
    except Exception as e:
        print "订票出错 重新填写信息"
        print traceback.print_exc()

#设置查询信息
def setQueryInfo():
        # 加载查询信息
        brow.cookies.add({"_jc_save_fromStation": currentCustomerInfo.fromStation})
        brow.cookies.add({"_jc_save_toStation": currentCustomerInfo.toStation})
        brow.cookies.add({"_jc_save_fromDate": currentCustomerInfo.fromDate})
        brow.reload()


#设置订票帮手
def ticketHelper():
    
        brow.find_by_text("订票帮手").click()
        
        #乘车人
        selectPassenger()
        #sleep(0.2)

        #优先车次
        selectTrainNum()
        #sleep(0.2)
        
        #优先席别
        selectSeatType()
        #sleep(0.1)
        
        #高级设置  1 席别优先 2 车次优先
        brow.find_by_value(currentCustomerInfo.priorityType)[0].click()
        #自动提交
        # brow.find_by_id("autoSubmit").click()
        # 余票不足时部分提交
        # brow.find_by_id("partSubmit").click()

#选择乘车人
def selectPassenger():
    
    brow.find_by_text("请选择")[0].click()
    #只要用户登录 乘车人信息 就会缓存 这里不是新请求的 所以不需要等待  为防止出错 还是验证一下
    count = 0 ;
    
    while True :
        div = brow.find_by_id("buyer-list")
        if div:
            print "有可选乘车人 将要选择乘车人"
            break
        else :
            count += 1
            print "等待0.5秒后再查询乘车人"
            sleep(0.5)
        
        #控制等待时间
        if count == 3 :
            break

    #给他人购票 乘车人不是该账户本人
    i = 0
    for name in currentCustomerInfo.passengerList:
        
        try:
            div = brow.find_by_id("buyer-list")
            if div:
                print "有可选乘车人 开始选择乘车人"
            else:
                break
            
            #搜索
            brow.find_by_id("searchPassenger")[0].fill(name)

            #给自己购票 自己的出现次数是两次
            if name == currentAccountInfo.authenticationname:
                brow.find_by_text(currentAccountInfo.authenticationname)[1].click()
            else:
                brow.find_by_text(name)[0].click()
            
            i += 1
            if i >= 4:
                print "一张订单最多选择5个乘车人 {}".format(len(currentCustomerInfo.passengerList))
                break
        except Exception as e:
            print "选择乘车人失败 {} {}".format(name,str(currentCustomerInfo))
            print traceback.print_exc()


    closeBtn = brow.find_by_text("关闭")
    
    if closeBtn:
        print "点击选择乘车人关闭按钮"
        closeBtn[3].click()

def selectTrainNum():

    brow.find_by_text("请选择")[1].click()
    
    #需要请求网络拿到车次  故会有延迟 需要等待  当正在查询时进行搜索 会导致数据请求终止  车次无法显示
    count = 0 ;
    while True :
        div = brow.find_by_xpath(".//ul[@style='height: auto; display: block;']")
        if div:
            print "有可选车次"
            break
        else :
            count += 1
            print "等待0.5秒后再查询车次"
            sleep(0.5)
        
        #控制等待时间
        if count == 3 :
            break

    have = False
    #选择车次
    i = 0
    for train in currentCustomerInfo.trainNumList :
        
        print "{}".format(train)
        
        try :
            if have == False :
                div = brow.find_by_xpath(".//ul[@style='height: auto; display: block;']")
                if div:
                    have = True
                    print "有可选车次 开始选择"
                else:
                    break
            
            brow.find_by_id("yxtraininput")[0].fill(train)
            path = ".//li[@traincode='{name}']".format(name=train)
            print "车次div路径   {}".format(path)
            brow.find_by_xpath(path).click()
        
        except Exception as e:
            print "选择车次出错。。。{}".format(train)
            print traceback.print_exc()
        i += 1
        if i >= 5 :
            print "最多选择5个优先车次 {}".format(len(currentCustomerInfo.trainNumList))
            break

    print "关闭选择车次"
    brow.find_by_id("yxtrain_close")[0].click()

#选择席别
def selectSeatType():
    
    brow.find_by_text("请选择")[2].click()

    i = 0
    for seat in currentCustomerInfo.seatTypeList:
        try:
            
            brow.find_by_text(seat)[1].click()
        except Exception as e:
            print "选择席别出错。。。{}".format(seat)
            print traceback.print_exc()
        i += 1
        if i >= 4 :
            print "最多选择5个优先席别 {}".format(len(currentCustomerInfo.seatTypeList))
            break


    brow.find_by_text("关闭")[4].click()


#提交
def click():
    count = 0
    while brow.url == URL.ticket_url:
        
        if count > 0 :
            #重复查询的间隔
            sleep(0.2)

        count += 1
        print "循环点击查询... 第 %s 次" % count
        try:
            brow.find_by_text("停止查询").click()
        except Exception as e:
            print "点击 “停止查询按钮” 时出错"
        
        try:
	        brow.find_by_text("查询").click()
        except Exception as e:
        	print "点击 查询按钮 出错"
                	

        try:
            brow.find_by_text("[未完成订单]")[0].click()
            print "有未完成订单..."
        except Exception as e:
            print "没有未完成订单..."

    print "离开了查询页"
    
    success = False
    #判断是否是待付款页面 如果不是则重新购买
    if brow.url == URL.pay_order_url :
        print "购票成功 待付款..."
        success = True
    if brow.url == URL.no_complete_url :
        print "有未完成订单"
        success = True
        
    if success:
        FileData.appendWriteFile(currentCustomerInfo.__dict__,"/Users/anning/Documents/python/application/GrabTicketApplication/log/success.txt")
        SendEmail.sendMultipartEmailQQToQQ(currentCustomerInfo.jsonDic(),[])


def huoCheApplication():
    
    #获取Browser
    global brow
    brow = GetBrowser.getChromeBrowser()

    #登录
    login()

    #购票
    buyTicket()


# 获取12306用户名，密码
currentAccountInfo = AccountInfo.getCurrentAccountInfo()

# 获取订单信息
currentCustomerInfo = CustomerInfo.getCurrentCustomerInfo()


if __name__ == "__main__":
    huoCheApplication()

'''
小技巧：

如何在chrome中获得起始站和终点站等的cookie值？

大家可以先登录一下12306，输入地点日期什么的查询一下，然后在chrome浏览器中按F12，出现如下页面，在resource选项里找到相应的值。

'''




