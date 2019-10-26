import random
import json
import os
import ObjectMgr

from pico2d import *

import game_framework
import Player


name = "MainState"

boy = None
grass = None
font = None
m_ObjectMgr = None

class Font:
    def __init__(self):
        self.image = load_image('paused.png')

    def draw(self):
        self.image.draw(400, 300)


def enter():
    global m_ObjectMgr
    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_ObjectMgr.Add_Object('Player', Player.CPlayer())

def exit():
    pass


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


def draw():
    clear_canvas()
    m_ObjectMgr.Draw_Object()
    update_canvas()
