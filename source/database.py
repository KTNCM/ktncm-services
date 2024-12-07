import os
import mysql.connector
import time
from dotenv import load_dotenv
load_dotenv()

class Database:
    connection = None
    def connect(self):
        db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'db': os.getenv('DB_NAME'),
            'port': int(os.getenv('DB_PORT')),
        }

        while True:
            try:
                self.connection = mysql.connector.connect(**db_config)
                print("Connected to the database!")
                break
            except mysql.connector.Error as err:
                print(f"Database not ready, retrying in 5 seconds... Error: {err}")
                time.sleep(5)

    def insert_destinations(self, excursion_destinations) -> None:
        insert_query = """
        INSERT INTO destinations (name, description, contact_info)
        VALUES (%s, %s, %s);
        """

        data = []

        for dest in excursion_destinations:
            entry = (dest.name, dest.description, "".join(dest.contact_info))
            data.append(entry)

        cursor = self.connection.cursor()
        cursor.executemany(insert_query, data)
        self.connection.commit()
