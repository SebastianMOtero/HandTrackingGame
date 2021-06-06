import cv2
import random

LIMIT_BOTTOM = 480
LIMIT_TOP = 0
LIMIT_LEFT = 0
LIMIT_RIGHT = 640

class Object():
    def __init__(self):
        self.posX = random.randint(1, 200)
        self.posY = random.randint(1, 200)
        self.radius = random.randint(5, 15)
        self.velX = random.randint(-5, 5)
        self.velY = random.randint(-5, 5)
        self.colorR = random.randint(1, 255)
        self.colorG = random.randint(1, 255)
        self.colorB = random.randint(1, 255)

    def move(self):
        # Check limit RIGHT
        if self.posX + self.velX >= LIMIT_RIGHT - self.radius:
            self.posX = LIMIT_RIGHT - self.radius
            self.velX = self.velX * -1
        else:
            # Check limit LEFT
            if self.posX + self.velX <= LIMIT_LEFT + self.radius:
                self.posX = LIMIT_LEFT + self.radius
                self.velX *= -1
            else:
                self.posX += self.velX
        # Check limit BOTTOM
        if self.posY + self.velY >= LIMIT_BOTTOM - self.radius:
            self.posY = LIMIT_BOTTOM - self.radius
            self.velY *= -1
        else:
            # Check limit TOP
            if self.posY + self.velY <= LIMIT_TOP + self.radius:
                self.posY = LIMIT_TOP + self.radius
                self.velY *= -1
            else:
                self.posY+= self.velY
        return

    def draw(self, img):
        cv2.circle(img, (self.posX, self.posY), self.radius, (self.colorR, self.colorG, self.colorB), cv2.FILLED)
        return

    def busted(self, d4, d8):
        if abs(d4[1]-d8[1]) <= 20 and abs(d4[2]-d8[2]) <= 20:
            if abs( ((d4[1] + d8[1]) / 2) - self.posX) <= 20:
                if abs(((d4[2] + d8[2]) / 2) - self.posY) <= 20:
                    return True
