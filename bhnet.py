import sys
import socket
import argparse
import threading
import subprocess


def main():
	parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help='Target host address', type=str)
    parser.add_argument('-p', '--port', help='The target port', type=str)
    parser.add_argument('-l', '--listen', help='Listen on [host]:[port] for incoming connections', action='store_true')
    parser.add_argument('-e', '--execute', help='Execute the given file upon receiving a connection', type=str)
    parser.add_argument('-c', '--command', help='Initialize a command shell', type=str)
    parser.add_argument('-m', '--message', help='Message to send', type=str)
    args = parser.parse_args()
