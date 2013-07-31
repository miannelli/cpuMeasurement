from time import sleep, time
from threading import Thread
import random
from multiprocessing import Process, Manager



class backgroundTaskLauncher:
    def __init__(self, chunkSize, chunkAmount, interchunkGap, processes):
        self.chunkSize = chunkSize
        self.chunkAmount = chunkAmount
        self.interchunkGap = interchunkGap
        self.processes = processes
        self.toggle = True

    def start(self):
        for i in range(0,self.processes):
            Process(target=self.taskLauncher, args=()).start()

    def taskLauncher:
        pass



    def stop(self):
        pass