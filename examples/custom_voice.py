"""
Custom Voice Example
Demonstrates how to use custom voice profiles with the Voice Agent.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class VoiceProfile:
    """Represents a voice profile with specific characteristics."""
    
    def __init__(self, name, voice_id, speed=1.0, pitch=1.0, personality=None):
        self.name = name
        self.voice_id = voice_id
        self.speed = speed
        self.pitch = pitch
        self.personality = personality or "friendly"
    
    def __repr__(self):
        return f"VoiceProfile(name='{self.name}', personality='{self.personality}')"


class CustomVoiceAgent:
    """Voice agent with custom voice profile support."""
    
    # Predefined voice profiles
    VOICE_PROFILES = {
        "professional": VoiceProfile(
            name="Professional",
            voice_id="prof_001",
            speed=1.0,
            pitch=1.0,
            personality="professional and courteous"
        ),
        "friendly": VoiceProfile(
            name="Friendly",
            voice_id="friend_001",
            speed=1.1,
            pitch=1.05,
            personality="warm and friendly"
        ),
        "energetic": VoiceProfile(
            name="Energetic",
            voice_id="energy_001",
            speed=1.2,
            pitch=1.1,
            personality="enthusiastic and energetic"
        ),
        "calm": VoiceProfile(
            name="Calm",
            voice_id="calm_001",
            speed=0.9,
            pitch=0.95,
            personality="calm and soothing"
        )
    }
    
    def __init__(self, voice_profile="friendly"):
        if voice_profile not in self.VOICE_PROFILES:
            raise ValueError(f"Unknown voice profile: {voice_profile}")
        
        self.voice_profile = self.VOICE_PROFILES[voice_profile]
        print(f"🎭 Voice Agent initialized with profile: {self.voice_profile}")
    
    def change_voice(self, profile_name):
        """Change the current voice profile."""
        if profile_name not in self.VOICE_PROFILES:
            print(f"❌ Unknown profile: {profile_name}")
            print(f"Available profiles: {', '.join(self.VOICE_PROFILES.keys())}")
            return False
        
        self.voice_profile = self.VOICE_PROFILES[profile_name]
        print(f"✅ Voice changed to: {self.voice_profile.name}")
        return True
    
    def speak(self, text):
        """Speak with the current voice profile."""
        print(f"\n🔊 [{self.voice_profile.name}] Agent: {text}")
        print(f"   (Speed: {self.voice_profile.speed}x, Pitch: {self.voice_profile.pitch}x)")
    
    def demonstrate_voices(self):
        """Demonstrate all available voice profiles."""
        demo_text = "Hello! This is how I sound with this voice profile."
        
        print("\n" + "="*60)
        print("🎭 Voice Profile Demonstration")
        print("="*60)
        
        for profile_name, profile in self.VOICE_PROFILES.items():
            print(f"\n--- {profile.name} Voice ---")
            print(f"Personality: {profile.personality}")
            self.change_voice(profile_name)
            self.speak(demo_text)
        
        print("\n" + "="*60)


def main():
    """Main function to demonstrate custom voices."""
    print("🎙️ Custom Voice Agent Demo\n")
    
    # Create agent with default voice
    agent = CustomVoiceAgent(voice_profile="friendly")
    
    # Demonstrate all voice profiles
    agent.demonstrate_voices()
    
    # Interactive voice selection
    print("\n\n📝 Interactive Mode")
    print("Available voice profiles:")
    for profile_name in CustomVoiceAgent.VOICE_PROFILES.keys():
        print(f"  - {profile_name}")
    
    print("\nType a profile name to change voice, or 'exit' to quit.")
    
    while True:
        choice = input("\nSelect voice profile: ").strip().lower()
        
        if choice in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        
        if agent.change_voice(choice):
            test_text = input("Enter text for the agent to say: ")
            agent.speak(test_text)


if __name__ == "__main__":
    main()
