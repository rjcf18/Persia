#!/usr/bin/env python

from pepper import Pepper
import logging
import speech_recognition as sr

def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    # Initialize Pepper
    Pepper.initiate_Pepper()

if __name__ == '__main__':
    main()
