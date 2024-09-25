from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database_setup import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    
    concerts = relationship('Concert', back_populates='band')

    def venues(self):
        return [concert.venue for concert in self.concerts]
