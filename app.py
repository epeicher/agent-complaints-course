from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from models import Complaint, complaints

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/complaints")
async def complaints_board(request: Request):
    return templates.TemplateResponse(request, "complaints.html", {"complaints": complaints})

@app.post("/complaints")
async def create_complaint(agent_name: str = Form(..., min_length=1), text: str = Form(..., min_length=1)):
    new_complaint = Complaint(agent_name=agent_name, text=text)
    complaints.append(new_complaint)
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/complaints", status_code=303)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)