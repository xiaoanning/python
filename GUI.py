
#coding=utf-8
import wx

#事件处理

def loadAction(event):
    file = open(fileName.GetValue())
    contents.SetValue(file.read())
    file.close()

def saveAction(event):
    file = open(fileName.GetValue(),'w') #r 读 w 写 a 追加 b 二进制 + 读写
    file.write(contents.GetValue())
    file.close()

#UI
app = wx.App()
win = wx.Frame(None, title = "编辑器", size = (410,335))

#固定位置
#saveButton = wx.Button(win, label = '保存' , pos = (320,5) , size = (80,25))
#loadButton = wx.Button(win, label = '打开' , pos = (225,5) , size = (80,25))
#fileName = wx.TextCtrl(win, pos = (5,5) , size = (210,25))
#contents = wx.TextCtrl(win, pos = (5,35), size = (390,260), style = wx.TE_MULTILINE | wx.HSCROLL | wx.VSCROLL)


#智能布局
bkg = wx.Panel(win)
saveButton = wx.Button(bkg , label = '保存')
saveButton.Bind(wx.EVT_BUTTON,saveAction)

loadButton = wx.Button(bkg , label = '打开')
loadButton.Bind(wx.EVT_BUTTON, loadAction)

fileName = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer() # 参数表示水平显示还是垂直显示  默认水平  垂直 VERTICAL
hbox.Add(fileName , proportion = 4 , flag = wx.EXPAND)
hbox.Add(loadButton, proportion = 1 , flag = wx.LEFT , border = 5)
hbox.Add(saveButton, proportion = 1 , flag = wx.LEFT , border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0 , flag = wx.EXPAND | wx.ALL , border = 5)
vbox.Add(contents , proportion = 1 , flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT , border = 5)

bkg.SetSizer(vbox)

print "hello world"

win.Show()
app.MainLoop()
