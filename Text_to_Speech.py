def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)
title=input("Enter Any Text:")
speak(title)