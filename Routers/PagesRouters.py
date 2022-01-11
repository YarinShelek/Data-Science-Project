from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from Consts import Consts, Player
import pandas as pd
from MachineLearning import ml
import MLUtility as util

router = APIRouter()


@router.get("/DataSource", response_class=HTMLResponse)
def DataSource(request: Request):
    with open(Consts.All_Data_File, "r") as file:
        df = pd.read_csv(file)
        df=df.dropna()
    return Consts.templates.TemplateResponse("DataSource.html", {"request": request, "Title": "DataSource Page", "df": [df.to_html(index=False,classes="table table-bordered table-dark", justify="justify-all")]})
@router.get("/DataCleaning", response_class=HTMLResponse)
def DataCleaning(request: Request):
    with open(Consts.Clean_Data_File, "r") as file:
        df = pd.read_csv(file)
    df=df.dropna()
    return Consts.templates.TemplateResponse("DataCleaning.html", {"request": request, "Title": "DataCleaning Page", "df": [df.to_html(index=False,classes="table table-bordered table-dark", justify="justify-all")]})
@router.get("/EDA", response_class=HTMLResponse)
def EDA(request: Request):
    return Consts.templates.TemplateResponse("EDA.html", {"request": request, "Title": "EDA Page"})
@router.get("/EDA_Corr", response_class=HTMLResponse)
def EDA(request: Request):
    return Consts.templates.TemplateResponse("EDA_Corr.html", {"request": request, "Title": "EDA Page"})
@router.get("/EDA_Damage_Gold", response_class=HTMLResponse)
def EDA(request: Request):
    return Consts.templates.TemplateResponse("EDA_Damage_Gold.html", {"request": request, "Title": "EDA Page"})
@router.get("/MachineLearning", response_class=HTMLResponse)
def MachineLearning(request: Request):
    return Consts.templates.TemplateResponse("MachineLearning.html", {"request": request, "Title": "MachineLearning Page", "Data": ml(False), "DataMap": Consts.ml_replace_map})
@router.post("/RankGuess", response_class=HTMLResponse)
def RankGuess(request: Request, FormData: Player = Depends(Player.read_form)):
    return Consts.templates.TemplateResponse("RankGuess.html", {"request": request, "Title": "RankGuess Page", "Rank": util.predict_player_rank(FormData.to_list())})