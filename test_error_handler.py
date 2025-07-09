import pytest
from error_handler import InputValidator, ValidationError, process_user_data

def test_string_validation():
    # Valid string
    assert InputValidator.validate_string("test") == "test"
    
    # Invalid type
    with pytest.raises(ValidationError):
        InputValidator.validate_string(123)
    
    # Too short
    with pytest.raises(ValidationError):
        InputValidator.validate_string("a", min_len=5)
    
    # Too long
    with pytest.raises(ValidationError):
        InputValidator.validate_string("very long string", max_len=5)

def test_number_validation():
    # Valid numbers
    assert InputValidator.validate_number(42) == 42.0
    assert InputValidator.validate_number(3.14) == 3.14
    
    # Invalid type
    with pytest.raises(ValidationError):
        InputValidator.validate_number("not a number")
    
    # Out of range
    with pytest.raises(ValidationError):
        InputValidator.validate_number(150, min_val=0, max_val=120)

def test_email_validation():
    # Valid email
    assert InputValidator.validate_email("test@example.com") == "test@example.com"
    
    # Invalid emails
    with pytest.raises(ValidationError):
        InputValidator.validate_email("invalid")
    
    with pytest.raises(ValidationError):
        InputValidator.validate_email("no@domain")

def test_process_user_data():
    # Valid data
    result = process_user_data("John Doe", 30, "john@example.com")
    assert result["status"] == "success"
    assert result["name"] == "John Doe"
    
    # Invalid data
    result = process_user_data("", 30, "john@example.com")
    assert "error" in result
    
    result = process_user_data("John", 150, "john@example.com")
    assert "error" in result

if __name__ == "__main__":
    test_string_validation()
    test_number_validation()
    test_email_validation()
    test_process_user_data()
    print("All tests passed!")