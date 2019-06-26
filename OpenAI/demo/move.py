# 创作者 马如云
# ai移动类
from demo.point import Point
from demo.operation import Operation
from demo.screenshot import  screenshot

class Move:

    op=Operation()

    def __init__(self):
        return
    def findpath(self):
        img = screenshot()#截图
        img_array = img.load()#获取像素点信息
        w, h = img.size
        #用来记录所求物体的左上像素点
        first1 = False
        first2 = False
        #分别为左上和右下坐标
        r1 = Point(0,0)
        r2 = Point(0,0)
        d1 = Point(0,0)
        d2 = Point(0,0)
        for i in range(0, h):
            for j in range(0, w):
                pixel = img_array[j, i]
                if pixel == (0, 254, 254):
                    if first1 == False:#第一次找到的点即为左上坐标
                        r1 = Point(j, i)
                        first1 = True
                    r2 = Point(j, i)#最后一次找到的即为右下坐标
                if pixel == (213, 245, 252):
                    if first2 == False:
                        d1 = Point(j, i)
                        first2 = True
                    d2 = Point(j, i)
        player = (r2+r1).getmidpoint()
        destination = (d2+d1).getmidpoint()
        dir = destination-player
        if abs(dir.x)>abs(dir.y) and dir.x>0:
            self.op.goRight()
        elif abs(dir.x)>abs(dir.y) and dir.x<0:
            self.op.goLeft()
        elif abs(dir.x)<abs(dir.y) and dir.y>0:
            self.op.goDown()
        elif abs(dir.x) < abs(dir.y) and dir.y < 0:
            self.op.goUp()