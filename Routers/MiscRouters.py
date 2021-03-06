from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from Consts import Consts
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("HomePage.html", {"request": request, "Title": "Home Page"})


@router.get("/Lolgo")
def Lolgo():
    return FileResponse("Images/lolgo.png")


#ranks
@router.get("/ApexLogo")
def ApexLogo():
    return FileResponse("Images/ApexLogo.png")
@router.get("/DiamondLogo")
def DiamondLogo():
    return FileResponse("Images/DiamondLogo.png")
@router.get("/PlatinumLogo")
def PlatinumLogo():
    return FileResponse("Images/PlatinumLogo.png")
@router.get("/GoldLogo")
def GoldLogo():
    return FileResponse("Images/GoldLogo.png")
@router.get("/SilverLogo")
def SilverLogo():
    return FileResponse("Images/SilverLogo.png")
@router.get("/BronzeLogo")
def BronzeLogo():
    return FileResponse("Images/BronzeLogo.png")
@router.get("/Presentation")
def Presentation():
    return FileResponse("Presentation.pptx")
@router.get("/LolIcon")
def LolIcon():
    return FileResponse("Images/LolIcon.png")
