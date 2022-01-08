from fastapi.templating import Jinja2Templates

class Consts():
    templates = Jinja2Templates(directory="templates")
    replace_map = {"Iron": 0, "Bronze": 1, "Silver": 2, "Gold": 3, "Platinum": 4, "Diamond": 5, "Master": 6, "Grandmaster": 7, "Challenger": 8}
