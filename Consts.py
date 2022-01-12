from fastapi.templating import Jinja2Templates
from fastapi import Form
from pydantic import BaseModel

class Consts():
    templates = Jinja2Templates(directory="templates")
    replace_map = {"Bronze": 0, "Silver": 1, "Gold": 2, "Platinum": 3, "Diamond": 4, "Apex": 5}
    replace_list = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Apex"]
    Color_List = ["#CD7F32", "#C0C0C0", "#d4af37", "#E5E4E2", "#A0e1f5", "#860111"]
    ml_replace_map = {"n": 0, "f1": 1, "acc": 2}
    ##file_names
    Clean_Data_File = "CleanData.csv"
    All_Data_File = "AllData.csv"
class Player(BaseModel):
    WinRate: float
    Games: float
    Kills: float
    Deaths: float
    Assists: float
    CS: float
    Damage: float
    Gold: float
    Multi_Kills: float

    @classmethod
    def read_form(cls, WinRate: float = Form(...), Games: float = Form(...), Kills: float = Form(...), Deaths: float = Form(...), Assists: float = Form(...), CS: float = Form(...), Damage: float = Form(...), Gold: float = Form(...), Multi_Kills: float = Form(...)):
        return cls(WinRate=WinRate, Games=Games, Kills=Kills, Deaths=Deaths, Assists=Assists, CS=CS, Damage=Damage, Gold=Gold, Multi_Kills=Multi_Kills)

    def to_list(self):
        res = []
        res.append(self.WinRate)
        res.append(self.Games)
        res.append(self.Kills)
        res.append(self.Deaths)
        res.append(self.Assists)
        res.append(self.CS)
        res.append(self.Damage)
        res.append(self.Gold)
        res.append(self.Multi_Kills)
        return res