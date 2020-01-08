# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:20:43 2020

@author: rgvaish
"""
#---------------Finding FPS of video---------------------------------------------------------------------------------------------------------

import numpy as np
import cv2
import os 

cap = cv2.VideoCapture('C:/Users/rgvaish/Documents/vid/aaagqkcdis.mp4')
    
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if int(major_ver)  < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    
    
#------------------------------Extracting full image from frames--------------------------------------------------------------------------------
    
try: 
    if not os.path.exists('C:/Users/rgvaish/Documents/vid/'): 
        os.makedirs('C:/Users/rgvaish/Documents/vid/') 
  
except OSError: 
    print ('Error: Creating directory of data') 
  
currentframe = 0
 
while(True):  
    ret,frame = cap.read() 
  
    if ret: 
        name = 'C:/Users/rgvaish/Documents/vid/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
        cv2.imwrite(name, frame) 
        currentframe += 1
    else: 
        break
   
cap.release() 
cv2.destroyAllWindows()     

#-------------------------Face detection-----------------------------------------------------------------------------------------------------
from mtcnn import MTCNN

img = cv2.cvtColor(cv2.imread('C:/Users/rgvaish/Documents/vid/frame0.jpg'), cv2.COLOR_BGR2RGB)
detector = MTCNN()
detector.detect_faces(img)

cro = img[846, 158, 74, 94]
