#!bin/bash

# SCREEN_NAME="doorlock"

# tmux new -s $SCREEN_NAME -d
# sleep 1
# tmux send-keys -t $SCREEN_NAME "cd ~/doorlock" C-m
# tmux send-keys -t $SCREEN_NAME "rm -rf ./Door_lock" C-m
# tmux send-keys -t $SCREEN_NAME "git clone https://github.com/KlTUNE/Door_lock.git" C-m
# sleep 10
# tmux send-keys -t $SCREEN_NAME "python ./Door_lock/main.py" C-m

SCREEN_NAME="Door_lock"

tmux new -s $SCREEN_NAME -d
sleep 1
tmux send-keys -t $SCREEN_NAME "cd ~/$SCREEN_NAME" C-m
tmux send-keys -t $SCREEN_NAME "rm -rf ./$SCREEN_NAME" C-m
tmux send-keys -t $SCREEN_NAME "git clone https://github.com/KlTUNE/$SCREEN_NAME.git" C-m
sleep 10
tmux send-keys -t $SCREEN_NAME "python ./$SCREEN_NAME/main.py" C-m