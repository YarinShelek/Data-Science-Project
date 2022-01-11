from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()
@router.get("/PlotBeforeClean")
def PlotBeforeClean():
    return FileResponse("Plots/Plot_Before_Cleaning.png")
@router.get("/PlotAfterClean")
def PlotAfterClean():
    return FileResponse("Plots/Plot_After_Cleaning.png")

##
#EDA

##APEX
@router.get("/Apex_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Apex_Damage_Gold_Mean.png")
@router.get("/Apex_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Apex_Damage_Gold_Mean.png")
##APEX

##DIAMOND
@router.get("/Diamond_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Diamond_Damage_Gold_Mean.png")
@router.get("/Diamond_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Diamond_Damage_Gold_Mean.png")
##DIAMOND

##PLATINUM
@router.get("/Platinum_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Platinum_Damage_Gold_Mean.png")
@router.get("/Platinum_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Platinum_Damage_Gold_Mean.png")
##PLATINUM

##GOLD
@router.get("/Gold_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Gold_Damage_Gold_Mean.png")
@router.get("/Gold_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Gold_Damage_Gold_Mean.png")
##GOLD

##SILVER
@router.get("/Silver_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Silver_Damage_Gold_Mean.png")
@router.get("/Silver_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Silver_Damage_Gold_Mean.png")
##SILVER

##BRONZE
@router.get("/Bronze_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Bronze_Damage_Gold_Mean.png")
@router.get("/Bronze_Damage_Gold_Mean.png")
def Plot():
    return FileResponse("Bronze_Damage_Gold_Mean.png")
##BRONZE
