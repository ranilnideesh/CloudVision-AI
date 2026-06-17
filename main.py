from fastapi import FastAPI
from pydantic import BaseModel
import math
app=FastAPI(title='UrbanCool AI Pro API')
class HeatRequest(BaseModel): lat:float; lon:float; apparent_temp:float=35; density:float=0.5
@app.get('/health')
def health(): return {'status':'ok','service':'UrbanCool AI Pro'}
@app.post('/api/heat-score')
def heat(req:HeatRequest):
    base=req.apparent_temp+6+(3 if abs(req.lat)<30 else 0)
    built=max(0,min(1,req.density)); veg=1-built
    lst=base+built*5.2-veg*2.8
    risk=round(max(0,min(100,(lst-30)*6+built*18)))
    return {'risk':risk,'estimated_lst_c':round(lst,1),'classification':'modelled','note':'Use measured LST upload for operational analysis.'}
