# HARIS AI ENGINE

def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! I am Haris AI."

    elif "name" in message:
        return "My name is Haris AI."

    elif "how are you" in message:
        return "I am working perfectly!"

    else:
        return "I don't know that yet, but I am learning!"
