#!/usr/bin/python3
from evdev import InputDevice, categorize, ecodes
import configparser, os
config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__))+'/config.ini')
def sysrun(command):
    os.system(command+ " &")
dev = InputDevice(config["DEVICE"]["path"])
dev.grab()
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            print(key.keycode)
            if key.keycode in config["KEYS"].keys():
                print("Executing "+config["KEYS"][key.keycode])
                sysrun(config["KEYS"][key.keycode])
