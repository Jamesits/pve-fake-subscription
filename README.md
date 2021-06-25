Disables the "No valid subscription" dialog on all Proxmox products.

> I am really poor and I can't afford a license. I just want to get rid of the annoying dialog.

## Features

Works for:
- Proxmox VE (5.x or later, tested up to 7.0)
- Proxmox Mail Gateway (5.x or later)
- Proxmox Backup Server (1.x)

Highlights:
- Non-intrusive: zero modification of any system file
- Future-proof: persists between system updates & major upgrades
- Hassle-free: you can uninstall at any time
- Comes with standard Debian package, easy to manage and automate
- **No JavaScript is involved** in the whole process, as I believe JavaScript is harmful to developers

## Installation

1. [Download the latest release](https://github.com/Jamesits/pve-fake-subscription/releases/latest)
1. Install: run `dpkg -i pve-fake-subscription_*.deb` as root on every node
1. (Optional) `echo "127.0.0.1 shop.maurer-it.com" | sudo tee -a /etc/hosts` to prevent fake keys from being checked against the Proxmox servers

The fake subscription status doesn't grant you access to the enterprise repository. You should switch to the no-subscription repository if not already done. Use the following method:
- [PVE](https://pve.proxmox.com/wiki/Package_Repositories#sysadmin_no_subscription_repo)
- [PMG](https://pmg.proxmox.com/pmg-docs/pmg-admin-guide.html#pmg_package_repositories)
- [PBS](https://pbs.proxmox.com/docs/installation.html#proxmox-backup-no-subscription-repository)

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
