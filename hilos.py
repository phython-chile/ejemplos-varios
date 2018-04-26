# -- coding: utf-8 --
#************#
from math import sin
import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        x = list(range(0,100))
        y = [0.0 for i in range(len(x))]

        print "inicio:" + self.getName()
        for i in range(100):
            y[i] = sin(x[i])
        print "terminado" + self.getName()

if __name__=="__main__":
    for x in range(10):
        hilo = MiHilo(name="Thread:" + str(x+1))
        hilo.start()
        time.sleep(.5)