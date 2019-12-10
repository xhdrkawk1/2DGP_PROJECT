from pico2d import *
import win32api
import Struct

class CBossHp:
    def __init__(self):
        self.Image = load_image('Texture/BossHp.png')
        self.BossHp = 5
        self.m_bisDead = 0
    def draw(self):
        self.Image.clip_draw(0,0, 388, 64, 500,500)
        self.Image.clip_draw(0,64, 388-(16*(25-(self.BossHp+5))), 64, 500-(8*(25-(self.BossHp+5))), 500)

    def update(self):

        return self.m_bisDead
