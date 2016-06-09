# Pepper

A simple "bot", or "assistant" which responds to several commands, using TTS and speech recognition.


## Dependencies

### There are several dependencies to solve in order to run this project. There is a makefile to make the process easier. 

	$ make install

### Install PyAudio

In most machines just run:

	$ pip install pyaudio
   or

	$ apt-get install python-pyaudio


portaudio.h may not link correctly on Mac OSX machines, if so happens run:

	$ pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

### SpeechRecognition - library using CMU Sphinx project, Google services, or Wit.ai

	$ pip install SpeechRecognition
    
### gTTS - Google Text-To-Speech

	$ pip install gtts

### mpg321

	$ apt-get install mpg321

### WolframAlpha

	$ pip install wolframalpha

### python-geoip

	$ pip install python-geoip
	$ pip install python-geoip-geolite2

### requests

	$ pip install requests

# Running
In order to run the program just run the following command after installing all the dependencies:

	$ python main.py

Or just use the Makefile:

	$ make run



