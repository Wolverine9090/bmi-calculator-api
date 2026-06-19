# BMI Calculator API

A REST API built with FastAPI that calculates Body Mass Index (BMI) and returns the health category.

## Tech Stack
- Python
- FastAPI
- Pydantic

## How to Run Locally

1. Clone the repository
git clone https://github.com/Wolverine9090/bmi-calculator-api.git

2. Install dependencies
pip install fastapi uvicorn

3. Run the server
uvicorn bmi:app --reload

4. Open in browser
http://127.0.0.1:8000/docs

## API Endpoint

### POST /bmi

**Input:**
```json
{
    "first_name": "Satyaki",
    "last_name": "Patra",
    "weight_kg": 70,
    "height_m": 1.75
}
```

**Output:**
```json
{
    "Name": "Satyaki Patra",
    "bmi": 22.86,
    "bmi_Category": "Normal"
}
```

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25 - 29.9 | Overweight |
| 30 and above | Obese |

## Author
Satyaki Ranjan Patra
