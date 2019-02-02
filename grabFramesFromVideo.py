'''
Author : Kunchala Anil
Date : 2 feb 2019
This script is used to grab the specified number of images from video
'''
import cv2
class Frames():
    
    def __init__(self,videoFileName,directoryToSave):
        self.videoObject = cv2.VideoCapture(videoFileName)
        self.totalFrames = 0
        self.frameHeight = 0
        self.frameWidth = 0
        self.directoryToSave = directoryToSave
        self.calculateFrameProperties()
    
    def calculateFrameProperties(self):
        self.totalFrames = int(self.videoObject.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frameHeight = self.videoObject.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frameWidth = self.videoObject.get(cv2.CAP_PROP_FRAME_WIDTH)

        print('total no of frames in video : ' + str(self.totalFrames))
        print('frame height  : ' + str(self.frameHeight))
        print('frame width : ' + str(self.frameWidth))


    def grabFrames(self,noOfFramesToCapture) :
       
        # calculate the step
        framesStep = int(self.totalFrames / noOfFramesToCapture)
        framesStep = framesStep + 1

        #grab frames using step
        for frameId in range(0,self.totalFrames , framesStep):
            self.videoObject.set(cv2.CAP_PROP_POS_FRAMES, frameId)
            sucess, image = self.videoObject.read()
            if sucess :
                imgName = self.directoryToSave + '/' + 'frame' + str(frameId) + '.jpg'
                cv2.imwrite(imgName,image)
                print("captured frame no : " + str(frameId))
            else :
                print("ERROR : unable to capture frame no : " + str(frameId))
        print("completed grabbing frames")

def main() :
    grabFrames = Frames('test.mp4','data/org')
    grabFrames.grabFrames(50)

main()