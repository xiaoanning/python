#coding=utf-8

'''

同级目录下  直接import 即可 
如 ：
import python1.py

调用方法
python1.function()

不同级目录 如果想要调用文件内容 则 要在被调用文件的目录下 建__init__.py 文件 该文件为空也可以 不为空也可以 之后再导入 

使用通配符导入时 要在__init__.py 文件里配置 通配符匹配的文件
__all__ = ["SendEmail"]

如：
folder
    file1.py
    __init__.py
file2.py

file2.py中写
import folder.file1  
调用时
folder.file1.function()
或者
from folder import file1
调用时
file1.function()


'''
