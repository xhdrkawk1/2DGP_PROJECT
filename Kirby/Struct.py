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

