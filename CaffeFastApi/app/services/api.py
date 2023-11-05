# import json

# def current_status():
#     with open('data/csi_caffe.json') as stream:
#         caffe = json.load(stream)
#     return caffe

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.db import db_service, model, schemas
from app.db.database import SessionLocal, engine, get_db

model.Base.metadata.create_all(bind=engine)




def get_tabellone():
    return db_service.get_colleghi(get_db())
