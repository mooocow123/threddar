from threddar.rethread import Thread
from threddar import Threddar
from time import sleep

def yo():
    while True:
        sleep(2)
        print("yo")

def lo():
    while True:
        sleep(3)
        print("whatcha doin")

t = Thread(target=yo)
b = Thread(target=lo)
b.daemon = True
t.daemon = True

th = Threddar(t, b)
th.start()
while True:
    sleep(10000)