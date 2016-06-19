
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

### Desktop

For the very minimal set of tools, install below:

```bash
$ sudo apt-get install gparted synaptic cifs-utils kdiff3 7z krename krusader
```

### Media

Using these very often. There is no need to name below too much:
- vlc: greatest video and music reader
- digikam: THE best photo library management by far
- audacity: whenever need to edit sound
- dvdrip: whenever you buy a DVD, rip it to NAS for streaming later, and forget about it

```bash
$ sudo apt-get install vlc audacity digikam dvdrip k3b
```

### Install Oracle JDK 8

Java is needed for many softwares.

Add the ppa, update and install:
```bash
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
```

### Development minimum

This is simply to edit and share the kind of file you are reading.

```bash
$ sudo add-apt-repository ppa:eugenesan/ppa
$ sudo apt-get update
$ sudo apt-get install smartgit
```

### Install NAS mounted drives

```bash
$ sudo apt-get install cifs-utils
$ sudo vi /etc/fstab
```

Add something like below:

```shell
//mynas/Medias /media/nas/Medias cifs credentials=/home/user/.cifspwd,noauto,iocharset=utf8,uid=1000,gid=1000,sec=ntlm 0 0
```

Edit password in /home/user/.cifspwd

```bash
sudo vi /home/clement/.cifspwd
```

such as below
```shell
username=xxx
password=yyy
```

Ensure file is not usable by others:

```bash
$ sudo chown root:root .cifspwd
$ sudo chmod 0600 .cifspwd
```



