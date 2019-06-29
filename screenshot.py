# 创作者 马如云
# 截屏函数
from PIL import Image
from PyQt5.QtWidgets import QApplication
import win32gui
import sys

def screenshot():
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  # 窗口的类名可以用Visual Studio的SPY++工具获取

    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    image = screen.grabWindow(hWnd).toImage()
    img=Image.fromqpixmap(image)

    return img


