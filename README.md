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
- works for software version 1.53.3-r27175
- belongs to the `UUID 932c32bd-0002-47a2-835a-a8d455b859dd`

```
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
```

  
- works for software version  1.65.7_hCDE64320

- :!: The trick is, that the lamp must not be paired with a smart-phone. I've chosen to "reset" the device in the HUE app, then it got a new bluetooth-address and was not paired any longer. After this step, the things below worked out of the box :!:

```
root@haendel:~# bluetoothctl 
[NEW] Controller 00:15:83:D2:06:79 haendel [default]
...
[bluetooth]# devices
Device CB:40:11:0D:03:B5 Hue Lamp
Device C9:F0:78:3C:9E:CF Hue Lamp
[bluetooth]# paired-devices
Device CB:40:11:0D:03:B5 Hue Lamp
[bluetooth]# pairable on
Changing pairable on succeeded
[bluetooth]# scan
Missing on/off argument
[bluetooth]# scan on
Discovery started
[CHG] Controller 00:15:83:D2:06:79 Discovering: yes
[NEW] Device EF:03:B5:5F:1B:88 Hue Lamp
[bluetooth]# pair EF:03:B5:5F:1B:88
Attempting to pair with EF:03:B5:5F:1B:88
[CHG] Device EF:03:B5:5F:1B:88 Connected: yes
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 00001800-0000-1000-8000-00805f9b34fb
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 00001801-0000-1000-8000-00805f9b34fb
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 0000180a-0000-1000-8000-00805f9b34fb
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 0000fe0f-0000-1000-8000-00805f9b34fb
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 932c32bd-0000-47a2-835a-a8d455b859dd
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: 9da2ddf1-0000-44d0-909c-3f3d3cb34a7b
[CHG] Device EF:03:B5:5F:1B:88 UUIDs: b8843add-0000-4aa1-8794-c3f462030bda
[CHG] Device EF:03:B5:5F:1B:88 ServicesResolved: yes
[CHG] Device EF:03:B5:5F:1B:88 Paired: yes
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0001
        00001801-0000-1000-8000-00805f9b34fb
        Generic Attribute Profile
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0001/char0002
        00002a05-0000-1000-8000-00805f9b34fb
        Service Changed
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0001/char0002/desc0004
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0001/char0005
        00002b2a-0000-1000-8000-00805f9b34fb
        Unknown
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0001/char0007
        00002b29-0000-1000-8000-00805f9b34fb
        Unknown
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e
        0000180a-0000-1000-8000-00805f9b34fb
        Device Information
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char000f
        00002a29-0000-1000-8000-00805f9b34fb
        Manufacturer Name String
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0011
        00002a24-0000-1000-8000-00805f9b34fb
        Model Number String
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013
        00002a28-0000-1000-8000-00805f9b34fb
        Software Revision String
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015
        0000fe0f-0000-1000-8000-00805f9b34fb
        Unknown
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0016
        97fe6561-0001-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0018
        97fe6561-0003-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char001a
        97fe6561-0004-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char001c
        97fe6561-0008-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char001c/desc001e
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char001f
        97fe6561-1001-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char001f/desc0021
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0022
        97fe6561-2001-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0024
        97fe6561-2002-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0026
        97fe6561-2004-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0015/char0028
        97fe6561-a001-4f62-86e9-b71ee2da3d22
        Vendor specific
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a
        932c32bd-0000-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002b
        932c32bd-0001-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d
        932c32bd-0002-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d/desc002f
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char0030
        932c32bd-0003-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char0030/desc0032
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char0033
        932c32bd-0004-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char0033/desc0035
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char0039
        932c32bd-0006-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char003b
        932c32bd-0007-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char003b/desc003d
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char003e
        932c32bd-1005-47a2-835a-a8d455b859dd
        Vendor specific
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040
        b8843add-0000-4aa1-8794-c3f462030bda
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040/char0041
        b8843add-0001-4aa1-8794-c3f462030bda
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040/char0043
        b8843add-0002-4aa1-8794-c3f462030bda
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040/char0043/desc0045
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040/char0046
        b8843add-0003-4aa1-8794-c3f462030bda
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service0040/char0048
        b8843add-0004-4aa1-8794-c3f462030bda
        Vendor specific
[NEW] Primary Service
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service004a
        9da2ddf1-0000-44d0-909c-3f3d3cb34a7b
        Vendor specific
[NEW] Characteristic
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service004a/char004b
        9da2ddf1-0001-44d0-909c-3f3d3cb34a7b
        Vendor specific
[NEW] Descriptor
        /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service004a/char004b/desc004d
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration
Pairing successful
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Key: 0000fe0f-0000-1000-8000-00805f9b34fb
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Value: 0x02
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Value: 0x10
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Value: 0xff
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Value: 0xff
[CHG] Device EF:03:B5:5F:1B:88 ServiceData Value: 0x00
[Hue Lamp]# paired-devices
Device EF:03:B5:5F:1B:88 Hue Lamp
[CHG] Device D0:B5:C2:F7:FE:FB TxPower: 0
[Hue Lamp]# connect EF:03:B5:5F:1B:88
Attempting to connect to EF:03:B5:5F:1B:88
Connection successful
[Hue Lamp]# scan off
[CHG] Device EF:03:B5:5F:1B:88 TxPower is nil
[CHG] Device EF:03:B5:5F:1B:88 RSSI is nil
[CHG] Controller 00:15:83:D2:06:79 Discovering: no
Discovery stopped
[Hue Lamp:/service002a/char002b]# select-attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d
[Hue Lamp:/service002a/char002d]# read
Attempting to read /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d Value: 0x01
  01                                               .               
[Hue Lamp:/service002a/char002d]# write 0
Attempting to write /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d
[Hue Lamp:/service002a/char002d]# write 1
Attempting to write /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service002a/char002d
[Hue Lamp:/service002a/char002d]# select-attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013
[Hue Lamp:/service000e/char0013]# read
Attempting to read /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x31
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x2e
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x36
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x35
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x2e
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x37
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x5f
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x68
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x43
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x44
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x45
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x36
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x34
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x33
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x32
[CHG] Attribute /org/bluez/hci0/dev_EF_03_B5_5F_1B_88/service000e/char0013 Value: 0x30
  31 2e 36 35 2e 37 5f 68 43 44 45 36 34 33 32 30  1.65.7_hCDE64320
[Hue Lamp:/service000e/char0013]# exit
...
```

# first application for switching on/off
See bluelamp.py
