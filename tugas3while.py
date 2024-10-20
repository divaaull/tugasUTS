from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BirthDate(BaseModel):
    name: str           # nama
    birth_month: int    # bulan lahir (1-12)
    birth_year: int     # tahun lahir (YYYY)
    current_year: int   # tahun saat ini (YYYY)

@app.post("/calculate_age/")
async def calculate_age(birth_date: BirthDate):
    ages = []
    
    months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]

    month_index = 1  # mulai dari bulan 1 (januari)
    
    # menghitung umur menggunakan loop while
    while month_index <= 12:  # dari bulan 1 (januari) sampai 12 (desember)
        if month_index >= birth_date.birth_month:
            age_years = birth_date.current_year - birth_date.birth_year
            age_months = month_index - birth_date.birth_month
        else:
            age_years = birth_date.current_year - birth_date.birth_year - 1
            age_months = 12 - birth_date.birth_month + month_index

        ages.append(f"{birth_date.name} berumur {age_years} tahun {age_months} bulan pada bulan {months[month_index - 1]} {birth_date.current_year}")

        month_index += 1  
        
    return {
        "code": 200,
        "mess": "succ",
        "data": {
            "birth_date": {
                "name": birth_date.name,
                "birth_month": birth_date.birth_month,
                "birth_year": birth_date.birth_year,
                "current_year": birth_date.current_year
            },
            "ages": ages
        }
    }