import os
import yaml
from fastapi import FastAPI
from utils.constellation import Constellation
from utils.search import SearchUtils
from pydantic import BaseModel

DATA_DIR = "data/"

app = FastAPI()

class SearchRequest(BaseModel):
	name: str

sky = []
for fname in os.listdir(DATA_DIR):
	with open(DATA_DIR+fname) as f:
		yml = yaml.safe_load(f)
		con = Constellation(fname, yml)
		sky.append(con)

@app.get("/")
async def root():
    return "<h1>gay<h1>"

@app.post("/search_const")
async def search(req: SearchRequest):
	return SearchUtils.search(sky, req.name)


