# Pepper

A simple "bot", or "assistant" which responds to several commands, using TTS and speech recognition. It runs on Python 2.7+ and Python 3.5+.

Computer Vision was introduced in the project, but this part works currently only on Python 2.7+ using Opencv 2.4.  In order to run the whole program in Python 3.4+ or 3.5+ you'll have to install Opencv 3.1.0.

Should you want to run the program in Python 3+ (3.4/3.5) just follow the steps described here:

- http://cyaninfinite.com/tutorials/installing-opencv-in-ubuntu-for-python-3/

	or here:

- www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/


# Dependencies
There are several dependencies to solve in order to run this project.

##### Ubuntu / Debain

```
  # sudo apt install python3-pip libopencv-dev opencv-data python3-dev portaudio19-dev mpg321
```

##### Python

```
  # pip3 install virtualenv
  $ virtualenv pepper-bot -p python3
  $ source pepper-bot/bin/activate
  $ pip install -r py-requirements/dev.txt

```

##### OpenCV

```
  $ git clone https://github.com/Itseez/opencv.git
  $ cd opencv
  $ mkdir release
  $ cd release
  $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
	$
  $ make -j4
  # sudo make install
	# sudo ldconfig
	# sudo ln -s /usr/local/lib/python3.5/site-packages/cv2.('version').so /path/to/the/virtualenv/folder/lib/python3.5/site-packages/cv2.so

```

# Running
In order to run the program just run the following command after installing all the dependencies:

	$ source pepper-bot/bin/activate
	$ python src/main.py

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
