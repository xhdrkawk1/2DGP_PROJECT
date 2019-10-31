from pico2d import *


class CAniDate:
       def __init__(self, x, y,index):
           self.MixFrame, self.MaxFrame = x, y
           self.AniNumber= index


class CLinePos:
       def __init__(self, x1, y1, x2, y2, option):
           self.p1x = x1
           self.p1y = y1
           self.p2x = x2
           self.p2y = y2
           self.Option = option

class CRect:
    def __init__(self,x,y,PositionX,PositionY):
        self.PosX = PositionX
        self.PosY = PositionY
        self.YLength = y/2
        self.XLength = x/2

    def update(self,x,y):
        self.PosX = x
        self.PosY = y


def CollisionRect(R1,R2):
     if abs(R1.PosX-R2.PosX) < R1.XLength+R2.XLength and abs(R1.PosY-R2.PosY) < R1.YLength+R2.YLength:
           return True

     return False

