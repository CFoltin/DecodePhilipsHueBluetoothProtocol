# DecodePhilipsHueBluetoothProtocol
We try to decode the Philips Hue Bluetooth protocol

# Analysis
See [Analysis](https://github.com/CFoltin/DecodePhilipsHueBluetoothProtocol/wiki/Analysis).


# first application for switching on/off, setting color and brightness


See [bluelamp.py](https://github.com/CFoltin/DecodePhilipsHueBluetoothProtocol/blob/master/bluelamp.py)

Works for the following firmware versions:
* 1.65.9_hB3217DF4
* 1.65.7_hCDE64320
* 1.53.3_r27175

## Installation on a raspberry pi 3

*  apt install python-pexpect python-pip bluez
*  apt-get remove python-filelock
*  pip install lockfile
*  git clone https://github.com/CFoltin/DecodePhilipsHueBluetoothProtocol.git
*  ./DecodePhilipsHueBluetoothProtocol/bluelamp.py --device <MAC> --verbose --switch-on
