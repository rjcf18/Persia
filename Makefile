install:
	sudo apt-get install pip python-pyaudio mpg321 build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libv4l-dev python-numpy python-scipy unzip libopencv-dev python-opencv opencv-data
	sudo pip install pyaudio SpeechRecognition gtts requests geocoder

run:
	python src/main.py
