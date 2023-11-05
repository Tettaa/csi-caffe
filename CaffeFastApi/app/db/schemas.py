from pydantic import BaseModel

class ColleghiBase(BaseModel):
    nome: str
    cognome: str
    

class ColleghiCreate(ColleghiBase):
    pass 

class OrdiniBase(BaseModel):
    id: int
    order_in: str
    qty: int
class OrdiniCreate(ColleghiBase):
    pass 

class Ordini(OrdiniBase):
    id: int
    collega_id: int
    class Config:
        orm_mode = True

class Colleghi(ColleghiBase):
    id: int

    class Config:
        orm_mode  = True

class Tabellone(BaseModel):
    id: int
    nome: str
    cognome: str
    collega_id: int | None
    totals: int | None
    
    class Config:
        orm_mode  = True