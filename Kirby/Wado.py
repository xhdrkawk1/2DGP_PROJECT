from pico2d import *
import Struct


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
        self.pointy = 0
        self.frame = 0
        self.Maxframe = 7
        self.CurAni = 'RUN'
        self.LineLst = [Struct.CLinePos(-30,120,800,120,0)]
        self.AniLst = {'RUN':Struct.CAniDate(0,7,0),'DAMAGE':Struct.CAniDate(0,7,1)}


    def draw(self):
        if self.dir == 0:
            CWado.ImageR.clip_draw(self.frame * 128, 384 - (self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,
                                      self.x, self.y)
        else:
            CWado.ImageL.clip_draw((1024 - 128) - (self.frame * 128), 384-(self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,self.x, self.y)

    def enter(self):
        for lineIndex in self.LineLst:
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
            if self.x < self.pointx2:
                self.x = self.pointx1
                self.dir = 0






    def update(self):
        self.MoveFrame()
        self.MoveWade()


    def MoveFrame(self):
        self.frame = (int)(self.frame + 1)
        if(self.frame>self.Maxframe):
            self.frame = 0