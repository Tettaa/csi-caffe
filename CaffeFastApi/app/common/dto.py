from pydantic import BaseModel

class ItemTabellone(BaseModel):
    id: int
    nome: str
    cognome: str
    totals: int


class Collega(BaseModel):
    nome: str
    cognome: str 