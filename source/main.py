from database import Database
from destinations_service import fetch_destinations

database = Database()
database.connect()
excursion_destinations = fetch_destinations()
database.insert_destinations(excursion_destinations)