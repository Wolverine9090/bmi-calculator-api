from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator, Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PersonDetail(BaseModel):
    first_name : str
    last_name : str
    weight_kg : float = Field(gt= 0, le= 500)
    height_cm : float = Field(gt= 0, le= 300)

    @field_validator("first_name", "last_name")
    def name_validator(cls, value):
        value=  value.strip().title()
        if value is None:
            return ValueError("Name Cannot be empty")
        return value


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "bmi_calculator_frontend.html",
        {"request": request}
    )



@app.post("/bmi")
def calculate_bmi(details : PersonDetail):
    height_m = details.height_cm / 100
    bmi = round(details.weight_kg / (height_m * height_m),2)
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        bmi_category = "Normal"
    elif 25 <= bmi <= 29.9:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obesity"
    return {
        "Name" : f"{details.first_name} {details.last_name}",
        "bmi" : bmi,
        "bmi_Category" : bmi_category
    }