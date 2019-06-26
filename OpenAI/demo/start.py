# 创作者 马如云
# 主程序
from demo.screenshot import  screenshot
from demo.operation import Operation
from demo.formfocus import setf
from demo.move import Move
import win32api
import time
import pytesseract
import threading
import pythoncom

move=Move()
op=Operation()
If_gamestart=False
#定义操作类
def Job_formfocus():#窗口焦点线程
    pythoncom.CoInitialize()
    sf = setf()
    while True:
        time.sleep(3)
        try:
            sf.setfocus()
        except Exception as e:
            print (e)

def Job_gamestart():#打开游戏线程
    pythoncom.CoInitialize()
    time.sleep(5)
    while True:
        img=screenshot()#截图
        str=pytesseract.image_to_string(img)#文字识别
        #判断动画是否已经加载完毕
        print(str)
        if str.find('GAME')>0:
            #进入游戏
            op.enter()
            global If_gamestart
            If_gamestart=True#游戏开始
            break;

def Job_AI_move():
    pythoncom.CoInitialize()
    while True:#判断是否开始游戏
        #while If_gamestart==True:
            move.findpath()



if __name__ == '__main__':
    #打开游戏
    win32api.ShellExecute(0, 'open', r'F:\SteamLibrary\steamapps\common\Just Shapes & Beats\JSB.exe', '', '', 1)
    #运行线程
    thread_formfocus = threading.Thread(target=Job_formfocus, name="Job1", args=())
    thread_formfocus.start()
    thread_gamestart = threading.Thread(target=Job_gamestart, name="Job2", args=())
    thread_gamestart.start()
    thread_AI_move = threading.Thread(target=Job_AI_move, name="Job3", args=())
    thread_AI_move.start()