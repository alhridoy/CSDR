import requests
import json

BASE_URL = 'http://localhost:5000'

def test_auth_system():
    # Test registration
    print('Testing registration...')
    response = requests.post(f'{BASE_URL}/register', 
                           json={'username': 'testuser', 'password': 'testpass'})
    print(f'Register: {response.status_code} - {response.json()}')
    
    # Test login
    print('Testing login...')
    session = requests.Session()
    response = session.post(f'{BASE_URL}/login', 
                          json={'username': 'testuser', 'password': 'testpass'})
    print(f'Login: {response.status_code} - {response.json()}')
    
    # Test protected route
    print('Testing protected route...')
    response = session.get(f'{BASE_URL}/profile')
    print(f'Profile: {response.status_code} - {response.json()}')
    
    # Test logout
    print('Testing logout...')
    response = session.post(f'{BASE_URL}/logout')
    print(f'Logout: {response.status_code} - {response.json()}')

if __name__ == '__main__':
    test_auth_system()