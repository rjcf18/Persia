install:
	sudo apt-get install pip python-pyaudio mpg321
	sudo pip install pyaudio SpeechRecognition gtts requests python-geoip python-geoip-geolite2

run:
	python main.py
