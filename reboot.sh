#!/usr/bin/bash
ps -ef | grep 'hotcutdaemon.py' | grep -v grep | awk '{print $2}' | xargs -r kill -9
nohup python3 hotcutdaemon.py &
