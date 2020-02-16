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
		task  = r.recognize_google(audio).lower()
		print("You said: " + text)
	except:
		print("You said something misunderstanding!")
		command = command()
	if "jarvis" in task:
		return task




#=========================
#Router tasks
#=========================
def router(task):
	if task == 'exit':
		talk("Ok, no problem")
		sys.exit()
	elif task == "turn off pc":
		talk("goodbye")
		os.system("poweroff")
	elif 'open' in task:
		open(task)
	elif 'close' in task:
		os.system("killall " + task[task.find('close')+len(5):])
	else:
		talk("That function is developing")



#==============================
#Open something
#==============================
def open(task):
	talk("opening")
	if 'app' in task:
		keyword = 'app'
		if 'sublime' in task:
			t = os.system("subl")
		elif "browser" in task:
			t = os.system("firefox")
		elif "player" in task:
			t = os.system("rhythmbox")
		else:
			t = os.system(task[task.find(keyword)+len(keyword)+1:])	
	elif 'folder' in task:
		keyword = 'folder'
		t = os.system("nautilus | " + task[task.find(keyword)+len(keyword)+1:])
	else:
		webbrowser.open_new_tab('http://google.com/?q='+task[task.find(keyword)+len(keyword)+1:])
	talk("Opened")