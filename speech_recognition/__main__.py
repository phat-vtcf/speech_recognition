import speech_recognition as sr
from calculator import *

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("Hello! I will calculate your equations for you,\nbut please be kind and use me in a quiet area.")
    print("If you want to use brackets, please use the words 'open' and 'close'.")
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                if value.lower() == "stop":
                    print("You said doe maar {}".format(value))
                    break
                ## Calculate
                print("You said {}".format(value))
                tidy_eq, result = calculate(value)
                if result == None:
                    print("That's not an equation! Try again.")
                else:
                    print(f"{tidy_eq} = {result}")
        except sr.UnknownValueError:
            print("What? What did you say? Could you repeat it more clearly?")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        # with m as source: r.adjust_for_ambient_noise(source)
except KeyboardInterrupt:
    pass
