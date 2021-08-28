import os, time
lastCommand=""
r = open("lastCommand","r")
while True:
    r.seek(0,0)
    cmd = r.read()
    if cmd != "OK":
        print(cmd+ " &")
        os.system(cmd + " &")
        r.close()
        r = open("lastCommand","w")
        r.write("OK")
        r.close()
        r = open("lastCommand","r")
    time.sleep(0.5)
