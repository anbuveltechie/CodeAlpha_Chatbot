
def get_reply(msg):
    msg = " ".join(msg.lower().strip().split()).rstrip("?.!").strip()

    if not msg:
        return "Please type something.", True

    elif msg in ("hello", "hi", "hey"):
        return "Hi! Welcome. How can I help you?", True

    elif msg == "how are you":
        return "I'm fine, thanks! How are you?", True

    elif msg in ("what is your name", "what's your name", "your name"):
        return "I'm CodeAlpha Bot, your virtual assistant.", True

    elif msg in ("help", "options"):
        return "You can say hello, ask how are you, ask my name, or say bye.", True

    elif msg in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a nice day!", False

    else:
        return "Sorry, I don't understand that. Type help to see available commands.", True


def main():
    print("\n" + "=" * 45)
    print("             CODEALPHA CHATBOT")
    print("=" * 45)
    print("Bot: Hello! I'm your virtual assistant.")
    print("Bot: Type 'help' to see available commands.")
    print("Bot: Type 'bye' whenever you want to exit.")
    print("=" * 45)

    while True:
        msg = input("\nYou: ")

        reply, running = get_reply(msg)

        print("Bot:", reply)

        if not running:
            break


if __name__ == "__main__":
    main()
