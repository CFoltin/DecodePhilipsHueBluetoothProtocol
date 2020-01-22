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
  
# first successful switch-off!

  [bluetooth]# devices
  Device CB:40:11:0D:03:B5 Hue Lamp
  Device C9:F0:78:3C:9E:CF Hue Lamp
  [bluetooth]# paired-devices
  Device CB:40:11:0D:03:B5 Hue Lamp
  [bluetooth]# connect CB:40:11:0D:03:B5
  Attempting to connect to CB:40:11:0D:03:B5
  [CHG] Device CB:40:11:0D:03:B5 Connected: yes
  Connection successful
  [CHG] Device CB:40:11:0D:03:B5 ServicesResolved: yes
  [Hue Lamp]# select-attribute /org/bluez/hci0/dev_CB_40_11_0D_03_B5/service0023/char0026
  [Hue Lamp:/service0023/char0026]# write 0
  Attempting to write /org/bluez/hci0/dev_CB_40_11_0D_03_B5/service0023/char0026
  [Hue Lamp:/service0023/char0026]# exit

  
