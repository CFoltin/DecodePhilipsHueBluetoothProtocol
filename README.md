# DecodePhilipsHueBluetoothProtocol
We try to decode the Philips Hue Bluetooth protocol

- Tests to be done
  - Update: after update of a bulb, we try to connect with usual Bluetooth LE: ok
    - Remove the device from the app
    - Try to establish a pairing
  - Log different commands: ok
    - Select different colors and analyze the log files
    - Provide a log file of an update process
  - Look into the log file of the Android app itself for useful messages: open

# Analysis
See [Analysis](https://github.com/CFoltin/DecodePhilipsHueBluetoothProtocol/wiki/Analysis).


# first application for switching on/off
See [bluelamp.py](https://github.com/CFoltin/DecodePhilipsHueBluetoothProtocol/blob/master/bluelamp.py)

