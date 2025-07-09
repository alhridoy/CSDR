import sqlite3
import os
from contextlib import contextmanager

class DatabaseHelper:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.getenv('DB_PATH', 'app.db')
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def execute_query(self, query, params=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            conn.commit()
            return cursor.fetchall()
    
    def execute_single(self, query, params=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            conn.commit()
            return cursor.fetchone()

db = DatabaseHelper()