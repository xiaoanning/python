#coding=utf-8

#打开文件

'''
    打开文件时，需要指定文件路径和以何等方式打开文件，打开后，即可获取该文件句柄，此后通过此文件句柄对该文件操作。
    
    打开文件的模式有：
    
    r，只读模式（默认）。
    w，只写模式。【不可读；不存在则创建；存在则删除内容；】
    a，追加模式。【可读;不存在则创建；存在则只追加内容；】
    "+" 表示可以同时读写某个文件
    
    r+， 可读写文件。【可读；可写；可追加】
    w+，无意义
    a+， 同a
    "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
    
    rU
    r+U
    "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
    
    rb
    wb
    ab
    
    '''

# file_obj = file('/Users/anning/Documents/python/xt.txt' , 'r+')

with file('/Users/anning/Documents/python/xt.txt' , 'r+') as file_obj :


    #读一个 文件指针就会移动一个


    #读取文件的内容：

    print 'truncate : '
    print file_obj.truncate(4) #截断数据，仅保留指定之前数据

    print 'readline : ' + file_obj.readline(2)
    print 'read : ' + file_obj.read(2)  #读取指定字节数据

    for line in file_obj :
        
        print 'next : ' + file_obj.next() #获取下一行数据，不存在，则报错

        print 'for in : ' + line

    print 'tell : ' + str ( file_obj.tell() ) #获取当前指针位置

    file_obj.seek(0) #指定文件中指针位置
    print 'read : ' + file_obj.read()  # 一次性加载所有内容到内存
    file_obj.seek(0)

    # 每次仅读取一行数据
    print 'readline : ' + str ( file_obj.readline(2) )# 读一行


    print 'readlines : ' + str ( file_obj.readlines(2) )# 一次性加载所有内容到内存，并根据行分割成字符串

    print 'read : ' + file_obj.read()  # 一次性加载所有内容到内存

    file_obj.write('\n2001') #写文件的内容：
    file_obj.write('\n2002')
    file_obj.writelines(['111111111','2222222'])

    print 'xreadline : ' + str (file_obj.xreadlines())

    print '=== : ' + file_obj.read()

    print 'fileno : ' + str ( file_obj.fileno() ) #文件描述符  返回int

    file_obj.flush() #刷新文件内部缓冲区

    print 'isatty : ' + str ( file_obj.isatty() ) #判断文件是否是同意tty设备

#file_obj.close() #关闭文件句柄

file_obj.read();







