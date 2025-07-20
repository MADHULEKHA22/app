from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os

def translate_and_speak(text, target_language):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(f"🌐 Translated: {translated}")

        tts = gTTS(translated, lang=target_language)
        filename = "temp.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

        os.remove(filename)
    except Exception as e:
        print(f"❌ Translation Error: {e}")
