#!/usr/bin/env python

import time
import multiprocessing
import datetime

import remove_albums
import remove_images

class Factory:
    
    def __init__(self):
        self.start_time = time.mktime(time.strptime( time.strftime('%Y-%m-%d-%H-%M-%S'), '%Y-%m-%d-%H-%M-%S'))

    def current_time(self):
        current = time.mktime(time.strptime( time.strftime('%Y-%m-%d-%H-%M-%S'), '%Y-%m-%d-%H-%M-%S'))
        return current

    def run_jobs(self):
        multiprocessing.Process(target=self.image_factory).start()
    
    def image_factory(self):
        remove_albums.start(self)
        remove_images.start(self)
        current = self.current_time()
        difference = current - self.start_time
        result = str(datetime.timedelta(seconds = difference))
        print "It took %s to remove images" % result

if __name__ == "__main__":
    factory = Factory()
    factory.run_jobs()
    
