from pico2d import *
import main_state


class CStar:
    Image = None

    def __init__(self, x, y,dir):
        if CStar.Image is None :
            CStar.Image = load_image('Texture/Star.png')
        self.x = x
        self.y = y
        self.dir = dir
        if(dir == 0):
            self.dir = -1
        self.frame = 0
        self.Count = 0
        self.Dead =False

    def enter(self):
        pass

    def update(self):
        self.x = self.x-(self.dir * 10)

        self.Count += 1
        if(self.Count>70):
            self.Dead = True

        self.frame =self.frame+0.3
        if(self.frame>5):
            self.frame=0

        return self.Dead

    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y
        CStar.Image.clip_draw((int)(self.frame) * 104, 0, 104, 96,self.x-ScrollX, self.y-ScrollY,70,55)

