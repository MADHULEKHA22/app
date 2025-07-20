import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record_audio(filename="test.wav", duration=5, fs=44100):
    """
    Records audio from the microphone and saves it to a WAV file.

    Args:
        filename (str): The name of the output WAV file.
        duration (int): Recording duration in seconds.
        fs (int): Sampling rate.
    """
    print("🔴 Recording... Please speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wav.write(filename, fs, audio)
    print(f"✅ Audio saved as {filename}")
