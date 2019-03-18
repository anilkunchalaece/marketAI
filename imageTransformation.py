
'''
Author : Kunchala Anil
Date : 2 feb 2019
This script is used to perform basic transformations on  images
'''
import cv2
import numpy
import os,shutil

class Transform:
    def __init__(self,baseDir,srcDir,desDir,desSize):
        self.imageHeight = 0
        self.imageWidth = 0
        self.imgBaseDirectory = baseDir
        self.srcDirectory = self.imgBaseDirectory+'/'+srcDir
        self.directoryToSave = self.imgBaseDirectory+ '/' +desDir
        self.desImgSize = desSize
    
    def calculateImageProperties(self,imageObj):
        self.imageHeight , self.imageWidth = imageObj.shape[:2]

    def resizeImage(self,image,destImgSize):
        '''
        imageObj : source image 
        destImgSize : destination image size as tuple (height ,width)
        '''
        srcImageObj = cv2.imread(image)
        self.calculateImageProperties(srcImageObj)
        destImageName = self.directoryToSave+ image.replace(self.srcDirectory,'')
        output = cv2.resize(srcImageObj,destImgSize,interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(destImageName,output)
    
    def resizeImagesInDirectory(self):

        allImages = os.listdir(self.srcDirectory)
        
        print("total number of images to be resized is : "+ str(len(allImages)))
        
        # resize all images 
        for image in allImages :
            imgName = self.srcDirectory + '/' + image
            self.resizeImage(imgName,self.desImgSize)


def main():
    BASE_DIR = 'data3'
    SOURCE_DIR = 'org'
    DESTINATION_DIR = 'edit'
    DESTINATION_IMG_SIZE = (100,100) #tuple
    editImg = Transform(BASE_DIR,SOURCE_DIR,DESTINATION_DIR,DESTINATION_IMG_SIZE)
    editImg.resizeImagesInDirectory()

if __name__ == "__main__":
    main()