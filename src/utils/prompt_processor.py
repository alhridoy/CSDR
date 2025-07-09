"""
Utility functions generated for: add mimick test files
"""

import json
import time
from datetime import datetime
from typing import Dict, Any, Optional, List
from pathlib import Path

class PromptProcessor:
    """Process and analyze user prompts intelligently"""
    
    def __init__(self):
        self.processed_prompts = []
    
    def analyze_prompt(self, prompt: str) -> Dict[str, Any]:
        """Analyze the given prompt and extract actionable insights"""
        analysis = {
            "prompt": prompt,
            "timestamp": datetime.now().isoformat(),
            "keywords": self._extract_keywords(prompt),
            "intent": self._determine_intent(prompt),
            "complexity": self._assess_complexity(prompt)
        }
        
        self.processed_prompts.append(analysis)
        return analysis
    
    def _extract_keywords(self, prompt: str) -> List[str]:
        """Extract key terms from the prompt"""
        keywords = []
        for word in prompt.lower().split():
            if len(word) > 3 and word.isalpha():
                keywords.append(word)
        return keywords[:10]  # Top 10 keywords
    
    def _determine_intent(self, prompt: str) -> str:
        """Determine the primary intent of the prompt"""
        if any(word in prompt.lower() for word in ['add', 'create', 'build']):
            return 'creation'
        elif any(word in prompt.lower() for word in ['fix', 'debug', 'error']):
            return 'debugging'
        elif any(word in prompt.lower() for word in ['improve', 'optimize', 'enhance']):
            return 'optimization'
        else:
            return 'general'
    
    def _assess_complexity(self, prompt: str) -> str:
        """Assess the complexity level of the prompt"""
        word_count = len(prompt.split())
        if word_count < 5:
            return 'simple'
        elif word_count < 15:
            return 'moderate'
        else:
            return 'complex'
    
    def get_suggestions(self, prompt: str) -> List[str]:
        """Get implementation suggestions for the prompt"""
        analysis = self.analyze_prompt(prompt)
        suggestions = []
        
        if analysis['intent'] == 'creation':
            suggestions.extend([
                "Create comprehensive documentation",
                "Add proper error handling",
                "Implement logging functionality",
                "Add input validation"
            ])
        elif analysis['intent'] == 'debugging':
            suggestions.extend([
                "Add debug logging statements",
                "Implement error tracking",
                "Create test cases",
                "Add monitoring endpoints"
            ])
        
        return suggestions[:5]  # Top 5 suggestions

# Global processor instance
prompt_processor = PromptProcessor()
