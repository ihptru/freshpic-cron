#!/usr/bin/env python

import time

import remove_albums
import remove_images

class Factory:
    
    def __init__(self):
        self.start_time = time.mktime(time.strptime( time.strftime('%Y-%m-%d-%H-%M-%S'), '%Y-%m-%d-%H-%M-%S'))
        
    def run_jobs(self):
        remove_albums.start(self)
        remove_images.start(self)

if __name__ == "__main__":
    factory = Factory()
    factory.run_jobs()
    
