# import uvicorn
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session

# from app.db import db_service, model, schemas
# from app.db.database import SessionLocal, engine, get_db

# model.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# @app.get("/colleghi")
# def get_colleghi(db: Session = Depends(get_db)):
#     colleghi = db_service.get_colleghi(db)
#     return colleghi

# @app.get("/tabellone")
# def get_tabellone(db: Session = Depends(get_db)):
#     colleghi = db_service.get_tabellone(db)
#     return colleghi


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")