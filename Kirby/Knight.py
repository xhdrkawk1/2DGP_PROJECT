from pico2d import *
import Struct
import main_state
import Effect
import Slash
import random
import Wado
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
        self.WadoCount = 0
        self.hp = 5


    def update(self):

        self.CheckPlayerDist()
        self.FrameCheck()
        self.MotionCheck()
        self.m_Rect.update(self.x, self.y-80)
        self.MakeSlash()
        self.MakeWado()

        self.PreAni = self.CurAni
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
                self.x = self.x + 1.5
            else :
                self.x = self.x -1.5
            TempLst = main_state.m_ObjectMgr.Get_ObjectList('PLAYER')
            PlayerX = TempLst[0].x
            if(PlayerX>self.x):
                self.dir =0
            else:
                self.dir =1
            self.SkillCount =self.SkillCount +1

        if(self.SkillCount == 200):
            self.CurAni = 'ATTACK'
    def MakeSlash(self):
        if(self.CurAni =='ATTACK' and self.PreAni != 'ATTACK'):
            Attack = Slash.CSlash(self.x,self.y-65,self.dir)
            main_state.m_ObjectMgr.Add_Object('BOSSBULLET',Attack)


    def MakeWado(self):
        self.WadoCount=self.WadoCount+1
        if(self.WadoCount > 200):

            rand = random.randint(0,1)

            if(rand==1):
               Mon1 = Wado.CWado(0, 120, 0)
            else:
               Mon1 = Wado.CWado(2000, 120, 1)

            Mon1.enter()
            main_state.m_ObjectMgr.Add_Object('MONSTER', Mon1)
            self.WadoCount = 0






