import json
import os
from typing import Any, Dict, Optional

class ConfigManager:
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}
    
    def save_config(self) -> None:
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get config value with env var fallback"""
        return self.config.get(key, os.getenv(key, default))
    
    def set(self, key: str, value: Any) -> None:
        """Set config value"""
        self.config[key] = value
        self.save_config()
    
    def get_all(self) -> Dict[str, Any]:
        """Get all config values"""
        return self.config.copy()

if __name__ == '__main__':
    config = ConfigManager()
    config.set('database_url', 'localhost:5432')
    print(f"Database URL: {config.get('database_url')}")
    print(f"All config: {config.get_all()}")