# importing modules
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import sys,os
import cv2
path=sys.argv[1]+" "+sys.argv[2]

if os.path.isfile(r"/app/UI/static/ml/pred.jpg"):
        os.system("rm /app/UI/static/ml/pred.jpg")


print(path)
# Loading model
model1 = load_model('/app/BT_MODEL-v1.h5')

# Preprocessing the Training set
train_data = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_data.flow_from_directory('/app/Dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
# Preprocessing the Testing set
test_data = ImageDataGenerator(rescale = 1./255)
test_set = test_data.flow_from_directory('/app/Dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')
# Predicting using the above created model
pred_image = image.load_img(path, target_size=(64,64))
pred_image = image.img_to_array(pred_image)
pred_image = np.expand_dims(pred_image, axis = 0)
result = model1.predict(pred_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'yes'
    # os.system(r"mkdir C:\script\a")
else:
    prediction = 'no'
print(prediction)

img =cv2.imread(path)
image_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HLS  )
# cimg = convolve2d(image_HSV, f) # Convolve cimbines both n reduces pixels of images
print("Before Saving")
if result[0][0] == 1:
    prediction = 'yes'
    cv2.imwrite("/app/UI/static/ml/pred.jpg",image_HSV)
else:
    pass


