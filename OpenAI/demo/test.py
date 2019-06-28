from demo.screenshot import  screenshot
from demo.imageanalysis import ImageAnalysis
import pyautogui






if __name__ == '__main__':
    img = screenshot()  # 截图
    ima=ImageAnalysis(img)
    ima.analysis()
