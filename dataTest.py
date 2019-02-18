import tensorflow as tf
from tensorflow import keras 

class loadData:
    def __init__ (self):
        ROOT_DIR = 'dataFormat'


    def getGenerators(self):
        train_datagen = keras.preprocessing.image.ImageDataGenerator()
        valid_datagen = keras.preprocessing.image.ImageDataGenerator()
        test_datagen = keras.preprocessing.image.ImageDataGenerator()

        train_generator = train_datagen.flow_from_directory(
            directory=r"dataFormat/Train/",
            target_size=(100, 100),
            color_mode="grayscale",
            batch_size=12,
            class_mode="categorical",
            shuffle=True,
            seed=42
        )
        valid_generator = valid_datagen.flow_from_directory(
            directory=r"dataFormat/Valid/",
            target_size=(100, 100),
            color_mode="grayscale",
            batch_size=32,
            class_mode="categorical",
            shuffle=True,
            seed=32
        )

        test_generator = test_datagen.flow_from_directory(
            directory=r"dataFormat/Test/",
            target_size=(100, 100),
            color_mode="grayscale",
            batch_size=1,
            class_mode=None,
            shuffle=False,
            seed=22
        )

        STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
        STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size

        print(STEP_SIZE_TRAIN)
        return (train_generator,valid_generator,test_generator)

if __name__ == '__main__':
    data = loadData()