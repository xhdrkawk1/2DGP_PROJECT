from pico2d import *
import Struct
import main_state


class CStage1:
    def __init__(self):
        self.backGroundImage = load_image('Texture/Stage1_Back.png')
        self.Image = load_image('Texture/Stage1.png')

    def draw(self):
        ScrollX = main_state.m_ScrollMgr.x
        ScrollY = main_state.m_ScrollMgr.y

        self.backGroundImage.draw(400,300)
        self.Image.clip_draw(10+(int)(ScrollX*0.29),60,200,150,400,300,800,600)

    def update(self):
        pass




