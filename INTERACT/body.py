import ear
import mouth


while True:
    data = ear.stream.read(4000, exception_on_overflow=False)
    # if len(data) == 0:
    #   break
    if ear.recognizer.AcceptWaveform(data):
        Text = ear.recognizer.Result()
        text = Text[14:-3]
        print(text)
        count = len(text.split())
        if count <= 3:
            if text == "athènes" or text == "athéna" or text == "a demain" or text == "a peine" or text == "demain" or text == "abdellah" or text == "avenant" or text == "demain" or text == "ah benin":
                mouth.engine.say(mouth.greeting())
                mouth.engine.runAndWait()

        elif count > 3:
            mouth.engine.say("parlons vrai et clair")
            mouth.engine.runAndWait()
        elif count > 3:
            mouth.engine.say("je ne te suis pas")
            mouth.engine.runAndWait()


