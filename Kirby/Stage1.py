from pico2d import *
import Struct
import main_state
import win32api

class CStage1:
    def __init__(self):
        self.Stage = 0
        self.backGroundImage = load_image('Texture/Stage1_Back.png')
        self.backGroundImage2 = load_image('Texture/Stage2_Back.png')
        self.Image = load_image('Texture/Stage1.png')
        self.Image2 = load_image('Texture/Stage2.png')


        self.Stage1Sound = load_music('Sound/Stage5.mp3')
        self.Stage1Sound.set_volume(20)
        self.Stage1Sound.repeat_play()



    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y


        if(self.Stage==0):
            self.backGroundImage.draw(400, 300)
            self.Image.clip_draw(10 + (int)(ScrollX * 0.29), 60, 200, 150, 400, 300, 800, 600)
        if(self.Stage==1):
            self.backGroundImage2.draw(400, 300)
            self.Image2.clip_draw(10 + (int)(ScrollX*0.5), 150, 400, 300, 400,300, 800, 600)
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
        return False

    def change(self):
        self.Stage2Sound.repeat_play()

    def enter(self):
      pass



