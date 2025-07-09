import functools
import logging
from typing import Any, Callable, Dict, List, Optional

class ValidationError(Exception):
    """Custom validation error"""
    pass

class InputValidator:
    @staticmethod
    def validate_string(value: Any, min_len: int = 0, max_len: int = 1000) -> str:
        if not isinstance(value, str):
            raise ValidationError(f"Expected string, got {type(value).__name__}")
        if len(value) < min_len:
            raise ValidationError(f"String too short: {len(value)} < {min_len}")
        if len(value) > max_len:
            raise ValidationError(f"String too long: {len(value)} > {max_len}")
        return value
    
    @staticmethod
    def validate_number(value: Any, min_val: float = float('-inf'), max_val: float = float('inf')) -> float:
        if not isinstance(value, (int, float)):
            raise ValidationError(f"Expected number, got {type(value).__name__}")
        if value < min_val or value > max_val:
            raise ValidationError(f"Number {value} not in range [{min_val}, {max_val}]")
        return float(value)
    
    @staticmethod
    def validate_email(email: str) -> str:
        email = InputValidator.validate_string(email, min_len=5)
        if '@' not in email or '.' not in email:
            raise ValidationError("Invalid email format")
        return email

def error_handler(logger: Optional[logging.Logger] = None):
    """Decorator for comprehensive error handling"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValidationError as e:
                if logger:
                    logger.error(f"Validation error in {func.__name__}: {e}")
                return {"error": "Validation failed", "message": str(e)}
            except Exception as e:
                if logger:
                    logger.error(f"Unexpected error in {func.__name__}: {e}")
                return {"error": "Internal error", "message": "Something went wrong"}
        return wrapper
    return decorator

# Usage example
logger = logging.getLogger(__name__)

@error_handler(logger)
def process_user_data(name: str, age: int, email: str) -> Dict[str, Any]:
    name = InputValidator.validate_string(name, min_len=2, max_len=50)
    age = InputValidator.validate_number(age, min_val=0, max_val=120)
    email = InputValidator.validate_email(email)
    
    return {"name": name, "age": age, "email": email, "status": "success"}