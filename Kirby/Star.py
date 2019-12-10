from pico2d import *
import main_state
import Struct
import Effect
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
        self.m_Rect = Struct.CRect(35, 30, self.x, self.y)
    def enter(self):
        pass

    def update(self):

        self.x = self.x-(self.dir * 20)

        self.Count += 1
        if(self.Count>25):
            self.Dead = True

        self.frame =self.frame+0.3
        if(self.frame>5):
            self.frame=0

        self.m_Rect.PosX = self.x
        self.m_Rect.PosY = self.y

        self.CollisionMonster()

        return self.Dead

    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y
        CStar.Image.clip_draw((int)(self.frame) * 104, 0, 104, 96,self.x-ScrollX, self.y-ScrollY,70,60)

    def CollisionMonster(self):
        TempLst = main_state.m_ObjectMgr.Get_ObjectList('MONSTER')
        for n in TempLst:
            if (Struct.CollisionRect(self.m_Rect, n.m_Rect) and n.m_bisdie == False):
                self.Dead=True
                n.m_bisStar=True

        TempLst2 = main_state.m_ObjectMgr.Get_ObjectList('BOSS')
        for n in TempLst2:
            if (Struct.CollisionRect(self.m_Rect, n.m_Rect) and n.Dead == False):
                self.Dead = True
                n.hp = n.hp-1
                PuffEffect = Effect.CEffect(self.x, self.y, 1, 1)
                main_state.m_ObjectMgr.Add_Object('EFFECT', PuffEffect)




