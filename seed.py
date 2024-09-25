from models.band import Band
from models.venue import Venue
from models.concert import Concert
from database_setup import session, init_db

def seed_data():
    # Initialize the database
    init_db()
    
    # Create bands
    band1 = Band(name="The Rolling Stones", hometown="London")
    band2 = Band(name="The Beatles", hometown="Liverpool")

    # Create venues
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="The O2 Arena", city="London")

    # Create concerts
    concert1 = Concert(date="2024-05-01", band=band1, venue=venue1)
    concert2 = Concert(date="2024-05-10", band=band2, venue=venue2)
    
    # Add and commit
    session.add_all([band1, band2, venue1, venue2, concert1, concert2])
    session.commit()

if __name__ == '__main__':
    seed_data()
