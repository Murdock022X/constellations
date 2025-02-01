from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "<h1> gay<h1>"

