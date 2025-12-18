"""
Multi-Language Example
Demonstrates multilingual support in the Voice Agent.
"""

import time
from typing import Dict, List


class MultiLanguageVoiceAgent:
    """Voice agent with multi-language support."""
    
    # Supported languages and their configurations
    SUPPORTED_LANGUAGES = {
        "en": {
            "name": "English",
            "code": "en-US",
            "greeting": "Hello! How can I help you today?",
            "goodbye": "Goodbye! Have a great day!",
            "voice_id": "en_voice_001"
        },
        "es": {
            "name": "Spanish",
            "code": "es-ES",
            "greeting": "¡Hola! ¿Cómo puedo ayudarte hoy?",
            "goodbye": "¡Adiós! ¡Que tengas un gran día!",
            "voice_id": "es_voice_001"
        },
        "fr": {
            "name": "French",
            "code": "fr-FR",
            "greeting": "Bonjour! Comment puis-je vous aider aujourd'hui?",
            "goodbye": "Au revoir! Passez une excellente journée!",
            "voice_id": "fr_voice_001"
        },
        "de": {
            "name": "German",
            "code": "de-DE",
            "greeting": "Hallo! Wie kann ich Ihnen heute helfen?",
            "goodbye": "Auf Wiedersehen! Haben Sie einen schönen Tag!",
            "voice_id": "de_voice_001"
        },
        "zh": {
            "name": "Chinese",
            "code": "zh-CN",
            "greeting": "你好！今天我能帮你什么？",
            "goodbye": "再见！祝你有美好的一天！",
            "voice_id": "zh_voice_001"
        },
        "ja": {
            "name": "Japanese",
            "code": "ja-JP",
            "greeting": "こんにちは！今日はどうすればお手伝いできますか？",
            "goodbye": "さようなら！良い一日を！",
            "voice_id": "ja_voice_001"
        },
        "hi": {
            "name": "Hindi",
            "code": "hi-IN",
            "greeting": "नमस्ते! आज मैं आपकी कैसे मदद कर सकता हूं?",
            "goodbye": "अलविदा! आपका दिन शुभ हो!",
            "voice_id": "hi_voice_001"
        },
        "ar": {
            "name": "Arabic",
            "code": "ar-SA",
            "greeting": "مرحبا! كيف يمكنني مساعدتك اليوم؟",
            "goodbye": "وداعا! أتمنى لك يوما سعيدا!",
            "voice_id": "ar_voice_001"
        }
    }
    
    def __init__(self, default_language="en"):
        if default_language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {default_language}")
        
        self.current_language = default_language
        self.conversation_history = []
        print(f"🌍 Multi-language Voice Agent initialized")
        print(f"   Current language: {self.SUPPORTED_LANGUAGES[default_language]['name']}")
    
    def get_current_language_info(self) -> Dict:
        """Get information about the current language."""
        return self.SUPPORTED_LANGUAGES[self.current_language]
    
    def change_language(self, language_code: str) -> bool:
        """Change the current language."""
        if language_code not in self.SUPPORTED_LANGUAGES:
            print(f"❌ Unsupported language: {language_code}")
            return False
        
        self.current_language = language_code
        lang_info = self.SUPPORTED_LANGUAGES[language_code]
        print(f"✅ Language changed to: {lang_info['name']} ({lang_info['code']})")
        return True
    
    def list_supported_languages(self):
        """Display all supported languages."""
        print("\n" + "="*60)
        print("🌍 Supported Languages")
        print("="*60)
        
        for code, info in self.SUPPORTED_LANGUAGES.items():
            current = "👉 " if code == self.current_language else "   "
            print(f"{current}{code}: {info['name']} ({info['code']})")
        
        print("="*60)
    
    def speak(self, text: str):
        """Speak in the current language."""
        lang_info = self.get_current_language_info()
        print(f"\n🔊 [{lang_info['name']}] Agent: {text}")
    
    def greet(self):
        """Greet the user in the current language."""
        lang_info = self.get_current_language_info()
        self.speak(lang_info['greeting'])
    
    def say_goodbye(self):
        """Say goodbye in the current language."""
        lang_info = self.get_current_language_info()
        self.speak(lang_info['goodbye'])
    
    def demonstrate_languages(self):
        """Demonstrate greetings in all supported languages."""
        print("\n" + "="*60)
        print("🗣️  Greeting Demonstration in All Languages")
        print("="*60)
        
        original_language = self.current_language
        
        for lang_code in self.SUPPORTED_LANGUAGES.keys():
            self.change_language(lang_code)
            self.greet()
            time.sleep(0.3)
        
        # Restore original language
        self.change_language(original_language)
        print("\n" + "="*60)
    
    def translate_demo(self):
        """Demonstrate translation capabilities."""
        print("\n" + "="*60)
        print("🔄 Translation Demo")
        print("="*60)
        
        phrases = {
            "en": "Thank you for using the voice agent!",
            "es": "¡Gracias por usar el agente de voz!",
            "fr": "Merci d'utiliser l'agent vocal!",
            "de": "Vielen Dank für die Nutzung des Sprachagenten!",
            "zh": "感谢您使用语音代理！",
            "ja": "音声エージェントをご利用いただきありがとうございます！"
        }
        
        print("\n💬 Same message in different languages:")
        for lang_code, phrase in phrases.items():
            self.change_language(lang_code)
            self.speak(phrase)
    
    def run(self):
        """Run the multi-language agent."""
        print("\n" + "="*60)
        print("🎙️  Multi-Language Voice Agent Started")
        print("="*60)
        
        self.greet()
        
        print("\nCommands:")
        print("  'list' - Show supported languages")
        print("  'demo' - Demonstrate all languages")
        print("  'translate' - Translation demo")
        print("  'lang <code>' - Change language (e.g., 'lang es')")
        print("  'exit' - Quit")
        
        while True:
            try:
                user_input = input("\n🎤 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    self.say_goodbye()
                    break
                
                if user_input.lower() == 'list':
                    self.list_supported_languages()
                    continue
                
                if user_input.lower() == 'demo':
                    self.demonstrate_languages()
                    continue
                
                if user_input.lower() == 'translate':
                    self.translate_demo()
                    continue
                
                if user_input.lower().startswith('lang '):
                    lang_code = user_input.split()[1]
                    if self.change_language(lang_code):
                        self.greet()
                    continue
                
                # Process normal input
                response = f"You said: '{user_input}'"
                self.speak(response)
                
            except KeyboardInterrupt:
                print("\n")
                self.say_goodbye()
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


def main():
    """Main function to run the multi-language example."""
    agent = MultiLanguageVoiceAgent(default_language="en")
    agent.run()


if __name__ == "__main__":
    main()
