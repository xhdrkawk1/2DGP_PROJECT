from pico2d import *
import Struct
import win32api

class CPlayer:
    def __init__(self):
        self.x, self.y = 200, 90
        self.frame = 0
        self.MaxFrame = 0
        self.imageRight = load_image('Texture/Kirby.png')
        self.imageLeft = load_image('Texture/KirbyL.png')
        self.LineLst = [Struct.CLinePos(0,90,800,90,0)]
        self.dir = 1
        self.PreAni ='DOWN'
        self.CurAni ='IDLE'
        self.AniLst = {'IDLE' : Struct.CAniDate(0,7,0),'DOWN':Struct.CAniDate(0,7,1),'WALK':Struct.CAniDate(0,9,2),'JUMP':Struct.CAniDate(0,8,4),'BLOW':Struct.CAniDate(0,13,12)}

    def enter(self):
        pass

    def update(self):

        self.Key_Input()
        self.AniMationCheck()
        self.Frame_Check()
        self.Move_Check()
        self.LineCollision()

    def draw(self):
        if self.dir== 0:
             self.imageRight.clip_draw(self.frame * 128, 2048-(self.AniLst[self.CurAni].AniNumber+1)*128, 128, 128, self.x, self.y)
        else:
             self.imageLeft.clip_draw((2048-128)-(self.frame * 128), 2048 - (self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,self.x, self.y)

    def AniMationCheck(self):
        if self.CurAni!= self.PreAni:
            self.frame = 0
            self.MaxFrame= self.AniLst[self.CurAni].MaxFrame

        self.PreAni=self.CurAni

    def Key_Input(self):
        if self.CurAni != 'BlOW' or self.CurAni != 'JUMP':
            self.CurAni = 'IDLE'
        if win32api.GetAsyncKeyState(0x28) & 0x8000:#아래
            self.CurAni = 'DOWN'
        if win32api.GetAsyncKeyState(0x25) & 0x8000:#왼쪽
            self.dir = 1
            self.CurAni = 'WALK'
        if win32api.GetAsyncKeyState(0x27) & 0x8000:#오른쪽
            self.CurAni = 'WALK'
            self.dir = 0
        if win32api.GetAsyncKeyState(0x26)&0x8000:  #위
            if self.CurAni!='JUMP':
               self.CurAni = 'JUMP'
        if win32api.GetAsyncKeyState(0x20) & 0x8000:  # 위
            if self.CurAni!='BlOW':
                self.CurAni = 'BLOW'

    def Frame_Check(self):
        self.frame = (int)(self.frame + 1)
        if(self.frame > self.MaxFrame):
            self.frame=0

    def LineCollision(self):
        for lineIndex in self.LineLst:
            if (int(lineIndex.p1y) <= int(self.x)) and lineIndex.p2x >= int(self.x):
                if(float(lineIndex.p2y - lineIndex.p1y)!=0):
                       fLineClimb = float(lineIndex.p2y - lineIndex.p1y)/ float(lineIndex.p2x - lineIndex.p1x)
                       fB = lineIndex.p1y-lineIndex.p1x*fLineClimb
                       self.y = fLineClimb*self.x+fB
                       break
                else:
                     self.y = lineIndex.p1y
                     break



    def Move_Check(self):
        if self.CurAni == 'WALK' and self.dir == 0:
            self.x = self.x+10
        elif self.CurAni == 'WALK' and self.dir == 1:
            self.x = self.x - 10


