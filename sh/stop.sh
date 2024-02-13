#!bin/bash

DIR_NAME="Door_lock"

tmux send-keys -t $DIR_NAME ^C
sleep 2
tmux kill-session -t $DIR_NAME

WEB_NAME="Door_lock_WEB"

tmux send-keys -t $WEB_NAME ^C
sleep 2
tmux kill-session -t $WEB_NAME