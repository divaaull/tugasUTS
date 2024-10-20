from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BirthDate(BaseModel):
    name: str           # Nama
    birth_month: int    # Bulan lahir (1-12)
    birth_year: int     # Tahun lahir (YYYY)
    current_year: int   # Tahun saat ini (YYYY)

@app.post("/calculate_age/")
async def calculate_age(birth_date: BirthDate):
    ages = []
    
    # Daftar nama bulan
    months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]

    # Menghitung umur untuk bulan Januari hingga Desember
    for month in range(1, 13):  # Dari bulan 1 (Januari) sampai 12 (Desember)
        if month >= birth_date.birth_month:
            age_years = birth_date.current_year - birth_date.birth_year
            age_months = month - birth_date.birth_month
        else:
            age_years = birth_date.current_year - birth_date.birth_year - 1
            age_months = 12 - birth_date.birth_month + month

        # Mengubah format respons sesuai permintaan
        ages.append(f"{birth_date.name} berumur {age_years} tahun {age_months} bulan pada bulan {months[month - 1]} {birth_date.current_year}")

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