import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta

class AuthSystem:
    def __init__(self, db_path='auth.db'):
        self.db_path = db_path
        self.init_db()
        self.sessions = {}
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            hashed_pw = self.hash_password(password)
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                         (username, hashed_pw))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def login(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()
        
        if result and result[0] == self.hash_password(password):
            token = secrets.token_hex(16)
            self.sessions[token] = {
                'username': username,
                'expires': datetime.now() + timedelta(hours=24)
            }
            return token
        return None
    
    def logout(self, token):
        if token in self.sessions:
            del self.sessions[token]
            return True
        return False
    
    def validate_session(self, token):
        if token in self.sessions:
            if datetime.now() < self.sessions[token]['expires']:
                return self.sessions[token]['username']
            else:
                del self.sessions[token]
        return None

if __name__ == '__main__':
    auth = AuthSystem()
    
    # Demo usage
    print("Registration:", auth.register('user1', 'password123'))
    token = auth.login('user1', 'password123')
    print("Login token:", token)
    print("Session valid:", auth.validate_session(token))
    print("Logout:", auth.logout(token))