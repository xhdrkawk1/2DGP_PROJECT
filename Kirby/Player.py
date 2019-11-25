from pico2d import *
import Struct
import win32api
import PlayerState
import main_state
import EatPlayer

m_PlayerState = None


class CPlayer:
    def __init__(self,x,y,dir):
        self.x, self.y = x, y
        self.frame = 0
        self.MaxFrame = 0
        self.imageRight = load_image('Texture/Kirby.png')
        self.imageLeft = load_image('Texture/KirbyL.png')
        self.dir = dir
        self.Eating =False
        self.fSpeed = 10
        self.fGravity = 20
        self.fJumpAcc = 1.5
        self.m_bisJump = False
        self.PreAni ='DOWN'
        self.AniStop =False
        self.CurAni ='IDLE'
        self.m_bisDead=0
        self.m_bisDamaged = False
        self.AniLst = {'IDLE' : Struct.CAniDate(0,7,0),'DOWN': Struct.CAniDate(0,7,1),'WALK':Struct.CAniDate(0,9,2),'JUMP':Struct.CAniDate(0,8,4),'BLOW':Struct.CAniDate(0,13,12),'FJUMP':
                       Struct.CAniDate(0,3,5),'BALLON': Struct.CAniDate(0,12,7),'FBALLON':Struct.CAniDate(0,2,8),'DAMAGED':Struct.CAniDate(0,8,9),'DRAIN':Struct.CAniDate(0,15,13)}
        self.m_Rect = Struct.CRect(128, 128, self.x, self.y)

    def enter(self):
        global m_PlayerState
        m_PlayerState = PlayerState.CPlayerState()
        pass

    def update(self):

        self.Key_Input()
        self.AniMationCheck()
        self.Frame_Check()
        self.Move_Check()
        self.LineCollision()
        self.Jumping()
        self.m_Rect.update(self.x, self.y)
        self.CollisionMonster()
        self.m_bisDamaged=False
        self.IsScrolling()
        if(self.Eating == True):
            self.m_bisDead=True
            m_Player = EatPlayer.CEatPlayer(self.x,self.y,self.dir)
            m_Player.enter()
            main_state.m_ObjectMgr.Add_Object('PLAYER', m_Player)


        return self.m_bisDead
    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        if self.dir== 0:
             self.imageRight.clip_draw((int)(self.frame) * 128, 2048-(self.AniLst[self.CurAni].AniNumber+1)*128, 128, 128, self.x-ScrollX, self.y-ScrollY)
        else:
             self.imageLeft.clip_draw((2048-128)-((int)(self.frame) * 128), 2048 - (self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128,self.x-ScrollX, self.y-ScrollY)

        m_PlayerState.draw()

    def AniMationCheck(self):
        if self.CurAni!= self.PreAni:
            self.frame = 0
            self.MaxFrame= self.AniLst[self.CurAni].MaxFrame

        self.PreAni=self.CurAni

    def Key_Input(self):
        if self.CurAni =='DAMAGED' or self.CurAni == 'DRAIN':
            return
        if self.CurAni == 'BALLON' and win32api.GetAsyncKeyState(0x41) & 0x8000 and self.PreAni == 'BALLON':
            self.CurAni = 'FBALLON'
            self.AniStop = False
        if  self.CurAni == 'JUMP' and win32api.GetAsyncKeyState(0x20) & 0x8000 and self.PreAni != 'BALLON':
            self.CurAni = 'BALLON'
            self.AniStop = False
        if  self.CurAni == 'BALLON' and  win32api.GetAsyncKeyState(0x27) & 0x8000 :
            self.dir = 0
        elif self.CurAni == 'BALLON' and  win32api.GetAsyncKeyState(0x25) & 0x8000 :
            self.dir = 1
        if self.CurAni != 'BlOW' and self.m_bisJump == False and self.CurAni != 'FJUMP':
            self.CurAni = 'IDLE'
        if(self.m_bisJump == True or self.CurAni == 'FJUMP'):
            return
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
               self.JumpingChecking()

        if win32api.GetAsyncKeyState(0x20) & 0x8000:  # 위
            if self.CurAni!='BlOW':
                self.CurAni = 'BLOW'

    def Frame_Check(self):
        if self.AniStop == False:
            self.frame = (self.frame + 0.3)
        if(self.frame > self.MaxFrame):
            if self.CurAni == 'JUMP' or self.CurAni == 'FBALLON':
                 self.AniStop = True
                 self.frame = self.MaxFrame
            elif self.CurAni == 'FJUMP':
                  self.CurAni = 'IDLE'
            elif self.CurAni == 'BALLON':
                self.frame=6
            elif self.CurAni =='DAMAGED':
                self.frame = 0
                self.CurAni ='IDLE'
            else :
                self.frame=0


    def LineCollision(self):
        Finish = False
        LineLst = main_state.m_LineMgr.LineLst;
        for lineIndex in LineLst:
            if Finish == True:
                return
            if (int(lineIndex.p1y) <= int(self.x)) and lineIndex.p2x >= int(self.x):
                Finish=True

                if(self.m_bisJump==False and self.y+30<lineIndex.p1y):
                 if(self.x <(lineIndex.p2x-lineIndex.p1x)/2+lineIndex.p1x): #중점보다크면
                    self.x = lineIndex.p1x
                 else:
                    self.x = lineIndex.p2x
                elif(self.m_bisJump==False):
                    if(self.y>lineIndex.p1y):
                        self.y=self.y-15
                        if(lineIndex.p1y>self.y):
                            self.y=lineIndex.p1y



                else:
                    if (int(lineIndex.p1y) <= int(self.x)) and lineIndex.p2x >= int(self.x) and self.y <lineIndex.p1y:
                        self.y = lineIndex.p1y
                        self.m_bisJump = False
                        self.fJumpAcc = 1.5
                        self.AniStop = False
                        self.CurAni = 'FJUMP'
                        self.frame =0




    def Move_Check(self):
        if self.CurAni == 'WALK' and self.dir == 0:
            self.x = self.x+10
        elif self.CurAni == 'WALK' and self .dir == 1:
            self.x = self.x - 10
        if self.CurAni == 'JUMP'and self.m_bisJump == True:
            if self.dir == 0:
                self.x = self.x + 7
            else :
                self.x = self.x - 7
        if self.CurAni == 'BALLON':
            if self.dir == 0:
                self.x = self.x + 5
            else :
                self.x = self.x - 5
        if self.CurAni == 'DAMAGED':
            if self.dir == 0:
                self.x = self.x - 5
            else:
                self.x = self.x + 5


    def Jumping(self):
        if self.m_bisJump == True :
            if self.CurAni == 'BALLON':
                self.fJumpAcc = 0.5
                self.y = self.y-self.fJumpAcc
            elif self.CurAni == 'FBALLON':
                self.fJumpAcc = 30.0
                self.y = self.y - self.fJumpAcc
            else:
                self.fJumpAcc = self.fJumpAcc + 1.0
                self.y = self.y+(self.fGravity-self.fJumpAcc)


    def CollisionMonster(self):
        if(self.CurAni=='DAMAGED'):
            return

        TempLst = main_state.m_ObjectMgr.Get_ObjectList('MONSTER')
        for n in TempLst:
            if(Struct.CollisionRect(self.m_Rect, n.m_Rect) and n.m_bisdie==False):
                self.CurAni = 'DAMAGED'
                self.frame = 0
                n.Collision = True
                TempLst2 = main_state.m_ObjectMgr.Get_ObjectList('UI')
                for n2 in TempLst2:
                    n2.change()

        if(self.CurAni == 'BLOW'and self.frame < 11):
             for n in TempLst:
                 if self.dir==0 and self.x< n.x  and Struct.CollisionDist(self.x,n.x,self.y,n.y,200):
                     self.CurAni = 'DRAIN'
                     n.m_bisdie = True
                 if self.dir == 1 and self.x > n.x and Struct.CollisionDist(self.x,n.x,self.y,n.y,200):
                     self.CurAni = 'DRAIN'
                     n.m_bisdie = True

    def IsScrolling(self):
        fOffsetX = 400
        fOffsetY = 300

        fScrollX = main_state.m_ScrollMgr.x
        fScrollY = main_state.m_ScrollMgr.y

        MoveX = 3
        MoveY = 3
        print(self.x)
        if(fOffsetX+50 <self.x - fScrollX):
            main_state.m_ScrollMgr.x= main_state.m_ScrollMgr.x+10
        if (fOffsetX - 50 > self.x - fScrollX):
            main_state.m_ScrollMgr.x = main_state.m_ScrollMgr.x -10
            if(main_state.m_ScrollMgr.x<0):
                main_state.m_ScrollMgr.x =0

    def JumpingChecking(self):
        LineLst = main_state.m_LineMgr.LineLst
        for lineIndex in LineLst:
            if (int(lineIndex.p1x) <= int(self.x)) and lineIndex.p2x >= int(self.x):
                if(self.dir == 0):
                    if(lineIndex.p2x - self.x>40):
                        self.CurAni = 'JUMP'
                        self.m_bisJump  = True

                else :
                    if (self.x-lineIndex.p1x > 40):
                        self.CurAni = 'JUMP'
                        self.m_bisJump = True
                return
        self.CurAni='IDLE'









