from evdev import InputDevice, categorize, ecodes
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
def sysrun(command):
    f=open("lastCommand","w")
    f.write(command)
    f.close()
dev = InputDevice('/dev/input/by-id/usb-dakai_PS_2+USB_Keyboard-event-kbd')
dev.grab()
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            print(key.keycode)
            if key.keycode in config["KEYS"].keys():
                print("Executing "+config["KEYS"][key.keycode])
                sysrun(config["KEYS"][key.keycode])
