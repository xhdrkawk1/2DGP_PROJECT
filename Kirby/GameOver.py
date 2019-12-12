from pico2d import *

import main_state

class CGameover:
    def __init__(self):
        self.frame=0
        self.maxframe =13
        self.image = load_image('Texture/Gameover.png')
        self.Sound = load_wav('Sound/Za.wav')
        self.Sound.set_volume(50)
        self.Sound.play()
    def update(self):
        self.frame +=0.1
        if (self.frame > self.maxframe):
            self.frame=self.maxframe
        return False

    def draw(self):
        self.image.clip_draw((int)(self.frame) *216,0,216,174, 400,300,800,600)

