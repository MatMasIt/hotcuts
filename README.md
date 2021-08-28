# hotcuts
Transform an input device into a shortcut board. for example, a second keyboard with pictures on keys

## How does it work?

A main daemon (`rootDaemon.py`) running as root intercepts a keyboard device through its device file, acquiring a lock on it and preventing it from sending inputs to the X server.

The key presses trigger commands by saving them to a file (`lastCommand`), and allowing the puppet process (`userpuppet.py`), which executes the commands and clears the cache file.

The main daemon should be run as root (edit it accordingly to set your device path, edit the INI file according to your needs) and the puppet process should run in the current user.

## WeewooWeewo, a process reading commands from a file?

Yes, besides the daemon needs root to grab the device, so it is best to pass commands to a puppet process in the user, which is also useful because it executes other apps as a normal user.

if you are concerned about a malicious actor editing the cache command file, be assured they could easily edit the daemon and the puppet too, or if anything the whole home and possibily `.bashrc`
