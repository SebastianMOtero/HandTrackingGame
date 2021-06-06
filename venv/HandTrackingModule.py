import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,static_image_mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.min_detection_confidence, self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        # Converts to RGB since hands class use RGB images
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process image
        self.results = self.hands.process(imgRGB)

        # Extract data for multiple hands
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo = 0, draw = True):
        lmList = []
        if self.results.multi_hand_landmarks:
            # Get one hand
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                # Get location in pixels
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    if id == 0 or id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList

def main():
    prevTime = 0
    currTime = 0
    show_FPS = True
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        # Grabs, decodes and returns the next video frame.
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        # Para printear una posicion de un punto de una mano -> print(lmList[0])
        #if len(lmList) != 0:
            #print(lmList[4])

        if show_FPS:
            currTime = time.time()
            fps = 1 / (currTime - prevTime)
            prevTime = currTime
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()