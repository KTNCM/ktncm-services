import os
import mysql.connector
import time
from dotenv import load_dotenv
from destination import Destination
load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'db': os.getenv('DB_NAME'),
            'port': os.getenv('DB_PORT'),
            'ssl_ca': os.getenv('DB_CERTIFICATE'),
            'ssl_verify_cert': bool(os.getenv('DB_VERIFY'))
        }

    def connect(self, max_retries = 10, sleep_time = 5) -> None:
        """Connects to database using data provided in environment variables.

        Args:
            max_retries (int, optional): The maximum number of retry attempts. Defaults to 10.
        """
        retries = 0
        while retries < max_retries:
            try:
                self.connection = mysql.connector.connect(**self.db_config)
                print("Connected to the database!")
                break
            except mysql.connector.Error as err:
                print(f"Database not ready, retrying in {sleep_time} seconds... Error: {err}")
                retries += 1
                time.sleep(sleep_time)

    def insert_destinations(self, excursion_destinations: list[Destination]) -> None:
        """Inserts destinations data into database.

        Args:
            excursion_destinations (list[Destination]): List of destination objects.
        """        
        insert_query = """
        INSERT INTO destinations (name, description, contact, address, url)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        description = VALUES(description),
        contact = VALUES(contact),
        address = VALUES(address),
        url = VALUES(url);
        """

        data = [(dest.name, dest.description, "".join(dest.contact), "", dest.img) for dest in excursion_destinations]

        cursor = self.connection.cursor()
        cursor.executemany(insert_query, data)
        rows_affected = cursor.rowcount
        print(f"Rows affected: {rows_affected}")

        self.connection.commit()
