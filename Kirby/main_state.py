import random
import json
import os

from pico2d import *
import Stage1
import game_framework
import Player
import PlayerHp
import ObjectMgr
import ScrollMgr
import LineMgr
import Wado

name = "MainState"



font = None
m_ObjectMgr = None
m_ScrollMgr = None
m_LineMgr =None


def enter():
    global m_LineMgr
    m_LineMgr = LineMgr.CLineMgr()

    global  m_ObjectMgr
    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_Player = Player.CPlayer(200,120,1)
    m_Player.enter()
    m_ObjectMgr.Add_Object('PLAYER', m_Player)

    m_Stage1 = Stage1.CStage1()
    m_ObjectMgr.Add_Object('MAP', m_Stage1)

    m_PlayerHp = PlayerHp.CPlayerHp()
    m_ObjectMgr.Add_Object('UI', m_PlayerHp)

    m_Wado =Wado.CWado(2500,120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER',m_Wado)

    m_Wado = Wado.CWado(800, 120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER', m_Wado)

    m_Wado = Wado.CWado(3000, 120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER', m_Wado)

    m_Wado = Wado.CWado(1400, 120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER', m_Wado)

    m_Wado = Wado.CWado(2000, 120)
    m_Wado.enter()
    m_ObjectMgr.Add_Object('MONSTER', m_Wado)

    global m_ScrollMgr
    m_ScrollMgr = ScrollMgr.CScrollMgr()




def exit():
    global m_Player,m_Stage1,m_PlayerHp,m_ObjectMgr,m_LineMgr

    del(m_LineMgr)
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
