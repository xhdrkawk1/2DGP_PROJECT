from pico2d import *
import Struct
import main_state
import win32api

class CStage1:
    def __init__(self):
        self.Stage = 0
        self.backGroundImage = load_image('Texture/Stage1_Back.png')
        self.Image = load_image('Texture/Stage1.png')
        self.Image2 = load_image('Texture/Stage2.png')

    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        self.backGroundImage.draw(400,300)
        if(self.Stage==0):
            self.Image.clip_draw(10 + (int)(ScrollX * 0.29), 60, 200, 150, 400, 300, 800, 600)
        if(self.Stage==1):
            self.Image2.clip_draw(10 + (int)(ScrollX), 700, 800, 600, 400, 300, 800, 600)


    def update(self):
        if(self.Stage == 0):
            TempLst = main_state.m_ObjectMgr.Get_ObjectList('PLAYER')
            PlayerX = TempLst[0].x
            if(PlayerX>3550 and PlayerX<3620 and  win32api.GetAsyncKeyState(0x41) & 0x8000 ):
                 self.Stage = 1
                 main_state.m_ScrollMgr.resetScroll()
                 main_state.m_LineMgr.LineChange()
                 TempLst[0].x = 400
                 TempLst[0].y = 120
            if(win32api.GetAsyncKeyState(0x41) & 0x8000 ):
                self.Stage = 1
                main_state.m_ScrollMgr.resetScroll()
                TempLst[0].x = 400
                TempLst[0].y = 120
                main_state.m_LineMgr.LineChange()



        return False
        pass




