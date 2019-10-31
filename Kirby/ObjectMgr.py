import game_framework


class CObjectMgr:
    def __init__(self):
        self.ObjLst = {'MAP': [], 'MONSTER':[] ,'PLAYER': [], 'UI': []}

    def Update_Object(self):
        for index in self.ObjLst:
            count = 0
            for index2 in self.ObjLst[index]:
             n= index2.update()




    def Draw_Object(self):
        for index in self.ObjLst:
            for index2 in self.ObjLst[index]:
                index2.draw()

    def Add_Object(self, _Key, _Object):
         self.ObjLst[_Key].append(_Object)

    def Remove_Object(self, _Key, Index):
         self.ObjLst[_Key].remove(Index)

    def Get_ObjectList(self,_Key):
        return self.ObjLst[_Key]
