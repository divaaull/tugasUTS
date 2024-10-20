from fastapi import FastAPI

app = FastAPI()

@app.get("/mahasiswa")
def read_mahasiswa(nama: str, tahun_join: int):
    return {"message": f"{nama} adalah mahasiswa TI Unpam saya masuk tahun {tahun_join}."}