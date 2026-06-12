def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi there!"
    elif "how are you" in user_input or "what's up" in user_input:
        return "I'm fine, thanks!"
    elif "name" in user_input or "who are you" in user_input:
        return "I'm a simple chatbot, nice to meet you!"
    elif "ok" in user_input:
        return "Yess.. Is there anything else?"
    elif "thank" in user_input:
        return "You're welcome!"
    elif "what can you do" in user_input:
        return "I can chat about basic things — try saying hello!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Greeting with pleasure! Bot here.")

    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print("Roxx:", response)

        if "bye" in user_message.lower().strip():
            break

run_chatbot()
