from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# Database connection string (update as needed)
DATABASE_URL = 'sqlite:///concerts.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    import models.band
    import models.venue
    import models.concert
    Base.metadata.create_all(engine)
