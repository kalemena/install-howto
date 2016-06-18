# install-howto

Installation How-To (ubuntu, docker, etc)

## Install Ubuntu 16.04

* [Download NetInstall](http://archive.ubuntu.com/ubuntu/dists/xenial-updates/main/installer-amd64/current/images/netboot/mini.iso)
* Flash the iso to USB key (using UNetBootIn for example)
* Reboot from the USB key
* Follow the install up to disk management, and do manual
 * Split disk in at least 3 partitions:
  * System mapped on / (reformat)
  * User Home on /home, this way to ensure next install keeps all files and properties from users
  * Swap
 * When asked for distribution, pick ubuntu desktop (may as well select from the plenty other flavors!)

## Components

### desktop

```bash
$ sudo apt-get install gparted synaptic cifs-utils kdiff3 7z krename krusader
```

### Media

```bash
$ sudo apt-get install vlc audacity digikam dvdrip k3b
```

### Install Oracle JDK 8

Add the ppa, update and install:
```bash
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
```

### Development minimum

```bash
$ sudo add-apt-repository ppa:eugenesan/ppa
$ sudo apt-get update
$ sudo apt-get install smartgit
```

