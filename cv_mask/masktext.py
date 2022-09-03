import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
import cv2
import matplotlib.pyplot as plt


model = keras.models.load_model("my_model.h5")



# img = cv2.imread('mask_0.jpg')

import cv2

size = (300,300)
cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret,img = cap.read()
        img_org = img.copy()
        if ret:
            img = img[:, 80:500]
            img = cv2.resize(img, size)
            img = img/255.0
            img = img.reshape(-1,300,300,3)

            pred = model.predict(img)
            
            if pred > 0.5:
                cv2.putText(
                    img_org,'MASK', (50,100), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0)) 
                                # 문자열     시작점
            else:
                cv2.putText(
                    img_org,'noMASK', (50,100), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0)) 
                                # 문자열     시작점
            cv2.imshow('camera', img_org)



            if cv2.waitKey(1) != -1:
                break
                
            

        else:
            print('error')
            
else:
    print('Camera error')

cap.release()
cv2.destroyAllWindows()

