#!/bin/bash

cd /home/pi/lock
sudo tmux new -s lock -d 'sudo python lock.py'
sudo tmux new -s listen -d 'sudo node listen.js'