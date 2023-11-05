import uvicorn

from fastapi import (
    Depends, 
    FastAPI, 
    Path, 
    Query, 
    Response, 
    status)
from fastapi.middleware.cors import CORSMiddleware
import copy
from pydantic import BaseModel
from app.services import api
from sqlalchemy.orm import Session
from sqlalchemy.exc import InterfaceError
from app.db.database import SessionLocal, engine, get_db
from app.db import db_service, model, schemas

from typing import Annotated

from app.common.dto import ItemTabellone, Collega

from app.caffelog import Caffelog
log = Caffelog().log


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tabellone")
async def get_tabellone(response: Response, db: Session = Depends(get_db)):    
    try:
        list = []
        colleghi = db_service.get_tabellone(db)
        for c in colleghi:
            item = ItemTabellone(id=c.id, nome=c.nome, cognome=c.cognome, totals=(c.totals if c.totals is not None else 0))
            list.append(item)

    except InterfaceError as ex:
        log.error("DB connection error",ex)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'message': 'Db connection error',"intern_error":ex}  
    return list
    
@app.get("/collega/status/{user_id}")
async def get_collega_status(response: Response,  user_id : int,   db: Session = Depends(get_db)):    
    try:
        
        colleghi = db_service.get_collega_status(user_id, db)
        if len(colleghi) == 1:
            c = colleghi[0]
            item = ItemTabellone(id=c.id, nome=c.nome, cognome=c.cognome, totals=(c.totals if c.totals is not None else 0))
            return item
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {}

    except InterfaceError as ex:
        log.error("DB connection error",ex)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'message': 'Db connection error',"intern_error":ex}  



def helper_caffe_io (
    response: Response,
    user_id : int,    
    db: Session,
    func,
    qty: Annotated [int | None, Query()] = None):
    if db_service.exist_user_id(user_id, db):
        try:
            func()
            return {'message': 'ok'}  
        except InterfaceError as ex:
            log.error("DB connection error",ex)
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'message': 'Db connection error',"intern_error":ex}
        except Exception as err:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            log.error("Generic error",err)
            return {'message': 'Errore interno',"intern_error":err}  

    response.status_code = status.HTTP_404_NOT_FOUND
    return {'message': 'Collega not found'}   



@app.post("/add/caffe/{user_id}/")
async def add_caffe(
    response: Response,
    user_id : Annotated[int, Path(title="The ID of user")],
    qty: Annotated [int | None, Query()],
    db: Session = Depends(get_db)):
    
    def increse():
        db_service.add_caffe(user_id, qty, db)
        log.info("Ordine inserito con successo")
    return helper_caffe_io(response,user_id,db,increse,qty)

  
    

@app.post("/drink/caffe/{user_id}")
async def bevo_caffe(
    response: Response,
    user_id : Annotated[int, Path(title="The ID of user")],
    db: Session = Depends(get_db)):
    
    def decrese():
        db_service.decrese_caffe(user_id, db)
        log.info("Caffe bevuto")
    return helper_caffe_io(response,user_id,db,decrese)



@app.post("/add/collega/")
async def add_caffe(
    collega: Collega,
    response: Response,
    db: Session = Depends(get_db)):
    try:
        db_service.add_collega(collega, db)
        return {'message': 'ok'}  
    except InterfaceError as ex:
        log.error("DB connection error",ex)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'message': 'Db connection error',"intern_error":ex}
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        log.error("Generic error",err)
        return {'message': 'Errore interno',"intern_error":err}  


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8000)