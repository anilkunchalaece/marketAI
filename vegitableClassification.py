#import numpy and tensorflow
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2

from preprocessData import PreprocessData

# check the versions of tensorflow and keras
print("tensorflow version is {}".format(tf.__version__))
print("keras version is {}".format(tf.keras.__version__))

DATA_ROOT_FOLDER = 'dataFormat'

# load data
data = PreprocessData(DATA_ROOT_FOLDER)
x_train,y_train = data.loadTrainData()
x_test,y_test = data.loadTestData()

#lets see the image
# cv2.imshow("pl",x_train[1].reshape(100,100))
# wait 3 sec before going further
# cv2.waitKey(3000)


#Define Keras Trainning and Networking parameters
NB_EPOCH = 5000
BATCH_SIZE = 50
VERBOSE = 1 # tf verbose level
NB_CLASSES = 15 # Number of outputs i.e 10 for MNIST
VALIDATION_SPLIT = 0.2


# Noramailize the Train and Test Feature Set

x_test = x_test / np.max(x_test)
x_train = x_train / np.max(x_train)

cv2.imshow("pl",x_train[1].reshape(100,100))
# wait 3 sec before going further
cv2.waitKey(3000)

#Convert labels in to categerolical class metrics
y_train = keras.utils.to_categorical(y_train,NB_CLASSES)
y_test = keras.utils.to_categorical(y_test,NB_CLASSES)

#lets check one of categorical label
# print(y_train[0])

# The  " HOLY MODEL "
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(100,input_shape=(100*100,),activation='relu'))
#model.add(tf.keras.layers.Dropout(0.2))
# model.add(tf.keras.layers.Dense(1000,activation='relu'))
# model.add(tf.keras.layers.Dense(100,activation='relu'))
# model.add(tf.keras.layers.Dense(50,activation='relu'))
model.add(tf.keras.layers.Dense(25,activation='relu'))
#model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.Dense(NB_CLASSES,activation='softmax'))

model.summary()

# Compile the model
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])

# Train the model
history = model.fit(x_train,y_train,batch_size=BATCH_SIZE,epochs=NB_EPOCH,verbose=VERBOSE,
          validation_split=VALIDATION_SPLIT)

# Evaluate a model
score = model.evaluate(x_test,y_test,verbose=VERBOSE)
print("test score {} ".format(score[0]))
print("test accuracy {}".format(score[1]))
