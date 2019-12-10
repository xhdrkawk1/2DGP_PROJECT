from pico2d import *
import main_state
import Struct


class CSlash:
    Image = None

    def __init__(self, x, y,dir):
        if CSlash.Image is None :
            CSlash.Image = load_image('Texture/Slash.png')
        self.x = x
        self.y = y
        self.dir = dir
        if(dir == 0):
            self.dir = -1
        self.frame = 0
        self.Count = 0
        self.Dead =False
        self.m_Rect = Struct.CRect(35, 30, self.x, self.y)

    def enter(self):
            pass

    def update(self):

        self.x = self.x - (self.dir * 15)

        self.Count += 1
        if (self.Count > 25):
            self.Dead = True

        self.m_Rect.PosX = self.x
        self.m_Rect.PosY = self.y

        return self.Dead

    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y
        if(self.dir == 1):
            CSlash.Image.composite_draw(0, 'h', self.x-ScrollX, self.y-ScrollY)
        else :
            CSlash.Image.draw(self.x-ScrollX, self.y-ScrollY)

