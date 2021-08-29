# hotcuts
Transform an input device into a shortcut board. for example, a second keyboard with pictures on keys

## How does it work?

A main daemon (`hotcutdaemon.py`) running as root intercepts a keyboard device through its device file, acquiring a lock on it and preventing it from sending inputs to the X server.

The key presses trigger commands  as specified in the `config.ini` file

## Setup

1. Locate the device file and edit `config.ini` by setting the device path and your shortcuts.
2.  Determine your keyboards serial id (you may use,`sudo udevadm info -a -n {DEVICE_FILE}`) edit `udev/99-keyboard-shortcuts.rules` with it, while setting `OWNER={Your username}` and add said file to `/etc/udev/rules.d` to tell udev to allow your user to access the device file; restart udev with `sudo udevadm trigger`
3. chmod +x `hotcutdaemon.py` with your user
4. add `hotcutdaemon.py` to a crontab (or to your i3/wm config file) for automatic execution
