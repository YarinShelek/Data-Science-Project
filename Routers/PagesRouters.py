from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from Consts import Consts

router = APIRouter()


@router.get("/DataSource", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("DataSource.html", {"request": request, "Title": "DataSource Page"})
@router.get("/OriginalData", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("OriginalData.html", {"request": request, "Title": "OriginalData Page"})
@router.get("/EDA", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("EDA.html", {"request": request, "Title": "EDA Page"})
@router.get("/MachineLearning", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("MachineLearning.html", {"request": request, "Title": "MachineLearning Page"})

