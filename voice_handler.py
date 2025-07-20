import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os

def record_and_recognize(username="Madhulekha"):
    try:
        print("🔴 Listening now...")
        
        # Recording configuration
        fs = 44100  # Sample rate
        duration = 4  # Duration in seconds

        # Record audio
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        # Save recording to file
        os.makedirs("recordings", exist_ok=True)
        filepath = f"recordings/{username}.wav"
        sf.write(filepath, recording, fs)
        print(f"✅ Audio saved as {filepath} for processing.")

        # Recognize speech
        recognizer = sr.Recognizer()
        with sr.AudioFile(filepath) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print(f"🗣️ You said: {text}")
            return text

    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; check your internet. {e}")
        return None
    except Exception as e:
        print(f"⚠️ Error: {str(e)}")
        return None
