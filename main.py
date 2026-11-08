
# HARIS AI
# Version 1.3

from ai_engine import get_response
from config import APP_NAME, WELCOME_MESSAGE


def main():
    history = []

    print("=" * 35)
    print(f"       {APP_NAME}")
    print("       Version 1.3")
    print("=" * 35)

    print(WELCOME_MESSAGE)
    print("Type 'exit' to close.")
    print("Type '/history' to see conversation history.")

    while True:
        message = input("\nYou: ").strip()

        if message.lower() == "exit":
            print("Haris AI: Goodbye!")
            break

        if not message:
            continue

        if message.lower() == "/history":
            print("\n--- CHAT HISTORY ---")
            for user, bot in history:
                print(f"You: {user}")
                print(f"Haris AI: {bot}")
            continue

        response = get_response(message)
        history.append((message, response))

        print(f"Haris AI: {response}")


if __name__ == "__main__":
    main()
    
