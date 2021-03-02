from pyfirmata import Arduino, util
import time

board = Arduino("COM3")
def setup():
 try:
  board.digital[13].write(1)
  board.digital[11].write(1)
  time.sleep(3)
  board.digital[13].write(0)
  board.digital[11].write(0)
 except :
     print("unable to connect to com3")
setup()
print("starting")
import speech_recognition as sr


def car():


 global text
 r = sr.Recognizer()


 with sr.Microphone() as source:
    print("say")
    audio = r.listen(source)

 try:
    print("you said " + r.recognize_google(audio))
    text = r.recognize_google(audio)
 except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
    

 except sr.RequestError as e:
    print("Could not request results from Google SpeechRecognitions service {0}.format(e))")
    pass

 if "straight" in text:
    board.digital[11].write(1)
    board.digital[13].write(1)
    car()
 elif "stop" in text:
    board.digital[11].write(0)
    board.digital[13].write(0)
    car()
 elif "right" in text:
    board.digital[11].write(0)
    board.digital[13].write(1)
    car()
 elif "left" in text:
    board.digital[11].write(1)
    board.digital[13].write(0)
    car()
 else:
     car()
car()
