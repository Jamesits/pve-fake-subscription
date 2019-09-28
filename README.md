I am really poor and I really can't afford a license. I just want to get rid of the annoying dialog on every login.

## Features

* Works for any version >=5 (we've tested this from 5.3 to 6.0 without any changes in the code)
* Supports Proxmox VE and Proxmox Mail Gateway
* Non-intrusive, no changes to any system file, persists between system updates
* Comes with standard Debian package, easy to manage and automate
* You can uninstall at any time, hassle-free
* **No JavaScript**

## Installation

* Go to [release](https://github.com/Jamesits/pve-fake-subscription/releases/latest) to download the latest release
* Run `dpkg -i pve-fake-subscription_*.deb` as root on every Proxmox VE node

## Uninstallation

Run as root:

```shell
apt purge pve-fake-subscription
```

This will revert your system to a "no subscription key" status.

## Building the Package

Run everything as root on a Debian 10 system:

```shell
apt-get install ruby ruby-dev rubygems build-essential
gem install --no-ri --no-rdoc fpm
./package.sh
```
