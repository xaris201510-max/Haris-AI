# HARIS AI
# Version 1.0

def main():
    print("========================")
    print("       HARIS AI")
    print("========================")
    print("Hello! I am Haris AI.")
    print("Type 'exit' to close.")

    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            print("Haris AI: Goodbye!")
            break

        elif message.lower() in ["hello", "hi"]:
            print("Haris AI: Hello! How can I help you?")

        else:
            print("Haris AI: I am still learning!")


if __name__ == "__main__":
    main()
