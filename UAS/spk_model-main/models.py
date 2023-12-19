from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Smartphone(Base):
    __tablename__ = 'smartphonesamsung'
    id = Column(Integer, primary_key=True)
    brand = Column(String(65))
    ram = Column(String(20)) 
    processor = Column(String(65))
    rom = Column(String(65))
    baterai = Column(String(30))
    harga = Column(String(20))

    def __repr__(self):
        return f"smartphonesamsug(id={self.id!r}, brand={self.brand!r}"
