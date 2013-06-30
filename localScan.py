#!/usr/local/bin/python2.7
# encoding: utf-8
'''
localScan -- scan your local network

localScan is free utility

@author:     Benoit Vanalderweireldt
        
@copyright:  2013 WebMining.eu. All rights reserved.
        
@license:    Apache License 2.0

@contact:    contact@web-mining.eu
'''
import netifaces
import re
import ping
__all__ = []
__version__ = 0.1
__date__ = '2013-06-30'
__updated__ = '2013-06-30'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class Address:
    address = None
    def __init__(self, address):
        self.address = address
    def process(self):
        print ping.do_one(self.address, 10)
        
        

for interface in netifaces.interfaces():
    if re.match('^(en|wln)\d+$', interface):
        address = netifaces.ifaddresses(interface)
        if len(address) >1:
            if len(address[2]) > 0:
                addr = address[2].pop()['addr']
                if re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', addr):
                    addrToProcess = Address(addr)
                    addrToProcess.process()
        
