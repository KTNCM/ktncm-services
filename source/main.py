from destination import Destination
from soup import return_soup
import threading
from database import Database

def update_info(destination):
    """Send request to a destination specific url and update the data.

    Args:
        destination (Destination): Object containing the url.
    """
    dest_soup = return_soup(destination.url)
    p = dest_soup.find('div', 'content-txt').find('p')
    destination.description = p.text
    
    h4 = dest_soup.find('div', 'kontakt-box').findAll('a')
    destination.contact_info = [i.text for i in h4]
    
url = "https://www.kaerntencard.at/sommer/en/ausflugsziele-uebersicht/"
soup = return_soup(url)

#TODO rewrite to use multithreading without GIL
def fetch_destinations():
    excursion_destinations = []
    for div in soup.find_all('div', class_='col-lg-6 col-11 align-self-center'):
        destination = Destination()
        h3 = div.find('div', class_='txt-box').find('h3')
        if(h3 == None):
            continue   
        destination.name = h3.text
        
        destination.url = div.find('a', class_='btn-std')['href']
        excursion_destinations.append(destination)
    
    threads = []
    for destination in excursion_destinations:
        thread = threading.Thread(target=update_info, args=[destination])
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return excursion_destinations

database = Database()
database.connect()
excursion_destinations = fetch_destinations()
database.insert_destinations(excursion_destinations)