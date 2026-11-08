# HARIS AI ENGINE
# Version 1.2

def get_response(message):
    message = message.lower().strip()

    # English
    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to Haris AI!"

    if "your name" in message or "who are you" in message:
        return "I am Haris AI, your personal assistant!"

    if "how are you" in message:
        return "I am working perfectly!"

    # Greek
    if any(word in message for word in ["γεια", "καλησπέρα", "καλημέρα"]):
        return "Γεια σου! Είμαι το Haris AI!"

    if "πως σε λενε" in message or "ποιος εισαι" in message:
        return "Με λένε Haris AI!"

    if "τι κανεις" in message:
        return "Είμαι έτοιμο να σε βοηθήσω!"

    if "ευχαριστω" in message:
        return "Παρακαλώ! Χαίρομαι που βοηθάω!"

    if "βοηθεια" in message:
        return "Φυσικά! Πες μου τι χρειάζεσαι."

    return "Δεν γνωρίζω ακόμη την απάντηση. Μαθαίνω συνεχώς!"
