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
from datetime import datetime

import pexpect
from lockfile import FileLock
import argparse

def getHandle(gatt, uuid):
    gatt.sendline('char-read-uuid %s' % (uuid) )
    gatt.expect('handle: 0x00(.*)\s+value:.*')
    handle = gatt.match.group(1)
    return handle

def getStatus(gatt, bulb, handle, description):
    gatt.sendline('char-read-hnd 0x00%s' % (handle))
    gatt.expect('Characteristic value/descriptor: (.*)')        
    all = gatt.match.group(1)
    print ("%s (handle %s): Status: %s" % (description, bulb, all[0:2]) )

def writeValue(gatt, bulb, handle, status, description):
    getStatus(gatt, bulb, handle, description)
    gatt.sendline('char-write-req 0x00%s %s' % (handle, status) )
    retValue = gatt.expect(['Characteristic value was written successfully', 'Attribute can\'t be written'])
    if retValue == 0:
        getStatus(gatt, bulb, handle, description)
    else:
        print ("Device busy, sorry.")
    
def disconnect(gatt, bluectl):
    gatt.sendline('disconnect')

    bluectl.sendline('power off')
    bluectl.expect('.*#')
    #bluectl.expect('.*Powered: no')
    bluectl.sendline('exit')

parser = argparse.ArgumentParser(description='Control Philips Hue modules..')
parser.add_argument('--switch-on', dest='switchOn', action='store_true')
parser.add_argument('--switch-off', dest='switchOn', action='store_false')
parser.set_defaults(switchOn=True)
parser.add_argument('--ping', dest='ping', action='store_true')
parser.set_defaults(ping=False)
parser.add_argument('--device', dest='device', required=True,
                                        help='device mac address of the form XX:XX:XX:XX:XX')
parser.add_argument('--color', dest='color', required=False,
                                        help='set a color in hex-form like "c601" (must be exactly 4 hex numbers). default is 6e01')
parser.add_argument('--brightness', dest='brightness', required=False,
                                        help='set the brightness in hex-form like "7f" (must be exactly 2 hex numbers). Full brightness corresponds to 0xfe')
parser.add_argument('--verbose', dest='verbose',  action='store_true',
                                        help='Verbose output')
parser.add_argument('--retries', dest='retries', required=False,
                                        help='Amount of retries')
parser.set_defaults(retries=0)

print(datetime.now())
args = parser.parse_args()
#args.verbose=True

status = "00"
if args.switchOn:
    status = "01"

bulb = args.device
lock = FileLock('/tmp/bluetooth.lock')
rounds = int(args.retries)
with lock:
    while rounds >= 0:
        rounds = rounds - 1
        try:
            bluectl = pexpect.spawn('bluetoothctl', encoding='utf-8')
            if args.verbose:
                bluectl.logfile = sys.stdout
            bluectl.sendline('power off')
            bluectl.expect('Changing power off succeeded')
            time.sleep(1)
            bluectl.sendline('power on')
            bluectl.expect('Changing power on succeeded')
            bluectl.expect('Powered: yes')
            bluectl.sendline('paired-devices')
            retValue = -1
            try:
                retValue = bluectl.expect(['Device %s ' % (bulb)], timeout=5)
            except:
                pass
            if retValue != 0:
                print ("""
ERROR:
------
Hue lamp doesn't seem to be paired. 
    First, reset the device in the app (not only 'remove' it, but really reset to factory defaults). Then it gets a new bluetooth address.
    Then, start bluetoothctl with the commands
      power on
      scan on
      <wait to see the new address of the lamp>
      scan off
      agent on
      default-agent
      discoverable on
      pairable on
      pair <device>
      exit
""")
                exit(1)
            
            # Run gatttool interactively.
            gatt = pexpect.spawn('gatttool -t random -I -b %s' % bulb, encoding='utf-8')
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
        
            if retValue != 1:
                disconnect(gatt, bluectl)
                exit(1)
            # only ping?
            if args.ping:
                print("Device %s successfully pinged" % (bulb))
                disconnect(gatt, bluectl)
                exit(0)
        
            if args.verbose:
                # read software version
                uuid = "00002a28-0000-1000-8000-00805f9b34fb"
                handle = getHandle(gatt, uuid)
                getStatus(gatt, bulb, handle, "Software version")
                
            if args.brightness:
                uuid_brightness = "932c32bd-0003-47a2-835a-a8d455b859dd"
                handle_brightness = getHandle(gatt, uuid_brightness)
                writeValue(gatt, bulb, handle_brightness, args.brightness, "Brightness")
            if args.color:
                uuid_color = "932c32bd-0004-47a2-835a-a8d455b859dd"
                handle_color = getHandle(gatt, uuid_color)
                writeValue(gatt, bulb, handle_color, args.color, "Color")
            # determine handle for on-/off switch uuid
            uuid = "932c32bd-0002-47a2-835a-a8d455b859dd"
            handle = getHandle(gatt, uuid)
            writeValue(gatt, bulb, handle, status, "On/Off-Status")
                
            disconnect(gatt, bluectl)
            break
        except:
            print("Exception.")
