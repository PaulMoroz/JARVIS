import speech_recognition as sr
import os
import sys
import webbrowser
from espeak import espeak
#================
#Say something
#================
def talk(words):
	espeak.synth(words)

#================
#recognizing program
#================
def command():
	r = sr.Recognizer()

	with sr.Microphone() as sourse:
		print("Say something")
		r.pause_treshhold = 2
		r.adjust_for_ambient_noise(sourse, duration  = 1)
		audio = r.listen(sourse)

	try:
		text  = r.recognize_google(audio).lower()
		print("You said: " + text)
	except:
		print("You said something misunderstanding!")
		command = command()
	return text


def make_something(task):
	if task == 'exit':
		sys.exit()

command()
