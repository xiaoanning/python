#!/usr/bin/env python
#coding=utf-8

'''
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import traceback


fromAccount = '734871221@qq.com'
pswd = "udkjpvecfqkhbcfc"  #发件人邮箱密码(当时申请smtp给的口令)


smtpServer = "smtp.yeah.net"
sslPort = 25

smtpServer = "smtp.sina.com"
sslPort = 25


smtpServer = "smtp.qq.com"
sslPort = 465
#sslPort = 587

#配置邮件内容
def setEmailContent(msg):
    msg['From'] = formataddr(["镖镖必达管理员",fromAccount])#显示发件人信息 对应发件人邮箱昵称、发件人邮箱账号 昵称是显示在收件人邮箱里的 这里写什么哪里就显示什么 理论上可以随便写
    msg['To'] = formataddr([u"镖镖必达客户",fromAccount])#显示收件人信息  这里的昵称是显示在收件人邮箱里的 这里写什么哪里就显示什么 理论上可以随便写
    msg['Subject'] = "镖镖必达邮件"#定义邮件主题


#登录 发送邮件
def loginAndSend(msg ,toAccounts):
    try:
        #创建SMTP对象 发件人邮箱中的SMTP服务器，端口是465
        server = smtplib.SMTP_SSL(smtpServer, sslPort)
        
        #可以打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        
        #用来登录SMTP服务器
        print "开始登录。。。"
        success = server.login(fromAccount, pswd)
        
        #(235, 'Authentication successful')  <type 'tuple'>
        print "登录结果  ：" +str(success) + "  " + str(type(success))
        
        if success[0] != 235:
            return False
        
        #发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        toAccounts.append(fromAccount)
        server.sendmail(fromAccount,toAccounts, msg.as_string())
        print u"邮件发送成功"
        
        server.quit()
        
        return True
    
    except Exception as e:
        
        print u"Error: 无法发送邮件 。。。"
        print traceback.print_exc()
        
        return False



#发送邮件
def sendEmail(message):

    print "发送邮件..."

    #构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    #传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

    #message为传入的参数,为发送的消息.
    msg = MIMEText(message, 'plain', 'utf-8') 

    """
        msg = MIMEText(
        '<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 
        'html', 
        'utf-8')
    """
    #标准邮件需要三个头部信息： From, To, 和 Subject。

    setEmailContent(msg)

    loginAndSend(msg, toAccounts)




#发送纯文本邮件 用QQ邮箱登录 然后QQ邮箱发给收件人的QQ邮箱
def sendTextEmailQQToQQ(message ,toAccounts):
	
    print "发送邮件..."

    #构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    #传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

    #message为传入的参数,为发送的消息.
    msg = MIMEText(message, 'plain', 'utf-8') 

    """
        msg = MIMEText(
        '<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 
        'html', 
        'utf-8')
    """

    setEmailContent(msg)

    loginAndSend(msg, toAccounts)

#发送多格式的邮件 文本和图片
def sendMultipartEmailQQToQQ(message ,toAccounts):
    
    print "发送邮件..."

    #纯图片
    #msg = MIMEMultipart()

    #多格式
    msg = MIMEMultipart('alternative')

    setEmailContent(msg)

    #增加文本
    msg.attach(MIMEText(message, 'plain', 'utf-8'))
    #增加图片
    msg.attach(MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8'))

    fp = open('/Users/anning/Documents/python/application/GrabTicketApplication/001.png', 'rb')

    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<imagel>')
    msg.attach(msgImage)

    loginAndSend(msg, toAccounts)
















