dependencies:
	sudo apt install virtualenv python3-pip python-dev python3-dev portaudio19-dev mpg321 cmake git v4l2ucp v4l-utils libv4l-dev libgtk2.0-dev pkg-config	

config:
	virtualenv persia-venv -p python3
	source persia-venv/bin/activate
	pip install -r py-requirements/dev.txt

opencv:
	git clone https://github.com/Itseez/opencv.git
	cd opencv/
	git checkout 3.0.0
	mkdir release
	cd release/
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
	      -D CMAKE_INSTALL_PREFIX=/usr/local \
	      -D INSTALL_C_EXAMPLES=ON \
	      -D INSTALL_PYTHON_EXAMPLES=ON \
	      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	      -D BUILD_EXAMPLES=ON ..

	make -j4
	sudo make install
	sudo ldconfig
	cd ../../pepper-bot/lib/python3.5/site-packages/
	ln -s /usr/local/lib/python3.5/site-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so

run:
	source persia-venv/bin/activate
	python src/main.py

