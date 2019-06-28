# 创作者 马如云
# 键盘操作类
import pyautogui
class Operation:
    def __init__(self):
        return
    def goRight(self):#移动指令
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
    def goLeft(self):
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
    def goUp(self):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
    def goDown(self):
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
    def goDownWithSpace(self):#使用空格
        pyautogui.keyDown('down')
        pyautogui.keyDown('space')
        pyautogui.keyUp( 'down')
        pyautogui.keyUp('space')
    def goUpWithSpace(self):#使用空格
        pyautogui.keyDown('up')
        pyautogui.keyDown('space')
        pyautogui.keyUp( 'up')
        pyautogui.keyUp('space')
    def goLeftWithSpace(self):#使用空格
        pyautogui.keyDown('left')
        pyautogui.keyDown('space')
        pyautogui.keyUp( 'left')
        pyautogui.keyUp('space')
    def goRightWithSpace(self):#使用空格
        pyautogui.keyDown('right')
        pyautogui.keyDown('space')
        pyautogui.keyUp( 'right')
        pyautogui.keyUp('space')
    def enter(self):
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
    def escape(self):
        pyautogui.press('space')#闪避
    def doNothing(self):#不动
        return