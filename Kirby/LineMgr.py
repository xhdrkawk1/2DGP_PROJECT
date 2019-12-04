import Struct

class CLineMgr :
    def __init__(self):
       self.LineLst = [Struct.CLinePos(-60, 120, 520, 120, 0), Struct.CLinePos(520, 230, 906, 230, 0),
                        Struct.CLinePos(906,280,1146,280,0),Struct.CLinePos(1146,230,1576,230,0),
                        Struct.CLinePos(1576,310,1966,310,0),Struct.CLinePos(1966,230,2243,230,0),
                        Struct.CLinePos(2243,360,2473,360,0),Struct.CLinePos(2473,230,2656,230,0),
                        Struct.CLinePos(2656,310,4000,310,0)]
    def LineChange(self):
        self.LineLst =[Struct.CLinePos(-60, 120, 1230, 120, 0),Struct.CLinePos(1230, 184, 1634, 184, 0),Struct.CLinePos(1634, 120, 2254, 120, 0),Struct.CLinePos(2254, 184, 2350, 184, 0),
                       Struct.CLinePos(2350, 120, 5000, 120, 0)]

