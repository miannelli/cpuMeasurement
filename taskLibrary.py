from time import sleep, time
from threading import Thread
import random
from multiprocessing import Process, Manager


def task(taskSize):
    a = 0;
    for i in range(1,taskSize):
        a+=1


class backgroundTaskLauncher:
    def __init__(self, chunkSize, chunkAmount, interchunkGap, processes):
        self.chunkSize = chunkSize
        self.chunkAmount = chunkAmount
        self.interchunkGap = interchunkGap
        self.processes = processes
        self.toggle = False

    def modify(self, chunkSize, chunkAmount, interchunkGap):
        self.toggle = False
        self.chunkSize = chunkSize
        self.chunkAmount = chunkAmount
        self.interchunkGap = interchunkGap

    def taskLauncher(self):
        while self.toggle:
            for i in range(0,self.chunkAmount):
                Thread(target=task, args=()).start()
            sleep(self.interchunkGap*random.random()*2)

    def start(self):
        self.toggle = True

    def stop(self):
        self.toggle = False



class probeTaskLauncher:
    pass