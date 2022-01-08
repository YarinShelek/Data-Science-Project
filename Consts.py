from fastapi.templating import Jinja2Templates

class Consts():
    templates = Jinja2Templates(directory="templates")
    replace_map = {"Iron": 1, "Bronze": 1, "Silver": 2, "Gold": 3, "Platinum": 4, "Diamond": 5, "Master": 6, "Grandmaster": 6, "Challenger": 6}
    replace_list = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Apex"]