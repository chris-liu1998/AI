from PIL import Image

class ImageAnalysis:


    def __init__(self,img:Image.Image):
        self.img=img
        return
    def analysis(self):
        img_array = self.img.load()  # 获取像素点信息
        w, h = self.img.size
        self.img.show()
        for i in range(0, h):
            for j in range(0, w):
                pixel = img_array[j, i]
                # 输出到文件
                