from pico2d import *


class CPlayerState:
    def __init__(self):
        self.Image = load_image('Texture/StateSheet.png')
        self.PlayerState = 0 #0이면 노말

    def draw(self):
            self.Image.clip_draw(0,100, 50, 50, 700,510,120,120)

    def update(self):
        pass