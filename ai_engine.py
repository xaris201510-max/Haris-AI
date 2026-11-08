
# HARIS AI ENGINE
# Version 1.3

import unicodedata


def normalize(text):
    text = text.lower().strip()
    text = unicodedata.normalize("NFD", text)
    return "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )


def get_response(message):
    text = normalize(message)

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "γεια", "καλημερα", "καλησπερα"]):
        return "Hello! Γεια σου! I am Haris AI!"

    # Identity
    if any(word in text for word in ["your name", "who are you", "ποιος εισαι", "πως σε λενε"]):
        return "I am Haris AI, your personal assistant!"

    # Feelings
    if "how are you" in text or "τι κανεις" in text:
        return "I am working perfectly! Είμαι έτοιμο να βοηθήσω!"

    # Help
    if "help" in text or "βοηθεια" in text:
        return "Of course! Tell me what you need help with."

    # Thanks
    if "thank" in text or "ευχαριστ" in text:
        return "You're welcome! Παρακαλώ!"

    # Time
    if "time" in text or "ωρα" in text:
        return "I cannot check the current time yet."

    # Goodbye
    if any(word in text for word in ["goodbye", "bye", "αντιο"]):
        return "Goodbye! Τα λέμε!"

    return "I don't know that answer yet. I am still learning!"
    
