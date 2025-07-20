import soundfile as sf
import numpy as np
import librosa
import os

def detect_emotion(username="Madhulekha"):
    try:
        file_path = f"recordings/{username}.wav"
        if not os.path.exists(file_path):
            return f"❌ No recorded voice found for {username}."

        # Load the audio
        y, sr = librosa.load(file_path, sr=None)
        if len(y) == 0:
            return f"❌ The recording seems to be empty."

        # Extract MFCC features
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        avg_mfcc = np.mean(mfcc, axis=1)

        # Very simple rule-based emotion classifier
        if avg_mfcc[0] < -200:
            emotion = "sad"
        elif avg_mfcc[0] > 100:
            emotion = "happy"
        else:
            emotion = "neutral"

        # Return appropriate emotional message
        if emotion == "sad":
            return f"😢 It sounds like you're feeling sad. I'm here for you, {username}. You're not alone. ❤️"
        elif emotion == "happy":
            return f"😊 You sound happy today! That’s wonderful, {username}!"
        else:
            return f"😌 You seem calm and neutral. I'm here if you ever want to talk, {username}."

    except Exception as e:
        return f"⚠️ Error during emotion detection: {str(e)}"
