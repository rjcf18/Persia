# Pepper

A simple "bot", or "assistant" which responds to several commands, using TTS and speech recognition. It runs on Python 2.7+ and Python 3.5+.

Computer Vision was introduced in the project, but this part works currently only on Python 2.7+ using Opencv 2.4. The whole program can be executed with Python 3.4+ or 3.5+ by installing Opencv 3.1.0. 

Should you want to run this program in Python 3+ (3.4/3.5) just follow the steps described here: http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/


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

	follow these steps: http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/

# Running
In order to run the program just run the following command after installing all the dependencies:

	$ python main.py

Or just use the Makefile:

	$ make run



