from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from Consts import Consts
import pandas as pd
router = APIRouter()


@router.get("/DataSource", response_class=HTMLResponse)
def HomePage(request: Request):
    with open("AllData.csv", "r") as file:
        df = pd.read_csv(file)
        df=df.dropna()
    return Consts.templates.TemplateResponse("DataSource.html", {"request": request, "Title": "DataSource Page", "df": [df.to_html(index=False,classes="table table-bordered table-dark", justify="justify-all")]})
@router.get("/DataCleaning", response_class=HTMLResponse)
def HomePage(request: Request):
    with open("AllData.csv", "r") as file:
        df = pd.read_csv(file)
    df=df.dropna()
    return Consts.templates.TemplateResponse("DataCleaning.html", {"request": request, "Title": "DataCleaning Page", "df": [df.to_html(index=False,classes="table table-bordered table-dark", justify="justify-all")]})
@router.get("/EDA", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("EDA.html", {"request": request, "Title": "EDA Page"})
@router.get("/MachineLearning", response_class=HTMLResponse)
def HomePage(request: Request):
    return Consts.templates.TemplateResponse("MachineLearning.html", {"request": request, "Title": "MachineLearning Page"})

