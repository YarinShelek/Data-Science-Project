from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from Consts import Consts
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("HomePage.html", {"request": request, "Title": "Home Page"})


@router.get("/Logo")
def TinderLogo():
    return FileResponse("Images/tinder_logo.png")
