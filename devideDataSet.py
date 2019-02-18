'''
Author : Kunchala Anil
Email : anilkunchalaece@gmail.com
Date : Feb 2 2019

This script is used to devide the data set in to training and validation
dataset is in kitti format

Create two dirs in Root Folder
    images and labels and save those files in respective directories and run script

'''
import os,random,shutil

class DevideDataSet:
    def __init__(self,rootDir) :
        self.rootDir = rootDir
        self.trainDir = 'Train'
        self.valDir = 'Valid'
        self.testDir = 'Test'

        listOfDirectoriesToCreate = [
            self.trainDir,self.valDir,self.testDir
        ]
        self.createDirectoryStrecture(listOfDirectoriesToCreate)
        self.readAllClassesAndMakeDirStrecture(self.rootDir)
    
    def createDirectoryStrecture(self,dirList):
        for directory in dirList :
            # if directory exists remove it
            if os.path.isdir(directory) :
                shutil.rmtree(directory)
            os.mkdir(directory)
    
    def checkAndCreateDir(self,dirName):
        if os.path.isdir(dirName) :
            shutil.rmtree(dirName)
        os.mkdir(dirName)

    def readAllClassesAndMakeDirStrecture(self,rootDir):
        self.allClasses = os.listdir(rootDir)
        for className in self.allClasses :
            self.checkAndCreateDir(os.path.join(self.trainDir,className))
            self.checkAndCreateDir(os.path.join(self.valDir,className))
            self.checkAndCreateDir(os.path.join(self.testDir,className))
        
                 
    
    def devideData(self,valPercentage,testPercentage):

        # 'org' is subdirectory in class where images reside
        for className in self.allClasses :
            totalImages = os.listdir(os.path.join(self.rootDir,className,'org'))
            totalNoOfImages = len(totalImages)
            valImagesToTake = int((totalNoOfImages*valPercentage))
            randomEvalSet = random.sample(range(0,totalNoOfImages),valImagesToTake)

            testImagesToTake = int(valImagesToTake * testPercentage)
            randomTestSet = random.sample(range(0,valImagesToTake),testImagesToTake)

            for fileIndex in range(len(totalImages)) :
                srcPath = os.path.join(self.rootDir,className,'org',totalImages[fileIndex])
                if fileIndex in randomEvalSet :
                    if fileIndex in randomTestSet :
                        # copy image to test folder
                        desPath = os.path.join(self.testDir)
                    else :
                        # copy image to val folder
                        desPath = os.path.join(self.valDir,className)
                    shutil.copy2(srcPath, desPath)
                else :
                    desPath = os.path.join(self.trainDir,className)
                    shutil.copy2(srcPath, desPath)


def main():
    ROOT_DIR = 'data'
    EVAL_PERCENTAGE = 0.30
    TEST_PERCENTAGE_WITHIN_EVAL = 0.33
    data = DevideDataSet(ROOT_DIR)
    data.devideData(EVAL_PERCENTAGE,TEST_PERCENTAGE_WITHIN_EVAL)

if __name__ == '__main__' :
    main()