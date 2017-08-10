#!usr/bin/env python
#coding=utf-8

'''
    默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
    日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
    
'''
import logging
from logging.handlers import RotatingFileHandler

'''
print dir (logging)

['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PlaceHolder', 'RootLogger', 'StreamHandler', 'WARN', 'WARNING', '__all__', '__author__', '__builtins__', '__date__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_handlerList', '_handlers', '_levelNames', '_lock', '_loggerClass', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_unicode', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'cStringIO', 'captureWarnings', 'codecs', 'collections', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogger', 'getLoggerClass', 'info', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 'root', 'setLoggerClass', 'shutdown', 'sys', 'thread', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
'''

'''
   
   
   
   logging.basicConfig函数各参数:
   filename: 指定日志文件名
   filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
   format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
   %(levelno)s: 打印日志级别的数值
   %(levelname)s: 打印日志级别名称
   %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
   %(filename)s: 打印当前执行程序名
   %(funcName)s: 打印日志的当前函数
   %(lineno)d: 打印日志的当前行号
   %(asctime)s: 打印日志的时间
   %(thread)d: 打印线程ID
   %(threadName)s: 打印线程名称
   %(process)d: 打印进程ID
   %(message)s: 打印日志信息
   datefmt: 指定时间格式，同time.strftime()
   level: 设置日志级别，默认为logging.WARNING
   stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
   
'''

format_str = '%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s'

#通过logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG,
                    format= format_str,
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename = './log/log.log',
                    filemode = 'w')

#将日志同时输出到文件和屏幕
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(format_str)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')


#logging之日志回滚

#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
rthandler = RotatingFileHandler('test.log', maxBytes= 10*1024*1024, backupCount = 5)
rthandler.setLevel(logging.DEBUG)
formatter = logging.Formatter(format_str)
rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(rthandler)

'''
    
    logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
    logging的几种handle方式如下：
    
    logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
    logging.FileHandler: 日志输出到文件
    日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
    logging.handlers.BaseRotatingHandler
    logging.handlers.RotatingFileHandler
    logging.handlers.TimedRotatingFileHandler
    logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
    logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
    logging.handlers.SMTPHandler:  远程输出日志到邮件地址
    logging.handlers.SysLogHandler: 日志输出到syslog
    logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
    logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
    logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器
    
    由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中，
    上述其它处理方式的使用请参见python2.5手册！
'''


#通过logging.config模块配置日志  创建logging.config



















