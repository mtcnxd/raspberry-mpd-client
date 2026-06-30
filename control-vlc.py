from gpiozero import Button
import socket

HOST = "127.0.0.1"
PORT = 4212

sock = socket.socket()
sock.connect((HOST, PORT))

play = Button(17)
next = Button(27)
prev = Button(22)

def send(cmd):
    sock.send((cmd + "\n").encode())

play.when_pressed = lambda: send("pause")
next.when_pressed = lambda: send("next")
prev.when_pressed = lambda: send("prev")

from signal import pause
pause()
