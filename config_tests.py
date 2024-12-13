import sqlite3
import unittest
from unittest.mock import patch

from app import app

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()

        cursor.execute(""" 
            CREATE TABLE students (
	            ID INTEGER PRIMARY KEY,
	            name TEXT NOT NULL,
	            age INTEGER,
                grade TEXT,
                subjects TEXT
            );
        """)
        cursor.execute("""
           INSERT INTO students (name,age,grade,subjects)
           VALUES ("zara",23,"g","maths,arts");          
        """)
        self.connection.commit()

        self.db_connection_patch = patch("app.db_connection", return_value=self.connection)
        self.db_connection_patch.start()
        
        self.app = app.test_client()

    def tearDown(self):
        self.connection.close()