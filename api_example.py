from error_handler import error_handler, validate_json, APIError, ValidationError

# Example user schema
USER_SCHEMA = {
    'username': {'type': str, 'required': True, 'min_length': 3, 'max_length': 50},
    'email': {'type': str, 'required': True, 'min_length': 5, 'max_length': 100},
    'age': {'type': int, 'required': False}
}

@error_handler
def create_user(request_data):
    # Validate input
    if not request_data:
        raise APIError("Request body is required", 400, "MISSING_BODY")
    
    # Validate against schema
    validate_json(request_data, USER_SCHEMA)
    
    # Additional custom validation
    if '@' not in request_data['email']:
        raise ValidationError("Invalid email format", "email")
    
    if 'age' in request_data and request_data['age'] < 0:
        raise ValidationError("Age must be positive", "age")
    
    # Simulate user creation
    user_id = 12345
    return {
        "success": True,
        "data": {
            "id": user_id,
            "username": request_data['username'],
            "email": request_data['email']
        }
    }, 201

@error_handler
def get_user(user_id):
    if not user_id or not str(user_id).isdigit():
        raise ValidationError("Invalid user ID format")
    
    # Simulate user lookup
    if int(user_id) != 12345:
        raise APIError("User not found", 404, "USER_NOT_FOUND")
    
    return {
        "success": True,
        "data": {
            "id": int(user_id),
            "username": "john_doe",
            "email": "john@example.com"
        }
    }

# Example usage
if __name__ == "__main__":
    # Test valid request
    result = create_user({"username": "john_doe", "email": "john@example.com", "age": 25})
    print("Valid request:", result)
    
    # Test invalid request
    result = create_user({"username": "jo", "email": "invalid-email"})
    print("Invalid request:", result)