#!/usr/bin/python
#
# script turns philips hue on/off via bluetooth.
# author: christian foltin
# adapted from: Tony DiCola
#
# Dependencies:
# - You must install the pexpect library, typically with 'sudo pip install pexpect'.
# - You must have bluez installed and gatttool in your path 
#
# License: Released under an MIT license: http://opensource.org/licenses/MIT

import sys
import time
import os.path

import pexpect
from lockfile import FileLock
import argparse

def getStatus(gatt, bulb):
    gatt.sendline('char-read-hnd 0x0027')
    gatt.expect('Characteristic value/descriptor: (.*)')        
    all = gatt.match.group(1)
    print "%s: Status: %s" % (bulb, all[0:2]) 


parser = argparse.ArgumentParser(description='Control sygonix ht100bt modules..')
parser.add_argument('--switch-on', dest='switchOn', action='store_true')
parser.add_argument('--switch-off', dest='switchOn', action='store_false')
parser.set_defaults(switchOn=True)
parser.add_argument('--device', dest='device', required=True,
                                        help='device mac address of the form XX:XX:XX:XX:XX')
parser.add_argument('--verbose', dest='verbose',  action='store_true',
                                        help='Verbose output')

args = parser.parse_args()
#args.verbose=True

status = "00"
if args.switchOn:
    status = "01"

# Get thermostat address from command parameters.
bulb = args.device
lock = FileLock('/tmp/bluetooth.lock')
with lock:
            
    bluectl = pexpect.spawn('bluetoothctl')
    if args.verbose:
        bluectl.logfile = sys.stdout
    bluectl.sendline('power off')
    bluectl.expect('Changing power off succeeded')
    time.sleep(1)
    bluectl.sendline('power on')
    bluectl.expect('Changing power on succeeded')
    bluectl.expect('Powered: yes')
    
    # Run gatttool interactively.
    gatt = pexpect.spawn('gatttool -t random -I -b %s' % bulb)
    if args.verbose:
        gatt.logfile = sys.stdout
    
    # Connect to the device.
    retries = 10
    retValue = 0
    while retries > 0 and retValue != 1:
        gatt.sendline('connect')
        retValue = gatt.expect(['Device or resource busy','Connection successful','Transport endpoint is not connected', 'connect error'])
        retries-=1
        if retValue != 1:
            time.sleep(1)

    if retValue == 1:
        getStatus(gatt, bulb)
        gatt.sendline('char-write-req 0x0027 %s' % (status) )
        retValue = gatt.expect(['Characteristic value was written successfully', 'Attribute can\'t be written'])
        if retValue == 0:
            getStatus(gatt, bulb)
        else:
            print "Device busy, sorry."
    
    gatt.sendline('disconnect')
    
    bluectl.sendline('power off')
    bluectl.expect('.*#')
    #bluectl.expect('.*Powered: no')
    bluectl.sendline('exit')
