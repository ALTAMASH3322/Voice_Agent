"""
Simple Chat Example
A basic example of using the Voice Agent for a simple conversation.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SimpleVoiceAgent:
    """A simple voice agent implementation for demonstration purposes."""
    
    def __init__(self, language="en-US"):
        self.language = language
        self.conversation_history = []
        print(f"🤖 Voice Agent initialized with language: {language}")
    
    def listen(self):
        """Simulate listening to user input."""
        print("\n🎤 Listening... (speak now)")
        # In a real implementation, this would use speech recognition
        user_input = input("You: ")
        return user_input
    
    def process(self, text):
        """Process the input text and generate a response."""
        self.conversation_history.append({"role": "user", "content": text})
        
        # Simulate LLM processing
        response = f"I heard you say: '{text}'. How can I help you with that?"
        
        self.conversation_history.append({"role": "assistant", "content": response})
        return response
    
    def speak(self, text):
        """Convert text to speech and play it."""
        print(f"🔊 Agent: {text}")
        # In a real implementation, this would use TTS and audio playback
    
    def run(self):
        """Run the main conversation loop."""
        print("\n" + "="*50)
        print("🎙️  Voice Agent Started")
        print("="*50)
        print("Say 'exit' or 'quit' to end the conversation.\n")
        
        while True:
            try:
                # Listen for user input
                user_input = self.listen()
                
                # Check for exit command
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\n👋 Goodbye! Thanks for chatting.")
                    break
                
                # Process and respond
                response = self.process(user_input)
                self.speak(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Conversation ended by user.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again.")


def main():
    """Main function to run the simple chat example."""
    # Create and run the voice agent
    agent = SimpleVoiceAgent(language="en-US")
    agent.run()


if __name__ == "__main__":
    main()
