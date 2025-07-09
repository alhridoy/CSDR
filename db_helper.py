import sqlite3
import os
from contextlib import contextmanager
from typing import Optional, Dict, Any, List

class DatabaseHelper:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self._connection = None
    
    def connect(self) -> sqlite3.Connection:
        """Establish database connection"""
        try:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row
            return self._connection
        except sqlite3.Error as e:
            raise Exception(f"Database connection failed: {e}")
    
    def close(self):
        """Close database connection"""
        if self._connection:
            self._connection.close()
            self._connection = None
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        conn = self.connect()
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict]:
        """Execute SELECT query and return results"""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute INSERT/UPDATE/DELETE query"""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.rowcount
    
    def create_table(self, table_name: str, columns: str):
        """Create table helper"""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_update(query)

# Usage example
if __name__ == "__main__":
    db = DatabaseHelper()
    db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT, email TEXT")
    db.execute_update("INSERT INTO users (name, email) VALUES (?, ?)", ("John", "john@example.com"))
    users = db.execute_query("SELECT * FROM users")
    print(users)