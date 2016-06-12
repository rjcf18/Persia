# Pepper

A simple "bot", or "assistant" which responds to several commands, using TTS and speech recognition. It runs on Python 2.7+ and Python 3.5+.

Computer Vision was introduced in the project, but this part works currently only on Python 2.7+ using Opencv 2.4.  In order to run the whole program in Python 3.4+ or 3.5+ you'll have to install Opencv 3.1.0. 

Should you want to run the program in Python 3+ (3.4/3.5) just follow the steps described here: 

- http://cyaninfinite.com/tutorials/installing-opencv-in-ubuntu-for-python-3/
	
	or here:

- www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/


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

### geocoder - Simple and consistent geocoding library

	$ pip install geocoder

### requests

	$ pip install requests

### OpenCV - Open Source Computer Vision

	$ apt-get install libopencv-dev python-opencv opencv-data python-numpy python-scipy

	or 

	follow these steps here: 

- http://cyaninfinite.com/tutorials/installing-opencv-in-ubuntu-for-python-3/

	or here:

- www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/

# Running
In order to run the program just run the following command after installing all the dependencies:

	$ python main.py

Or just use the Makefile:

	$ make run
	
# Examples of commands that may be used to interact with the bot

	$ Pepper (Bots' name)
	$ Shutdown/Go Away/Stop Listening/That's all
	$ How are you?
	$ Thank you
	$ What time is it?/Tell me the time
	$ What day is it?
	$ Open browser/map/gmail/youtube/facebook/home folder/music/pictures/documents...
	$ Search ... (opens a google search)
	$ Wolfram search ... (searches in the wolframalpha website)
	$ Calculate ... (performs calculations also using wolframalpha)
	$ Report the weather/Weather/Tell me the weather/Weather report in ...(if you dont specify where, it fetches the location according to the external IP address) detailed(more detailed weather report)/brief (a very brief weather report)
	$ Detect faces/Facial detection (tries to detect faces and reports back how many faces where detected)
	$ ...
