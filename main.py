import cv2
import pickle
import cvzone
import numpy as np

## camera source
video = cv2.VideoCapture("parkslot.mp4")

## rectangle size
width = 105
height = 50

with open('parkSlotPos', 'rb') as f:
        posList = pickle.load(f)


def checkParkSlot(imgProcess):
    slotCounter = 0
    for pos in posList:
        x, y = pos

        imgCrop = imgProcess[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)
    
        if count < 950:
            color = (90, 190, 0)
            thickness = 3
            slotCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

## information space
    cvzone.putTextRect(img, f'Available Slot: {slotCounter}/{len(posList)}', (700, 50), scale=2,
                           thickness=1, offset=10, font=1, colorR=(90,190,0))
    cvzone.putTextRect(img, f'Powered by OpenCV', (50, 50), scale=1,
                           thickness=1, offset=10, font=1, colorR=(90,190,0))


while True:
 
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

 
    checkParkSlot(imgDilate)
    cv2.imshow("image", img)
    cv2.waitKey(5)

