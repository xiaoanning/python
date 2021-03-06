#coding=utf-8

from JSONBaseClass import JSONBaseClass
import sys
sys.path.append("..")
from utils import FileData
from utils import GetStationEncoding


def getCustomerInfo(index):

    if index == 1 :
        return {
                "fromStation":"北京",
                "toStation":"邢台",
                "fromDate":"2017-07-20",
                "passengerList":[u"赵小旭"],
                "trainNumList":["G309","G655","G6741","G65","G429"],
                "seatTypeList":["二等座"],
                "priorityType":"1",
                "bookingTime":"2017-07-14 15:00:00",
                }
    if index == 2 :
        return {
                "fromStation":"齐齐哈尔",
                "toStation":"北京",
                "fromDate":"2017-09-29",
                "passengerList":[u"高桂春"],
                "trainNumList":["T48"],
                "seatTypeList":["软卧"],
                "priorityType":"1",
                "bookingTime":"2017-08-31 08:50:50",
                }

    if index == 3 :
        return {
                "fromStation":"杭州",
                "toStation":"台州",
                "fromDate":"2017-09-30",
                "passengerList":[u"潘崇毅"],
                "trainNumList":["G7677"],
                "seatTypeList":["二等座"],
                "priorityType":"1",
                "bookingTime":"2017-08-31 08:50:50",
                }
    if index == 4 :
        return {
                "fromStation":"十堰",
                "toStation":"北京",
                "fromDate":"2017-10-07",
                "passengerList":[u"韩遂云"],
                "trainNumList":["K590","K280"],
                "seatTypeList":["软卧","硬卧"],
                "priorityType":"1",
                "bookingTime":"2017-07-14 15:00:00",
                }



#客户
class CustomerInfo (JSONBaseClass):

    dictData = {}

    def __init__(self,dict):
        
        dictData = dict
        
        self.fromStation = ""
        self.toStation = ""
        self.fromDate = "" #出发时间
        self.passengerList = [] #乘车人 最多5个
        self.trainNumList = [] #优先车次 最多5个
        self.seatTypeList = [] #优先席别 无座 硬座 软座 硬卧 动卧 软卧 高级软卧 二等座 一等座 商务座 特等座 最多5个
        self.priorityType = "" #高级设置 1 席别优先 2 车次优先
        self.bookingTime = "" #开始售卖时间 不设置售卖时间时 可以设置为空 或过去的时间

        self.__dict__ = dict

        self.fromStation = GetStationEncoding.getStationEncoding(self.fromStation)
        self.toStation = GetStationEncoding.getStationEncoding(self.toStation)

    def jsonDic(self):
        
        return dictData


def getCurrentCustomerInfo():
    
    
    dict = getCustomerInfo(4)
    customerInfo = CustomerInfo(dict)
    
    print "当前客户订单：" + str(customerInfo.__dict__)
    
    return customerInfo





