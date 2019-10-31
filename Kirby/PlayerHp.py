from pico2d import *
import win32api
import Struct

class CPlayerHp:
    def __init__(self):
        self.Image = load_image('Texture/PlayerHp.png')
        self.PlayerHp = 20
        self.m_bisDead = 0
    def draw(self):
        self.Image.clip_draw(0,0, 388, 64, 200,500)
        self.Image.clip_draw(0,64, 388-(16*(25-(self.PlayerHp+5))), 64, 200-(8*(25-(self.PlayerHp+5))), 500)

    def update(self):
        if win32api.GetAsyncKeyState(0x47) & 0x8000:
            self.PlayerHp = self.PlayerHp-1
        return self.m_bisDead
    def change(self):
        self.PlayerHp = self.PlayerHp - 1