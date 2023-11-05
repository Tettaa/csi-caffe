from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Colleghi(Base):
    __tablename__ = 'colleghi'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cognome = Column(String)


class Tabellone(Base):
    __tablename__ = 'tabellone'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cognome = Column(String)
    collega_id = Column(Integer)
    totals = Column(Integer)


class Ordini(Base):
     __tablename__ = "ordini"
     id = Column(Integer, primary_key=True, index=True)
     order_in = Column(Integer)
     qty = Column(Integer)
     collega_id = Column(Integer, ForeignKey("colleghi.id"))
     insert_at = Column(DateTime(timezone=True))
     #collega = relationship("Colleghi")





