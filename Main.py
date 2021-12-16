from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from Routers import MiscRouters
app = FastAPI()
app.mount("/static", StaticFiles(directory="CSS"), name="static")
app.include_router(MiscRouters.router)

if __name__ == "__main__":
    uvicorn.run("Main:app", host="0.0.0.0", port=8888, reload=True)
