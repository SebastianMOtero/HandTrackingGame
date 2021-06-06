import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import MyObject as mo

prevTime = 0
currTime = 0
show_FPS = True
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
circle = False
balls = 0
sec = 0
start = time.time()
time.clock()

while True:
    # Grabs, decodes and returns the next video frame.
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    # Para printear una posicion de un punto de una mano -> print(lmList[0])
    #if len(lmList) != 0:
        #print(lmList[4])

    # if show_FPS:
    #     currTime = time.time()
    #     fps = 1 / (currTime - prevTime)
    #     prevTime = currTime
    #     cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # create
    if circle == False:
        o1 = mo.Object()
        circle = True

    o1.draw(img)
    o1.move()
    if len(lmList) != 0:
        busted = o1.busted(lmList[4], lmList[8])
        if busted:
            circle = False
            balls+=1

    sec = time.time() - start
    cv2.putText(img, str(int(sec)) + ' seconds.', (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 0)
    cv2.putText(img, 'Balls: ' + str(int(balls)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 0)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
