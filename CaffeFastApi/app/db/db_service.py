from sqlalchemy.orm import Session
from app.db import model, schemas
from fastapi import Depends
from app.db.database import get_db

from datetime import datetime

from app.common.dto import ItemTabellone, Collega

from app.caffelog import Caffelog
log = Caffelog().log


def get_colleghi(db: Session):
    x = db.query(model.Colleghi).all()
    return x

def get_tabellone(db: Session):
    x = db.query(model.Tabellone).all()
    return x

def get_collega_status(user_id, db: Session):
    x = db.query(model.Tabellone).filter(model.Tabellone.id == user_id).all()
    return x


def exist_user_id(user_id, db: Session):
    return db.query(model.Colleghi).filter(model.Colleghi.id == user_id).scalar() != None    

def add_caffe(user_id: int, qty: int, db: Session):    
    try:
        o = model.Ordini(collega_id = user_id, order_in = 1, qty = qty)
        o.insert_at = datetime.now()
        db.add(o)
        db.commit()
    finally:
        db.close()


def add_collega(collega_new: Collega, db: Session):    
    try:
        o = model.Colleghi(nome=collega_new.nome, cognome=collega_new.cognome)        
        db.add(o)
        db.commit()
    finally:
        db.close()

def decrese_caffe(user_id: int, db: Session):    
    try:
        o = model.Ordini(collega_id = user_id, order_in = 0, qty = -1)
        o.insert_at = datetime.now()
        db.add(o)
        db.commit()
    finally:
        db.close()

