from database import Database
from destinations_service import fetch_destinations

database = Database()
database.connect()
excursion_destinations = fetch_destinations("https://www.kaerntencard.at/sommer/en/ausflugsziele-uebersicht/")
database.insert_destinations(excursion_destinations)