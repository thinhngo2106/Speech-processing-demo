from fastapi import FastAPI, Form, Request
from starlette.responses import HTMLResponse
import router_audio
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    # This is the frontend port - 3000
    "http://localhost:3000",
    "localhost:3000"
]

# Allow communication between backend and frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# templates = Jinja2Templates(directory="htmlTemplate")
#
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/home", response_class=HTMLResponse)
# async def write_home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})



app.include_router(router_audio.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)