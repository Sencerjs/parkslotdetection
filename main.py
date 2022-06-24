import cv2
import pickle
import cvzone
import numpy as np

##camera source
video = cv2.VideoCapture("parkslot.mp4")

## rectangle
width = 105
height = 50

with open('parkSlotPos', 'rb') as f:
        posList = pickle.load(f)


def checkParkSlot(imgProcess):
    for pos in posList:
        cv2.rectangle(img, pos,(pos[0] + width, pos[1] + height),(255,0,0),3)


while True:
 
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)

 

    cv2.imshow("image", img)
    cv2.waitKey(1)

