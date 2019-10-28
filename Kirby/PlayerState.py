from pico2d import *


class CPlayerState:
    def __init__(self):
        self.Image = load_image('Texture/StateSheet.png')
        self.PlayerState = 0 #0이면 노말

    def draw(self):
            self.Image.clip_draw(0,100, 50, 50, 50,510,80,80)

    def update(self):
        pass