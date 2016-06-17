#!/usr/bin/env python

from persia import Persia
import logging
import speech_recognition as sr

def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    # Initialize Persia
    Persia.speak('Greetings. My name is Persia. How could I be of service?')
    Persia.initiate_Persia()

if __name__ == '__main__':
    main()
