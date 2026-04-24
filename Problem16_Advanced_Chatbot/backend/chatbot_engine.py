rules = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Nice to meet you.",
    "bye": "Goodbye! Have a nice day.",
    "order": "Your order has been placed successfully.",
    "weather": "Today's weather is sunny.",
    "name": "I am an AI Chatbot powered by logic."
}

def get_response(query):
    query = query.lower().strip()

    for key in rules:
        if query.startswith(key):
            return rules[key]

    return "Sorry, I didn't understand your query."