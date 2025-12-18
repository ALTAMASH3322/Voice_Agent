"""
Streaming Mode Example
Demonstrates real-time streaming responses for reduced latency.
"""

import time
import sys
from typing import Generator


class StreamingVoiceAgent:
    """Voice agent with streaming response capability."""
    
    def __init__(self):
        self.conversation_history = []
        print("🚀 Streaming Voice Agent initialized")
    
    def generate_response_stream(self, user_input: str) -> Generator[str, None, None]:
        """
        Generate streaming response chunks.
        In a real implementation, this would stream from the LLM API.
        """
        # Simulate a streaming response
        response = (
            f"Thank you for asking about '{user_input}'. "
            f"Let me provide you with a detailed response. "
            f"Streaming allows me to start speaking while still generating text, "
            f"which significantly reduces the perceived latency. "
            f"This creates a more natural conversation flow."
        )
        
        # Split into words and yield them one by one
        words = response.split()
        for word in words:
            yield word + " "
            time.sleep(0.05)  # Simulate processing delay
    
    def speak_streaming(self, text_stream: Generator[str, None, None]):
        """
        Speak text as it streams in.
        This would use TTS in chunks in a real implementation.
        """
        print("\n🔊 Agent: ", end="", flush=True)
        
        full_response = ""
        for chunk in text_stream:
            print(chunk, end="", flush=True)
            full_response += chunk
            # In real implementation, send chunk to TTS here
        
        print()  # New line after complete response
        return full_response
    
    def listen(self) -> str:
        """Listen for user input."""
        print("\n🎤 You: ", end="")
        return input()
    
    def process_streaming(self, user_input: str):
        """Process input and generate streaming response."""
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate and speak streaming response
        response_stream = self.generate_response_stream(user_input)
        full_response = self.speak_streaming(response_stream)
        
        # Add complete response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": full_response.strip()
        })
    
    def run_comparison_demo(self):
        """Demonstrate the difference between streaming and non-streaming."""
        print("\n" + "="*70)
        print("📊 Streaming vs Non-Streaming Comparison")
        print("="*70)
        
        test_input = "What are the benefits of voice agents?"
        
        # Non-streaming mode
        print("\n--- Non-Streaming Mode ---")
        print(f"🎤 User: {test_input}")
        print("⏳ Processing... (waiting for complete response)")
        
        response = (
            "The benefits of voice agents include hands-free operation, "
            "natural interaction, accessibility for users with disabilities, "
            "and increased efficiency in task completion."
        )
        
        # Simulate waiting for complete response
        time.sleep(2)
        print(f"🔊 Agent: {response}")
        print("⏱️  Total time: 2.0s (user waited for complete response)")
        
        # Streaming mode
        print("\n--- Streaming Mode ---")
        print(f"🎤 User: {test_input}")
        print("⚡ Streaming response...")
        
        start_time = time.time()
        stream = self.generate_response_stream(test_input)
        self.speak_streaming(stream)
        elapsed = time.time() - start_time
        
        print(f"⏱️  Total time: {elapsed:.1f}s (user heard response immediately)")
        
        print("\n💡 Key Difference:")
        print("   Non-streaming: User waits for complete response")
        print("   Streaming: User hears response as it's generated")
        print("   Result: Better user experience and perceived lower latency!")
    
    def run(self):
        """Run the streaming agent."""
        print("\n" + "="*70)
        print("🎙️  Streaming Voice Agent Started")
        print("="*70)
        print("Type your message and see the streaming response.")
        print("Commands: 'demo' for comparison, 'exit' to quit\n")
        
        while True:
            try:
                user_input = self.listen()
                
                if user_input.lower() in ['exit', 'quit']:
                    print("\n👋 Goodbye!")
                    break
                
                if user_input.lower() == 'demo':
                    self.run_comparison_demo()
                    continue
                
                self.process_streaming(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Conversation ended.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


def main():
    """Main function to run the streaming example."""
    agent = StreamingVoiceAgent()
    agent.run()


if __name__ == "__main__":
    main()
