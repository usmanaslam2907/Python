# Akbaar parh k sunao

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    # speak.Speak("Usman How are you and what are you doing here")
    speak.Speak(str)


if __name__ == '__main__':
    speak("Good by usman")
