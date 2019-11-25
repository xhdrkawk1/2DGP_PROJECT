from pico2d import *
import Struct
import main_state


class CWado:
    ImageL = None
    ImageR = None

    def __init__(self, x, y):

        if CWado.ImageL is None and CWado.ImageR is None:
            CWado.ImageL = load_image('Texture/WadoL.png')
            CWado.ImageR = load_image('Texture/WadoR.png')

        self.dir = 0
        self.x = x
        self.y = y
        self.pointx1 = 0
        self.pointx2 = 0
        self.m_bisDead = 0
        self.pointy = 0
        self.frame = 0
        self.Maxframe = 7
        self.SizeX = 128
        self.SizeY = 128
        self.CurAni = 'RUN'
        self.AniLst = {'RUN': Struct.CAniDate(0,7,0),'DAMAGE': Struct.CAniDate(0,7,1),'FLY':Struct.CAniDate(0,0,2)}
        self.m_Rect = Struct.CRect(64,64,self.x,self.y)
        self.Collision = False
        self.m_bisdie = False;
    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        if self.dir == 0:
            CWado.ImageR.clip_draw((int)(self.frame) * 128, 384 - (self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,
                                      self.x-ScrollX, self.y-ScrollY,self.SizeX,self.SizeY)
        else:
            CWado.ImageL.clip_draw((1024 - 128) - ((int)(self.frame) * 128), 384-(self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,self.x-ScrollX, self.y-ScrollY,self.SizeX,self.SizeY)

    def enter(self):
        global  m_Rect
        LineLst = main_state.m_LineMgr.LineLst
        for lineIndex in LineLst:
            if lineIndex.p1x < self.x and lineIndex.p2x > self.x:
                self.pointx1 = lineIndex.p1x
                self.pointx2 = lineIndex.p2x
                self.pointy = lineIndex.p1y
                break

    def MoveWade(self):
        if self.CurAni != 'RUN':
           return

        if self.dir==0:
            self.x = self.x +1
            if self.x > self.pointx2:
                self.x=self.pointx2
                self.dir = 1
        else:
            self.x = self.x -1
            if self.x < self.pointx1:
                self.x = self.pointx1
                self.dir = 0






    def update(self):
        self.MoveFrame()
        self.MoveWade()
        self.m_Rect.update(self.x, self.y)

        if self.Collision==True :
            if(self.dir==0):
                self.dir=1
            else:
                self.dir=0

        self.Collision = False
        self.Drain()
        return self.m_bisDead
    def MoveFrame(self):
        self.frame = self.frame + 0.3
        if(self.frame>self.Maxframe):
            self.frame = 0

    def Drain(self):
        if self.m_bisdie==True:
            self.SizeY = self.SizeY-(self.SizeY*0.02)
            self.SizeX = self.SizeX - (self.SizeX * 0.02)
            self.CurAni = 'FLY'
            self.Maxframe = 0
            TempLst = main_state.m_ObjectMgr.Get_ObjectList('PLAYER')
            PlayerX =TempLst[0].x
            self.x = self.x+(PlayerX-self.x)*0.1
            if(math.sqrt((PlayerX-self.x)**2)<10):
                TempLst[0].CurAni = 'IDLE'
                TempLst[0].Eating = True
                self.m_bisDead = True






