#!bin/bash

SCREEN_NAME="Door_lock"

tmux send-keys -t $SCREEN_NAME ^C
sleep 5
tmux kill-session -t $SCREEN_NAME