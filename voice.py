import pyttsx3

_engine = None


def _get_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 180)  # speaking speed
    return _engine


def speak(text: str):
    """
    Make Dora speak the given text out loud.
    """
    try:
        engine = _get_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        # Avoid crashing if sound fails
        pass
