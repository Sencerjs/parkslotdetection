import cv2
import pickle

img = cv2.imread("parkslotimage.png")

try:
    with open('parkSlotPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

## rectangle size
width = 105
height = 50

def onClick(events, x, y ,flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)


    with open('parkSlotPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('parkslotimage.png')
    for pos in posList:
        cv2.rectangle(img, pos,(pos[0] + width, pos[1] + height),(0,0,128),2)

    cv2.imshow("image",img)
    cv2.setMouseCallback("image",onClick)
    cv2.waitKey(5)