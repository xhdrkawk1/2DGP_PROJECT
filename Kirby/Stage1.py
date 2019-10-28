from pico2d import *
import Struct


class CStage1:
    def __init__(self):
        self.backGroundImage = load_image('Texture/Stage1_Back.png')
        self.Image = load_image('Texture/Stage1.png')

    def draw(self):
        self.backGroundImage.draw(400,300)
        self.Image.clip_draw(10,60,200,150,400,300,800,600)





