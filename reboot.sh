#!/usr/bin/bash
ps -ef | grep 'hotcutdaemon.py' | grep -v grep | awk '{print $2}' | xargs -r kill -9
python3 hotcutdaemon.py &
