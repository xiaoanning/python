#coding=utf-8

from splinter.browser import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#获取Browser
def getChromeBrowser():
    
    #使用splinter打开chrome浏览器
    brow = Browser(driver_name = "chrome")

    return brow 
