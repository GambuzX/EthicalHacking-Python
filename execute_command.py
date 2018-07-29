#!/usr/bin/env python

import subprocess

command = "%SystemRoot%\Sysnative\msg.exe * you have been hacked"
subprocess.Popen(command, shell=True)