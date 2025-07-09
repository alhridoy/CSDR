import json
import os
from typing import Any, Dict, Optional

class ConfigManager:
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config: Dict[str, Any] = {}
        self.load()
    
    def load(self) -> None:
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.config = {}
        else:
            self.config = {}
    
    def save(self) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except IOError as e:
            raise Exception(f"Failed to save config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
    
    def has(self, key: str) -> bool:
        """Check if key exists"""
        return key in self.config
    
    def delete(self, key: str) -> None:
        """Delete configuration key"""
        if key in self.config:
            del self.config[key]

# Example usage
if __name__ == '__main__':
    config = ConfigManager('app_config.json')
    config.set('database_url', 'postgresql://localhost:5432/mydb')
    config.set('debug', True)
    config.save()
    
    print(f"Database URL: {config.get('database_url')}")
    print(f"Debug mode: {config.get('debug', False)}")
    print(f"API key: {config.get('api_key', 'not_set')}")