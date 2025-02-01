import os
import yaml
from fastapi import FastAPI
from utils.constellation import Constellation
from utils.search import SearchUtils
from pydantic import BaseModel

DATA_DIR = "data/sample.yml"

app = FastAPI()

class SearchRequest(BaseModel):
	name: str

sky = {}
with open(DATA_DIR) as f:
	yml = yaml.safe_load(f)

for name in yml:
	con = Constellation(name, yml[name])
	sky[name] = con

@app.get("/")
async def root():
    return "<h1>gay<h1>"

@app.post("/search_const")
async def search(req: SearchRequest):
	return SearchUtils.search(sky, req.name)


