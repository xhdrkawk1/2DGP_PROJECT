import game_framework
import pico2d

class GameObject:
    def __init__(self, state):
        self.draw = state.draw
        self.exit = state.exit
        self.handle_events = state.handle_events
        self.update = state.update


class CObjectMgr:
    def __init__(self):
        self.ObjLst = {'Player': []}

    def Update_Object(self):
        for index in self.ObjLst:
            for index2 in self.ObjLst[index]:
                self.ObjLst[index][index2].update()

    def Draw_Object(self):
        for index in self.ObjLst:
            for index2 in self.ObjLst[index]:
                Lst = self.ObjLst[index].draw()

    def Add_Object(self, _Key, _Object):
         self.ObjLst[_Key].append(_Object)

    def Remove_Object(self, _Key, Index):
         self.ObjLst[_Key].remove(Index)

