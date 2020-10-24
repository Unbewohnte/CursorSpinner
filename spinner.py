import pynput
from time import sleep
from math import radians,sin,cos
from pyautogui import size,mouseDown,mouseUp

class Spinner:
    def __init__(self):
        self.MOUSE = pynput.mouse.Controller()
        self.SCREEN = size()
        self.CENTER = self.SCREEN[0] // 2, self.SCREEN[1] // 2
        self.angle = 0
        self.Y = self.MOUSE.position[1]
        self.X = self.MOUSE.position[0]

        self.xpositions = []
        self.ypositions = []


    def movetoCenter(self):
        self.MOUSE.position = self.CENTER
        self.update_m_pos()
        print("Moved to center - ", str(self.MOUSE.position))

    def update_m_pos(self):
        self.Y = self.MOUSE.position[1]
        self.X = self.MOUSE.position[0]

    def m_dwn(self):
        mouseDown()
    def m_up(self):
        mouseUp()

    def calculate(self,circles = 1 ,angle_change = 30, rad_change = 0, radius = 60):
        steps = (circles * 360)// angle_change 
        print("{} STEPS".format(steps))

        for i in range(steps+1):
            self.xpositions.append(self.X - radius * cos(radians(self.angle))) #sin
            self.ypositions.append(self.Y - radius * sin(radians(self.angle))) #cos
            self.angle += angle_change

    def spin(self, press = True):
        print("Spinning...")
        for i in range(len(self.xpositions)):
            if (i == 1 and press == True):
                self.m_dwn()
            sleep(.005)
            self.MOUSE.position = (self.xpositions[i],self.ypositions[i])
            pass
        self.xpositions.clear()
        self.ypositions.clear()

        if (press == True):
            self.m_up()
        print("Done")
        pass