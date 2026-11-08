# HARIS AI
# Version 1.1

from ai_engine import get_response
from config import APP_NAME, VERSION, WELCOME_MESSAGE


def main():
    print("=" * 35)
    print(f"       {APP_NAME}")
    print(f"       Version {VERSION}")
    print("=" * 35)

    print(WELCOME_MESSAGE)
    print("Type 'exit' to close.")

    while True:
        message = input("\nYou: ").strip()

        if message.lower() == "exit":
            print("Haris AI: Goodbye!")
            break

        if not message:
            continue

        response = get_response(message)
        print(f"Haris AI: {response}")


if __name__ == "__main__":
    main()
