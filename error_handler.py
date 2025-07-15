from functools import wraps
import json
from typing import Dict, Any

class APIError(Exception):
    def __init__(self, message: str, status_code: int = 400, error_code: str = None):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(self.message)

class ValidationError(APIError):
    def __init__(self, message: str, field: str = None):
        super().__init__(message, 422, "VALIDATION_ERROR")
        self.field = field

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return {
                "error": {
                    "message": e.message,
                    "code": e.error_code,
                    "field": e.field
                }
            }, e.status_code
        except APIError as e:
            return {
                "error": {
                    "message": e.message,
                    "code": e.error_code
                }
            }, e.status_code
        except Exception as e:
            return {
                "error": {
                    "message": "Internal server error",
                    "code": "INTERNAL_ERROR"
                }
            }, 500
    return wrapper

def validate_json(data: Dict[str, Any], schema: Dict[str, Any]):
    for field, rules in schema.items():
        if rules.get('required', False) and field not in data:
            raise ValidationError(f"Field '{field}' is required", field)
        
        if field in data:
            value = data[field]
            field_type = rules.get('type')
            
            if field_type and not isinstance(value, field_type):
                raise ValidationError(f"Field '{field}' must be of type {field_type.__name__}", field)
            
            if 'min_length' in rules and len(str(value)) < rules['min_length']:
                raise ValidationError(f"Field '{field}' must be at least {rules['min_length']} characters", field)
            
            if 'max_length' in rules and len(str(value)) > rules['max_length']:
                raise ValidationError(f"Field '{field}' must not exceed {rules['max_length']} characters", field)