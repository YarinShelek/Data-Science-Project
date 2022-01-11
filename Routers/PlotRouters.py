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
@router.get("/Apex_Mean_Plot")
def Plot():
    return FileResponse("Plots/Apex_Mean_Plot.png")
@router.get("/Apex_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Apex_Damage_Gold_Mean.png")
##APEX

##DIAMOND
@router.get("/Diamond_Mean_Plot")
def Plot():
    return FileResponse("Plots/Diamond_Mean_Plot.png")
@router.get("/Diamond_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Diamond_Damage_Gold_Mean.png")
##DIAMOND

##PLATINUM
@router.get("/Platinum_Mean_Plot")
def Plot():
    return FileResponse("Plots/Platinum_Mean_Plot.png")
@router.get("/Platinum_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Platinum_Damage_Gold_Mean.png")
##PLATINUM

##GOLD
@router.get("/Gold_Mean_Plot")
def Plot():
    return FileResponse("Plots/Gold_Mean_Plot.png")
@router.get("/Gold_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Gold_Damage_Gold_Mean.png")
##GOLD

##SILVER
@router.get("/Silver_Mean_Plot")
def Plot():
    return FileResponse("Plots/Silver_Mean_Plot.png")
@router.get("/Silver_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Silver_Damage_Gold_Mean.png")
##SILVER

##BRONZE
@router.get("/Bronze_Mean_Plot")
def Plot():
    return FileResponse("Plots/Bronze_Mean_Plot.png")
@router.get("/Bronze_Damage_Gold_Mean")
def Plot():
    return FileResponse("Plots/Bronze_Damage_Gold_Mean.png")
##BRONZE
