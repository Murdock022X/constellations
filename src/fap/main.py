import os
import yaml
from utils.constellation import Constellation
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from utils.search import SearchUtils
import json

DATA_DIR = "data/sample.yml"

app = FastAPI()

class ConstellationRequest(BaseModel):
	constellation: str
	
class StarRequest(BaseModel):
	name: str

class SearchRequest(BaseModel):
	name: str

sky = {}
with open(DATA_DIR) as f:
	yml = yaml.safe_load(f)

for name in yml:
	con = Constellation(name, yml[name])
	sky[name] = con

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/", response_class=HTMLResponse)
@app.get("/observatory", response_class=HTMLResponse)
async def root(request: Request):
    print(sky)
    return templates.TemplateResponse(request=request, name="observatory.html")

@app.post("/get-constellation")
async def get_constellation(constellation_request: ConstellationRequest):
    constellation = constellation_request.constellation
	
    c: Constellation = sky[constellation]

    return json.dumps(c.vertices.keys(), indent=4, default=str)

@app.post("/star-info", response_class=HTMLResponse)
async def star_info(star_req: StarRequest):
	return templates.TemplateResponse(request=star_req, name="star_info.html")

@app.post("/search_const")
async def search(req: SearchRequest):
	return SearchUtils.search(sky, req.name)
