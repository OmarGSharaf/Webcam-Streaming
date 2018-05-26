import sys, os, signal
from subprocess import Popen


if __name__ == "__main__" : 
    for i in range (0,5):
        Popen(['python', 'Client.py'], stdin=None, stdout=None, stderr=None, close_fds=True)
