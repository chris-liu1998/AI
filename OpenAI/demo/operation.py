# 创作者 马如云
# 键盘操作类
import pyautogui
class Operation:
    def __init__(self):
        return
    def goRight(self):
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
    def goLeft(self):
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
    def goUp(self):
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
    def goDown(self):
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
    def enter(self):
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
