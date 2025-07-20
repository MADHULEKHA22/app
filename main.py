from voice_emotion import detect_emotion
from gemini_assistant import talk_with_ayush
from translator import translate_and_speak
from communicator import handle_command, speak
from voice_handler import record_and_recognize
import time

def run_ayush():
    speak("Hi, I am AYUSH. What may I help you today?")
    time.sleep(0.5)  # small pause after greeting

    while True:
        # Give user some time to prepare to speak
        print("🎙️ Ready to listen in 3 seconds...")
        time.sleep(3)

        command = record_and_recognize()
        if command is None:
            speak("I couldn't hear you clearly. Please try again.")
            continue

        command = command.lower()
        print(f"💬 You said: {command}")

        if any(word in command for word in ["sad", "depressed", "anxious", "lonely", "angry", "unhappy", "crying", "low", "bad", "down", "miserable"]):
            emotion_feedback = detect_emotion("Madhulekha")
            speak(emotion_feedback)
            speak("I'm here for you. Would you like to talk about it?")
            
            time.sleep(1)  # pause before listening again
            response = record_and_recognize()
            if response:
                reply = talk_with_ayush(response)
                speak(reply)
            continue

        elif any(word in command for word in ["talk", "chat", "friend", "conversation", "help me", "i need help"]):
            reply = talk_with_ayush(command)
            speak(reply)

        elif "translate" in command:
            speak("Please say the sentence you want to translate.")
            time.sleep(1)
            text = record_and_recognize()
            if text:
                speak("Which language to translate to?")
                time.sleep(1)
                lang = record_and_recognize()
                if lang:
                    translate_and_speak(text, lang)
                else:
                    speak("I didn't catch the language. Please try again later.")
            else:
                speak("I didn't catch the sentence to translate.")

        elif "open" in command or "website" in command or "play" in command:
            result = handle_command(command)
            if result:
                speak(result)

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! AYUSH is always here for you.")
            break

        else:
            reply = talk_with_ayush(command)
            speak(reply)

if __name__ == "__main__":
    run_ayush()
