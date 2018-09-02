# install-howto

Installation How-To (ubuntu, docker, etc)

* [Install Ubuntu 16.04](/system/desktop/ubuntu1604)


# setting USB to keep same port

Grep information on device:
```bash
  $ udevadm info -a -n /dev/ttyUSB1 | grep '{serial}'
    ATTRS{serial}=="A600dVPj"
    ATTRS{serial}=="0000:00:14.0"
  $ udevadm info -a -n /dev/ttyUSB1 | grep '{idProduct}'
    ATTRS{idProduct}=="6001"
    ATTRS{idProduct}=="9254"
    ATTRS{idProduct}=="0002"
  $ udevadm info -a -n /dev/ttyUSB1 | grep '{idVendor}'
    ATTRS{idVendor}=="0403"
    ATTRS{idVendor}=="058f"
    ATTRS{idVendor}=="1d6b"
```

Add rule for this device:
```bash
  $ sudo nano /etc/udev/rules.d/99-usb-serial.rules

  SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="04VKC0FD", SYMLINK+="ttyRfxTrx"
  SUBSYSTEM=="tty", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", SYMLINK+="ttyCurrenCost"
  SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A600dVPj", SYMLINK+="ttyJeeLink"
```