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
@router.get("/ChallengerLogo")
def ChallengerLogo():
    return FileResponse("Images/challenger.png")

@router.get("/DiamondLogo")
def DiamondLogo():
    return FileResponse("Images/diamond.png")
