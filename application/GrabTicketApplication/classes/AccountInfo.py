#!usr/bin/env python
#coding=utf-8


from JSONBaseClass import JSONBaseClass

def getAccountInfo(index):
    if index == 1 :
        return {
                "username":"baiyuanyangshu",
                "password":"yuanlu1203",
                "authenticationname":u"肖湍"
                }
    if index == 2:
        return {
            "username":"zhaoshaoxu1234",
            "password":"xuri123",
            "authenticationname":u"韩遂云"
            }

class AccountInfo (JSONBaseClass):
    
    def __init__(self , dict):
        
        self.username = ""
        self.password = ""
        self.authenticationname = ""
        
        
        self.__dict__ = dict


def getCurrentAccountInfo():

    dict = getAccountInfo(1)

    currentAccount = AccountInfo(dict)

    print "当前登录用户：" + str(currentAccount.__dict__)

    return currentAccount



