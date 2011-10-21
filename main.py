#!/usr/bin/env python2

import multiprocessing
import time

import remove_images

class Factory:
    
    def __init__(self):
        self.start_time = time.mktime(time.strptime( time.strftime('%Y-%m-%d-%H-%M-%S'), '%Y-%m-%d-%H-%M-%S'))
        
    def run_jobs(self):
        multiprocessing.Process(target=remove_images.start, args=(self,)).start()

if __name__ == "__main__":
    factory = Factory()
    factory.run_jobs()
    
