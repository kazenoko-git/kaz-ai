import ai
chat = ai.AI(username="kazenoko", model=1)
tts = ai.tts(model=chat.getModel())

while 1:
    userInput = input("You: ")
    response = chat.ask(userInput)
    print(f"{chat.getModel()}: {response}")
    tts.speak(message=response,mood=chat.getMood())