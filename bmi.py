from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

app = FastAPI()

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
    weight_kg : float
    height_cm : float

    @field_validator("first_name", "last_name")
    def name_validator(cls, value):
        return value.strip().lower()


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
        bmi_category = "Obese"
    return {
        "Name" : f"{details.first_name} {details.last_name}",
        "bmi" : bmi,
        "bmi_Category" : bmi_category
    }