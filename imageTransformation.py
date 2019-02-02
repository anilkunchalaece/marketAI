
'''
Author : Kunchala Anil
Date : 2 feb 2019
This script is used to perform basic transformations on  images
'''
import cv2
import numpy
import os,shutil

class Transform:
    def __init__(self):
        self.imageHeight = 0
        self.imageWidth = 0
        self.imgBaseDirectory = 'data/'
        self.srcDirectory = self.imgBaseDirectory+'org/'
        self.directoryToSave = self.imgBaseDirectory+'edit/'
    
    def calculateImageProperties(self,imageObj):
        self.imageHeight , self.imageWidth = imageObj.shape[:2]

    def resizeImage(self,image,destImgSize):
        '''
        imageObj : source image 
        destImgSize : destination image size as tuple (height ,width)
        '''
        srcImageObj = cv2.imread(image)
        self.calculateImageProperties(srcImageObj)
        destImageName = self.directoryToSave+ image.replace('data/org/','')

        output = cv2.resize(srcImageObj,destImgSize,interpolation=cv2.INTER_LINEAR)
        print(destImageName)
        cv2.imwrite(destImageName,output)
    
    def resizeImagesInDirectory(self,srcDirectory,desImgSize):

        allImages = os.listdir(self.imgBaseDirectory + srcDirectory)
        
        print("total number of images to be resized is : "+ str(len(allImages)))
        
        # resize all images 
        for image in allImages :
            imgName = self.imgBaseDirectory + srcDirectory + '/' + image
            self.resizeImage(imgName,desImgSize)


def main():
    editImg = Transform()
    desImgSize = (200,200) #tuple
    editImg.resizeImagesInDirectory('org',desImgSize)

main()