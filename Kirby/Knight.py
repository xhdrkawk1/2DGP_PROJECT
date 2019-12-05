from pico2d import *
import Struct
import main_state
import Effect

class CKnight:
    def __init__(self):
        self.x = 1300
        self.y = 210
        self.frame = 0
        self.MaxFrame = 0
        self.imageRight = load_image('Texture/KnightR.png')
        self.imageLeft = load_image('Texture/KnightL.png')
        self.dir = 1
        self.hp = 10
        self.PreAni = 'IDLE'
        self.AniStop = True
        self.CurAni = 'IDLE'
        self.AniLst ={'IDLE' : Struct.CAniDate(0,16,0),'WALK' :  Struct.CAniDate(0,7,1),'ATTACK' :  Struct.CAniDate(0,11,2)}
        self.CheckPlayer =False
        self.Dead=False
        self.m_Rect = Struct.CRect(99, 69, self.x, self.y)
        self.SkillCount = 0


    def update(self):

        self.CheckPlayerDist()
        self.FrameCheck()
        self.MotionCheck()
        self.m_Rect.update(self.x, self.y-80)
        return self.Dead


    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        if self.dir == 0:
            self.imageRight.clip_draw((int)(self.frame) * 99, 759 - (self.AniLst[self.CurAni].AniNumber + 1) * 69,
                                      99, 69, self.x - ScrollX, self.y - ScrollY,300,300)
        else:
            self.imageLeft.clip_draw((int)(self.frame) * 99, 759 - (self.AniLst[self.CurAni].AniNumber + 1) * 69,
                                      99, 69, self.x - ScrollX, self.y - ScrollY,300,300)
    def CheckPlayerDist(self):
        if(self.AniStop == False):
            return
        TempLst = main_state.m_ObjectMgr.Get_ObjectList('PLAYER')
        PlayerX =TempLst[0].x

        if(self.x -PlayerX <300):
            self.AniStop=False


    def FrameCheck(self):
        if(self.AniStop==True):
            return


        self.frame += 0.3
        if(self.frame>self.AniLst[self.CurAni].MaxFrame):
            if(self.CurAni == 'IDLE'):
                self.CurAni ='WALK'
            if(self.CurAni == 'ATTACK'):
                self.CurAni = 'WALK'
                self.SkillCount = 0

            self.frame = 0

    def change(self):
        pass

    def MotionCheck(self):
        if self.CurAni =='WALK':
            if(self.dir == 0):
                self.x = self.x + 2
            else :
                self.x = self.x -2
            TempLst = main_state.m_ObjectMgr.Get_ObjectList('PLAYER')
            PlayerX = TempLst[0].x
            if(PlayerX>self.x):
                self.dir =0
            else:
                self.dir =1
            self.SkillCount =self.SkillCount +1

        if(self.SkillCount == 100):
            self.CurAni = 'ATTACK'





