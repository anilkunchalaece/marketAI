import os
import cv2
import numpy as np

class PreprocessData:
    
    def __init__(self, rootDir):
        self.rootDir = rootDir
        self.trainDir = os.path.join(rootDir,'Train')
        self.validDir = os.path.join(rootDir,'Valid')
        self.testDir = os.path.join(rootDir,'Test')

        self.labelMapping  = ('beans','bottleGourd','brinjal','broadBeans','carrot','garlic',
                                    'ginger','green_chilli','ivyguard','lemon','oninon','potato',
                                    'radish','red_chilli','tomoto')
    
    def readImageReturnArray(self,imageName):
        imArray = cv2.imread(imageName,0)
        # print("image shape is {}".format(imArray.shape))
        #reshape the array
        imArray = np.reshape(imArray,imArray.shape[0]*imArray.shape[1])
        # print("image reshaped to {}".format(imArray.shape))
        return imArray

    def loadTestData(self) :
        testFeatureArray =[]
        testClassArray = []
        for classDir in os.listdir(self.testDir) :
            for imgName in os.listdir(os.path.join(self.testDir,classDir)) :
                imgPath = os.path.join(self.testDir,classDir,imgName)
                testFeatureArray.append(self.readImageReturnArray(imgPath))
                testClassArray.append(self.labelMapping.index(classDir))
        
        return (np.array(testFeatureArray) , np.array(testClassArray))

    def loadTrainData(self) :
        trainFeatureArray =[]
        trainClassArray = []
        for classDir in os.listdir(self.trainDir) :
            for imgName in os.listdir(os.path.join(self.trainDir,classDir)) :
                imgPath = os.path.join(self.trainDir,classDir,imgName)
                trainFeatureArray.append(self.readImageReturnArray(imgPath))
                # print(classDir)
                trainClassArray.append(self.labelMapping.index(classDir))
        
        return (np.array(trainFeatureArray) , np.array(trainClassArray))

    def loadValidData(self) :
        validFeatureArray =[]
        validClassArray = []
        for classDir in os.listdir(self.validDir) :
            for imgName in os.listdir(os.path.join(self.validDir,classDir)) :
                imgPath = os.path.join(self.validDir,classDir,imgName)
                validFeatureArray.append(self.readImageReturnArray(imgPath))
                validClassArray.append(self.labelMapping.index(classDir))
        
        return (np.array(validFeatureArray) , np.array(validClassArray))             


if __name__ == "__main__":
    ROOT_DIR = 'dataFormat'
    data = PreprocessData(ROOT_DIR)
    # data.readImageReturnArray("dataFormat/Train/beans/frame1008.jpg")
  
