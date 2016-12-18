
## Install Cubieboard

[Armbian Debian Jessy](https://www.armbian.com/cubieboard-2/)

### System

System installed with [ArmBian Debian Jessie](https://docs.armbian.com/User-Guide_Getting-Started/)

First login uses root / 1234

Requires to change at first boot and create user account also.

```bash
$ ssh root@<ip>
```

### Installation 

Here are few things to install to run Cubieboard as a small garage server.

```bash
$ apt-get update
$ apt-get upgrade
$ apt-get install -y vim build-essential screen nodejs npm git
$ nodejs --version
$ ln -s /usr/bin/nodejs /usr/bin/node
$ npm install forever -g
$ 
```

### GPIOs

???

https://forum.armbian.com/index.php/topic/744-cubieboard2-gpio-help/



 