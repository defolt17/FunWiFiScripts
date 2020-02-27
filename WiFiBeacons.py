from os import system
from random import randint
import signal
from random import randint

def chunk(l, n):
    # Split array of items by n in each
    for i in range(0, len(l), int(n)): yield l[i:i + int(n)]

def terminateAir():
    system("sudo killall airbase-ng")

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    terminateAir()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

adapterName = input("Your adapter name [ wlp0s20u2mon ]: ")
if adapterName == "":
    adapterName = "wlp0s20u2mon"

APnum = int(input("AP number [ tested max - 50 ]: "))
APnames = []

for i in range(1, APnum+1):
    # APnames.append(input("AP-"+str(i)+" name: "))
    APnames.append("\"MGTS_GPON_"+str(randint(0, 9999)).zfill(4)+"\"")

print(APnames)

print("Starting!")

for i in range(APnum):
    macAddr = ":".join(list(chunk(hex(i)[2:].zfill(12), 2)))
    system("sudo airbase-ng"+" -a "+macAddr+" --essid "+APnames[i]+" -c "+str(i+1 % 12)+" "+adapterName+" -x 1"+" &")

while True:
    pass
