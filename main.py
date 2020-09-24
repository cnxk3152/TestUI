# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# !/usr/bin/python3

# import os
from time import sleep

#pywin32
import win32gui
import win32con
#pyautoGui
import pyautogui
# pywinauto
from pyautogui.screenshotUtil import locateCenterOnScreen
from pywinauto.application import Application

app = Application(backend="win32")


# https
# ://pypi.douban.com/simple  # 豆瓣镜像
# https://pypi.tuna.tsinghua.edu.cn/simple  # 清华镜像

# mirror = " -i https://pypi.douban.com/simple"

# os.system("python -m pip install --upgrade pip" + mirror)  # 更新 pip

# os.system("pip install pywinauto" + mirror)  # 安装 pywinauto
# os.system("pip install pypiwin32" + mirror)  # 安装 pypiwin32 和 pywin32
# os.system("pip install pyautogui" + mirror)  # 安装 pyautogui
# 安装 pywin32 模块时，使用的是 pypiwin32，否则在导入包时会报错

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# ====================pywinauto=======================

# 打开应用
# app.start(app_path)
# app.start(r"C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe")

# 连接应用
# app.connect(path=app_path)
# app.connect(path=r"C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe")


# 关闭应用


# 定位到窗口（class_name：窗口类名，title：窗口标题）
# dlg = app.window(class_name, title)
# dig = app.class_name
# dlg = app[title]

# 判断窗口是否存在
# dlg.exists()

# 获取窗口信息
# app.Notepad.print_control_identifiers()

# 最小化窗口
# dlg.minimize()

# 最大化窗口
# dlg.maximize()

# 恢复窗口
# dlg.restore()

# 关闭窗口
# dlg.close()



#app = app.start(r"C:\WINDOWS\system32\notepad.exe")  # 启动记事本
# app = app.start(r"notepad.exe")  # backend 取值为 win32 时，可以这样写
#sleep(1)
#app.Notepad["Edit"].TypeKeys(u"您好，记事本，我是 pywinauto")  # 定位到输入框，并输入文本
#sleep(1)
#app.Notepad.MenuSelect(u'文件->另存为(&A)...')  # 另存为
#sleep(1)
#app[u'另存为']['Edit'].TypeKeys(u"xxx.txt")  # 输入文件名
#sleep(1)
#app[u'另存为'][u'保存'].Click()  # 保存
#sleep(1)
#if app[u'另存为'].exists():
#    app[u'确认另存为'][u"是"].Click()  # 替换原文件

#======================pywin32====================

#hwnd = win32gui.FindWindow(lpClassName=None, lpWindowName=None)  # 查找窗口，不找子窗口，返回值为0表示未找到窗口
#hwnd = win32gui.FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None)  # 查找子窗口，返回值为0表示未找到子窗口

#hwnd = win32gui.FindWindow("Notepad", u"无标题 - 记事本")

#win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

# SW_HIDE：隐藏窗口并激活其他窗口。nCmdShow=0。
# SW_SHOWNORMAL：激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。应用程序在第一次显示窗口的时候应该指定此标志。nCmdShow=1。
# SW_SHOWMINIMIZED：激活窗口并将其最小化。nCmdShow=2。
# SW_SHOWMAXIMIZED：激活窗口并将其最大化。nCmdShow=3。
# SW_SHOWNOACTIVATE：以窗口最近一次的大小和状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=4。
# SW_SHOW：在窗口原来的位置以原来的尺寸激活和显示窗口。nCmdShow=5。
# SW_MINIMIZE：最小化指定的窗口并且激活在Z序中的下一个顶层窗口。nCmdShow=6。
# SW_SHOWMINNOACTIVE：窗口最小化，激活窗口仍然维持激活状态。nCmdShow=7。
# SW_SHOWNA：以窗口原来的状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=8。
# SW_RESTORE：激活并显示窗口。如果窗口最小化或最大化，则系统将窗口恢复到原来的尺寸和位置。在恢复最小化窗口时，应用程序应该指定这个标志。nCmdShow=9。
# SW_SHOWDEFAULT：依据在STARTUPINFO结构中指定的SW_FLAG标志设定显示状态，STARTUPINFO 结构是由启动应用程序的程序传递给CreateProcess函数的。nCmdShow=10。

# 若最小化，则将其显示
#if win32gui.IsIconic(hwnd):
      #win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

#关闭窗口
#win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
#窗口置前并获得焦点
#win32gui.SetForegroundWindow(hwnd)  # 设置前置窗口
#win32gui.SetFocus(hwnd)  # 设置聚焦窗口

#left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口边界

#屏幕缩放比
#import win32api, win32con, win32print, win32gui


#def get_screen_scale_rate():
   # x = win32api.GetSystemMetrics(0)  # 屏幕缩放后的宽度分辨率
    #hDC = win32gui.GetDC(0)
    #w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 屏幕真实的宽度分辨率
    #return w / x

#注意：在获取屏幕缩放比时，不要和 pyautogui 包同时使用，否则 x=w。

#============pyautogui==================
#获取屏幕分辨率
#screenWidth, screenHeight = pyautogui.size()
#截屏
#pyautogui.screenshot("my_screenshot.png", region=(100, 100, 500, 500))  # region 为截屏区域，忽略表示截全屏

#img = pyautogui.screenshot()
#img.save('my_screenshot.png')
#查找图片
#coords = pyautogui.locateOnScreen('target_capture.png')  # 在当前屏幕中查找指定图片(图片是当前屏幕某个区域的截图)
#x, y = pyautogui.center(coords)  # 获取定位到的图中间点坐标

#x, y = locateCenterOnScreen('target_capture.png')  # 返回查找到的截图中心坐标

#获取鼠标位置与移动鼠标

# 获取鼠标位置
#x, y=pyautogui.position()

# 移动鼠标（x, y 为绝对位置，xOffset, yOffset 为相对偏移量，tween：渐变函数）
#pyautogui.moveTo(x=100, y=100, duration=2, tween=pyautogui.linear)
#pyautogui.moveRel(xOffset=None, yOffset=10, duration=0.0, tween=pyautogui.linear)  # 相对原来的位置移动

#点击
# 单击鼠标（x, y 为点击位置，clicks：点击次数，interval：点击间隔，botton：取值有'left', 'middle', 'right'，对应鼠标的左、中、右，duration：点击持续时间，tween：渐变函数）
#pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
#pyautogui.click(x, y)  # 单击
#pyautogui.rightClick(x, y)  # 右击
#pyautogui.middleClick(x, y)  # 中击
#pyautogui.doubleClick(x, y)  # 双击

#拖拽
# 鼠标拖拽
#pyautogui.dragTo(x=427, y=535, duration=3, button='left')

# 鼠标相对拖拽
#pyautogui.dragRel(xOffset=100, yOffset=100, duration=3, button='left', mouseDownUp=False)

#滚动
#pyautogui.scroll(-500)  # 向下滚 500 格

#键盘控制

# 输入文本
#pyautogui.typewrite(message='Hello world!', interval=0.25)

# 按键
#pyautogui.press('esc')
#pyautogui.press(['left', 'left', 'left'])  # 依次按多个按键

# 组合热键（从左到右依次按下按键，再从右到左依次松开按键）
#pyautogui.hotkey('ctrl', 'c')
#常用按键说明如下：
#ctrl、shift、alt、esc、backspace、win：同键盘
#capslock、numlock、scrolllock、insert、delete、home、end、pageup、pagedown、pause、printscreen：同键盘
#f1、f2、f3、...、f12：同键盘
#enter、return、\n：Enter键
#tab、\t：Tab键
