#!/usr/bin/env python

import time
import multiprocessing
import datetime
import os

import config
import remove_albums
import remove_images

class Factory:
    
    def __init__(self):
        self.start_time = self.current_time()

    def oprint(self, attr):
        f = open(config.logfile, 'a')
        f.write("["+time.strftime('%Y-%m-%d %H:%M:%S')+"] "+attr+"\n")
        f.close()

    def current_time(self):
        current = time.mktime(time.strptime( time.strftime('%Y-%m-%d-%H-%M-%S'), '%Y-%m-%d-%H-%M-%S'))
        return current

    def time_spent(self):
        difference = self.current_time() - self.start_time
        time_spent = str(datetime.timedelta(seconds = difference))
        return time_spent

    def run_jobs(self):
        self.oprint("**********  SESSION START  **********")
        multiprocessing.Process(target=self.image_factory).start()
    
    def image_factory(self):
        remove_albums.start(self)
        remove_images.start(self)
        self.oprint("**********  SESSION END  **********")

if __name__ == "__main__":
    try:
        os.mkdir("var")
    except OSError as e:
        if e.args[0]==17:   #Directory already exists
            pass    #Ignore
        else:
            raise e #Raise exception again

    factory = Factory()
    factory.run_jobs()
