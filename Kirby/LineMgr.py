import Struct
import main_state
import Knight


class CLineMgr :
    def __init__(self):
       self.LineLst = [Struct.CLinePos(-60, 120, 520, 120, 0), Struct.CLinePos(520, 230, 906, 230, 0),
                        Struct.CLinePos(906,280,1146,280,0),Struct.CLinePos(1146,230,1576,230,0),
                        Struct.CLinePos(1576,310,1966,310,0),Struct.CLinePos(1966,230,2243,230,0),
                        Struct.CLinePos(2243,360,2473,360,0),Struct.CLinePos(2473,230,2656,230,0),
                        Struct.CLinePos(2656,310,4000,310,0)]
       self.stage = 0

    def LineChange(self):
        self.LineLst =[Struct.CLinePos(-60, 120, 5000, 120, 0)]
        self.stage = 1
        Boss = Knight.CKnight()
        main_state.m_ObjectMgr.Add_Object('BOSS', Boss)



