#!bin/bash

# mv -i ./Door_lock/sh/* ./
DIR_NAME="Door_lock"

# tmux new -s $DIR_NAME -d
# sleep 1
# tmux send-keys -t $DIR_NAME "cd ~/doorlock" C-m
# tmux send-keys -t $DIR_NAME "rm -rf ./Door_lock" C-m
# tmux send-keys -t $DIR_NAME "git clone https://github.com/KlTUNE/Door_lock.git" C-m
# sleep 10
# tmux send-keys -t $DIR_NAME "python ./Door_lock/main.py" C-m

tmux new -s $DIR_NAME -d
sleep 1
tmux send-keys -t $DIR_NAME "cd ~/$DIR_NAME" C-m
tmux send-keys -t $DIR_NAME "rm -rf ./$DIR_NAME" C-m
tmux send-keys -t $DIR_NAME "git clone https://github.com/KlTUNE/$DIR_NAME.git" C-m
sleep 10
tmux send-keys -t $DIR_NAME "python ./$DIR_NAME/main.py" C-m

WEB_NAME="Door_lock_WEB"

tmux new -s $WEB_NAME -d
sleep 1
tmux send-keys -t $WEB_NAME "cd ~/$DIR_NAME" C-m
tmux send-keys -t $WEB_NAME "python ./$DIR_NAME/web_server.py" C-m