from pico2d import *
import Struct
import win32api
import PlayerState
import main_state

m_PlayerState = None


class CEatPlayer:
    def __init__(self,x,y,dira):
        self.x, self.y = x, y
        self.frame = 1
        self.MaxFrame = 3
        self.imageRight = load_image('Texture/EatKirbyR.png')
        self.imageLeft = load_image('Texture/EatKirbyL.png')
        self.LineLst = [Struct.CLinePos(-60, 120, 400, 120, 0), Struct.CLinePos(400, 180, 800, 180, 0)]
        self.dir = dira
        self.Eating = False
        self.fSpeed = 10
        self.fGravity = 20
        self.fJumpAcc = 1.5
        self.m_bisJump = False
        self.PreAni = 'DOWN'
        self.AniStop = False
        self.CurAni = 'IDLE'
        self.m_bisDead = 0
        self.m_bisDamaged = False
        self.AniLst = {'IDLE': Struct.CAniDate(0, 3, 0), 'DOWN': Struct.CAniDate(0, 5, 1),
                       'WALK': Struct.CAniDate(0, 15, 3), 'JUMP': Struct.CAniDate(0, 4, 4),'FJUMP':Struct.CAniDate(0, 2, 5)}
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
        self.Jumping()
        self.LineCollision()
        self.m_Rect.update(self.x, self.y)
        self.CollisionMonster()
        self.m_bisDamaged = False

        return self.m_bisDead

    def draw(self):
        if self.dir == 0:
            self.imageRight.clip_draw((int)(self.frame) * 128, 1280 - (self.AniLst[self.CurAni].AniNumber + 1) * 128,
                                      128, 128, self.x, self.y+15)
        else:
            self.imageLeft.clip_draw((2176 - 128) - ((int)(self.frame) * 128),
                                     1280 - (self.AniLst[self.CurAni].AniNumber + 1) * 128, 128, 128, self.x, self.y+15)
        m_PlayerState.draw()

    def AniMationCheck(self):
        if self.CurAni != self.PreAni:
            self.frame = 0
            self.MaxFrame = self.AniLst[self.CurAni].MaxFrame

        self.PreAni = self.CurAni

    def Key_Input(self):
        if self.CurAni != 'JUMP':
         self.CurAni = 'IDLE'
        else :
          return

        if win32api.GetAsyncKeyState(0x28) & 0x8000:  # 아래
            self.CurAni = 'DOWN'
        if win32api.GetAsyncKeyState(0x25) & 0x8000:  # 왼쪽
            self.dir = 1
            self.CurAni = 'WALK'
        if win32api.GetAsyncKeyState(0x27) & 0x8000:  # 오른쪽
            self.CurAni = 'WALK'
            self.dir = 0
        if win32api.GetAsyncKeyState(0x26) & 0x8000:  # 위
            if self.CurAni != 'JUMP':
                self.CurAni = 'JUMP'
                self.m_bisJump = True

    def Frame_Check(self):
        if self.AniStop == False:
            self.frame = (self.frame + 0.3)
        if (self.frame > self.MaxFrame):
                self.frame = 0

    def LineCollision(self):
        count = 0
        Finish = False
        for lineIndex in self.LineLst:
            if Finish == True:
                return
            count = count + 1
            if (int(lineIndex.p1y) <= int(self.x)) and lineIndex.p2x >= int(self.x):
                Finish = True
                print(count)
                if (self.m_bisJump == False and self.y + 30 < lineIndex.p1y):
                    if (self.x < (lineIndex.p2x - lineIndex.p1x) / 2 + lineIndex.p1x):  # 중점보다크면
                        self.x = lineIndex.p1x
                    else:
                        self.x = lineIndex.p2x
                elif (self.m_bisJump == False):
                    self.y = lineIndex.p1y


                else:
                    if (int(lineIndex.p1y) <= int(self.x)) and lineIndex.p2x >= int(self.x) and self.y < lineIndex.p1y:
                        self.y = lineIndex.p1y
                        self.m_bisJump = False
                        self.fJumpAcc = 1.5
                        self.AniStop = False
                        self.CurAni = 'FJUMP'
                        self.frame = 0

    def Move_Check(self):
        if self.CurAni == 'WALK' and self.dir == 0:
            self.x = self.x + 10
        elif self.CurAni == 'WALK' and self.dir == 1:
            self.x = self.x - 10
        if self.CurAni == 'JUMP' and self.m_bisJump == True:
            if self.dir == 0:
                self.x = self.x + 10
            else:
                self.x = self.x - 10

    def Jumping(self):
        if self.m_bisJump == True:
                self.fJumpAcc = self.fJumpAcc + 1.0
                self.y = self.y + (self.fGravity - self.fJumpAcc)

    def CollisionMonster(self):
        TempLst = main_state.m_ObjectMgr.Get_ObjectList('MONSTER')
        for n in TempLst:
            if (Struct.CollisionRect(self.m_Rect, n.m_Rect) and n.m_bisdie == False):
                self.CurAni = 'DAMAGED'
                self.frame = 0
                n.Collision = True
                TempLst2 = main_state.m_ObjectMgr.Get_ObjectList('UI')
                for n2 in TempLst2:
                    n2.change()









