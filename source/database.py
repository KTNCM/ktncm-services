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
        INSERT INTO destinations (name, description, contact_info, img_url)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        description = VALUES(description),
        contact_info = VALUES(contact_info),
        img_url = VALUES(img_url);
        """

        data = [(dest.name, dest.description, "".join(dest.contact_info), dest.img_url) for dest in excursion_destinations]

        cursor = self.connection.cursor()
        cursor.executemany(insert_query, data)

        # MySql increments Id even on update so it needs to be corrected
        # Step 1: Calculate the next auto-increment value
        cursor.execute("SELECT MAX(id) + 1 FROM destinations")
        next_auto_increment = cursor.fetchone()[0]

        # Step 2: Dynamically construct and execute the ALTER TABLE statement if the table is not empty
        if next_auto_increment:
            alter_query = f"ALTER TABLE destinations AUTO_INCREMENT = {next_auto_increment}"
            cursor.execute(alter_query)

        self.connection.commit()
