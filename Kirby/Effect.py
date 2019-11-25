from pico2d import *
import main_state

#Type 0= Run,1 = Puff 2. Absorb
class CEffect:
    ImageRun  = None
    ImageRunL  = None
    ImagePuff = None
    ImageAbsorb = None
    def __init__(self,x,y,type,Compos):
        self.x = x
        self.y = y
        self.type = type
        self.dir = Compos
        self.MaxFrame = 0
        self.Dead = False
        if CEffect.ImageRun is None or CEffect.ImageRunL is None and self.type == 0:
            CEffect.ImageRun = load_image('Texture/Run.png')
            CEffect.ImageRunL = load_image('Texture/RunL.png')
        if CEffect.ImagePuff is None and self.type == 1:
            CEffect.ImagePuff = load_image('Texture/Puff.png')
        if CEffect.ImageAbsorb is None and self.type == 2:
            CEffect.ImageAbsorb = load_image('Texture/Absorb.png')

        if(self.type==0):
            self.MaxFrame = 11
            self.Speed = 0.5
        if(self.type==1):
            self.MaxFrame =6
            self.Speed = 0.2

        if(self.dir==1):
            self.frame = 0
        else:
            self.frame =self.MaxFrame

    def update(self):
        if(self.dir ==1):
            self.frame =self.frame+self.Speed
            if(self.frame>self.MaxFrame):
               self.Dead = True
        else:
            self.frame = self.frame - self.Speed
            if (self.frame <0):
                self.Dead = True

        return self.Dead

    def draw(self):

        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        if(self.type == 0):
            if(self.dir==1):
                CEffect.ImageRun.clip_draw((int)(self.frame) * 80, 0, 80, 80,
                                   self.x - ScrollX, self.y - ScrollY,40,40)
            else:
                CEffect.ImageRunL.clip_draw((int)(self.frame) * 80, 0, 80, 80,
                                           self.x - ScrollX, self.y - ScrollY,40,40)

        if (self.type == 1):
            CEffect.ImagePuff.clip_draw((int)(self.frame) * 192, 0, 192, 192,
                                       self.x - ScrollX, self.y - ScrollY)

