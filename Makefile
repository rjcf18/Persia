install:
	sudo apt-get install pip python-pyaudio mpg321
	sudo pip install pyaudio SpeechRecognition gtts requests geocoder

run:
	python main.py
