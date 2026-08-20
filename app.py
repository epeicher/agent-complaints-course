import uvicorn
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse

from models import Complaint, complaints

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/complaints")
async def get_complaints(request: Request):
    return templates.TemplateResponse(request, "complaints.html", {"complaints": complaints})


@app.post("/complaints")
async def post_complaints(agent_name: str = Form(...), text: str = Form(...)):
    complaint = Complaint(agent_name=agent_name, text=text)
    complaints.append(complaint)
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
