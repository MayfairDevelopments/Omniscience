from PIL import Image
import os

class InputProcessor():
    def __init__(self,imageDirectory,width=50,height=50,grayScale=True):
        self.inputImage=None
        self.imageDirectory=imageDirectory
        self.width = width
        self.height=height
        self.grayScale = grayScale
        self.directory = self.imageDirectory
        self.inputImage=None
        self.folder()
    
    def folder(self):
        i = 0 
        for img in os.listdir(imageDirectory):
            if img == "Modified":
                pass
            else:
                i+=1
                self.imageDirectory = imageDirectory+img
                self.inputImage = Image.open(self.imageDirectory)
                temp = self.directory+"temp"+img
                if self.grayScale:
                    self.setGrayScale(temp)
                self.resize(temp,self.width,self.height)
                self.pixelArray()
                self.inputImage.save('{}Modified\{}.jpg'.format(self.directory, i))
                os.remove(temp)

    def resize(self,temp,width,height):
        size = (width,height)
        self.inputImage.thumbnail(size)
        self.inputImage.save(temp)
        self.inputImage = Image.open(temp)

    def setGrayScale(self,temp):
        self.inputImage.convert(mode="L").save(temp)
        self.inputImage = Image.open(temp)

    def pixelArray(self):
        array = []
        for x in range(self.inputImage.width):
            for y in range(self.inputImage.height):
                if self.grayScale:
                    pixel = self.inputImage.getpixel((x,y))
                    pixel = pixel/255
                else: 
                    r,g,b = self.inputImage.getpixel((x,y))
                    pixel = sum([r,g,b])/3
                    pixel=pixel/255
                array.append(pixel)
        fileSave = open('XRayImages\Modified\PixelsArray.txt','a')
        fileSave.write(str(array))
        fileSave.write(">")
        fileSave.close()

#>>[Usage]
#imageDirectory = 'XRayImages\\'
#a = InputProcessor(imageDirectory)
