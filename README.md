# Pers. I. A. - Personal Intelligent Assistant

Persia - a simple "bot", or "assistant" which responds to several commands, using TTS and speech recognition. It runs on Python 3.5+.

Computer Vision was also introduced in the project using Opencv 3.0.0. Should you want to run the program on Python 2.7+, Opencv 2.4 should be used. Opencv 2.4 is a bit easier to install by using the following command:

	# sudo apt-get install python2-pip python2-dev libopencv-dev opencv-data

After installing libopencv-dev and opencv-data you'll just have to install the dependencies and you're ready to go.

The steps used to have opencv 3.0.0 running in Python 3+ (3.4/3.5) were based on these tutorials on hot to install opencv on Python 3+:

- http://cyaninfinite.com/tutorials/installing-opencv-in-ubuntu-for-python-3/

	or here:

- www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/


# Dependencies
There are several dependencies to solve in order to run this project. Please run the commands exactly how they are described here and in descending order in order to correctly configure your environment. Ensure you are inside the project's main folder before running the commands to configure the environment.

##### Ubuntu / Debian

```
  # sudo apt install virtualenv python3-pip python-dev python3-dev portaudio19-dev mpg321 cmake git v4l2ucp v4l-utils libv4l-dev libgtk2.0-dev pkg-config	
```

##### Python

```
  $ virtualenv persia-venv -p python3
  $ source persia-venv/bin/activate
  $ pip install -r py-requirements/dev.txt

```

##### OpenCV

```
  $ git clone https://github.com/Itseez/opencv.git
  $ cd opencv/
  $ git checkout 3.0.0
  $ mkdir release
  $ cd release/
  $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	  -D CMAKE_INSTALL_PREFIX=/usr/local \
	  -D INSTALL_C_EXAMPLES=ON \
	  -D INSTALL_PYTHON_EXAMPLES=ON \
	  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	  -D BUILD_EXAMPLES=ON ..

  // In the cmake output make sure that the python3 Interpreter, Libraries, numpy packages path are defined before continuing with the commands

  $ make -j4
  # sudo make install
  # sudo ldconfig
  $ cd ../../persia-venv/lib/python3.5/site-packages/
  
  // In the following command if the file 'cv2.cpython-35m-x86_64-linux-gnu.so' doesn't correspond to the existent version just replace the file name with the one with the correct version 'cv2.(insert version here or just press tab).so'.

  $ ln -s /usr/local/lib/python3.5/site-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so

```

# Running
In order to run the program ensure that you are inside the project's main folder and just run the following commands after installing all the dependencies:

	$ source persia-venv/bin/activate
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
