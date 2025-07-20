import webbrowser
import pyttsx3
import urllib.parse
import pywhatkit

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

def handle_command(text):
    text = text.lower()

    known_sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "whatsapp": "https://web.whatsapp.com",
        "twitter": "https://www.twitter.com",
    }

    # ✅ Auto-play song using pywhatkit
    if "play" in text or "youtube" in text:
        query = text.replace("play", "").replace("search", "").replace("on youtube", "").replace("youtube", "").strip()
        if query:
            speak(f"Playing {query} on YouTube")
            pywhatkit.playonyt(query)
            return f"Playing {query} on YouTube"
        else:
            return "What song do you want me to play?"

    # ✅ Google search
    if "search" in text or "google" in text:
        query = text.replace("search", "").replace("google", "").strip()
        if query:
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            speak(f"Searching Google for {query}")
            webbrowser.open(url)
            return f"Searching Google for {query}"
        else:
            return "What should I search for?"

    # ✅ Open known site
    if "open" in text:
        for key in known_sites:
            if key in text:
                url = known_sites[key]
                speak(f"Opening {key}")
                webbrowser.open(url)
                return f"Opening {key.capitalize()}"

        # Fallback: try to open by domain
        words = text.split()
        for word in words:
            if "." in word:
                url = word if word.startswith("http") else "https://" + word
                webbrowser.open(url)
                speak(f"Opening {url}")
                return f"Opening {url}"

    return "Sorry, I couldn't understand what to do."
