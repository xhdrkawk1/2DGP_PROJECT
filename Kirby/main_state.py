import random
import json
import os

from pico2d import *
import Stage1
import game_framework
import Player
import PlayerHp
import ObjectMgr
import Wado

name = "MainState"



font = None
m_ObjectMgr = None


class Font:
    def __init__(self):
        self.image = load_image('paused.png')

    def draw(self):
        self.image.draw(400, 300)


class Grass:
    def __init__(self):
        self.image = load_image('Texture/Stage1.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global  m_ObjectMgr
    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_Player = Player.CPlayer()
    m_Player.enter()
    m_ObjectMgr.Add_Object('PLAYER', m_Player)

    m_Stage1 = Stage1.CStage1()
    m_ObjectMgr.Add_Object('MAP', m_Stage1)

    m_PlayerHp = PlayerHp.CPlayerHp()
    m_ObjectMgr.Add_Object('UI', m_PlayerHp)

    m_Wado =Wado.CWado(100,120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER',m_Wado)



def exit():
    global m_Player,m_Stage1,m_PlayerHp,m_ObjectMgr

    del(m_ObjectMgr)


def pause():
    pass


def resume():
    pass


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()




def update():
    m_ObjectMgr.Update_Object()
    delay(0.015)

def draw():
    clear_canvas()
    m_ObjectMgr.Draw_Object()
    update_canvas()
