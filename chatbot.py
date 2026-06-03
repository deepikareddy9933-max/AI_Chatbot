import json

with open("responses.json", "r") as file:
    responses = json.load(file)

def get_response(message):
    message = message.lower()

    for keyword in responses:
        if keyword in message:
            return responses[keyword]

    return "Sorry, I don't understand that. Please ask another question."