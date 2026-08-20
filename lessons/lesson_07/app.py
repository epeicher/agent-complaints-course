from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse, JSONResponse

from models import complaints, Complaint

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/complaints")
async def list_complaints(request: Request):
    return templates.TemplateResponse(
        "complaints.html", {"request": request, "complaints": complaints}
    )


@app.post("/complaints")
async def add_complaint(agent_name: str = Form(...), text: str = Form(...)):
    if not agent_name or not agent_name.strip():
        return JSONResponse({"error": "Agent name is required"}, status_code=422)
    if not text or not text.strip():
        return JSONResponse({"error": "Complaint text is required"}, status_code=422)
    complaint = Complaint(agent_name=agent_name.strip(), text=text.strip())
    complaints.append(complaint)
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)