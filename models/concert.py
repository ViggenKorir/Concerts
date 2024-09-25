from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database_setup import Base

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
