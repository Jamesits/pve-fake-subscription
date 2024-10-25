# pve-fake-subscription

![JavaScript free](https://img.shields.io/badge/JavaScript-free-%09%23f7df1e "No JavaScript is involved in this project. ")

Disables the "No valid subscription" dialog on all Proxmox products.

> I am really poor and I can't afford a license. I just want to get rid of the annoying dialog.

## Features

Works for:

- Proxmox VE (5.x or later)
- Proxmox Mail Gateway (5.x or later)
- Proxmox Backup Server (1.x or later)

Highlights:

- Non-intrusive: zero modification of any system file
- Future-proof: persists between system updates & major upgrades
- Hassle-free: you can uninstall at any time
- Comes with standard Debian package, easy to manage and automate
- **No JavaScript is involved** in the whole process, as I believe JavaScript is harmful to developers

## Usage

### Installation

1. [Download the latest release](https://github.com/Jamesits/pve-fake-subscription/releases/latest)
1. Install: run `dpkg -i pve-fake-subscription_*.deb` as root on every node
1. (Optional) `echo "127.0.0.1 shop.maurer-it.com" | sudo tee -a /etc/hosts` to prevent fake keys from being checked against the Proxmox servers

Notes:

After installation, please refrain yourself from clicking the "check" button on the "Subscription" page. It will invalidate the cache and temporary revert your instance into an unlicensed status.

The fake subscription status doesn't grant you free access to the enterprise repository. You should switch to the no-subscription repository if not already done. Use the following method:

- [Proxmox VE (PVE)](https://pve.proxmox.com/wiki/Package_Repositories#sysadmin_no_subscription_repo)
- [Proxmox Mail Gateway (PMG)](https://pmg.proxmox.com/pmg-docs/pmg-admin-guide.html#pmg_package_repositories)
- [Proxmox Backup Server (PBS)](https://pbs.proxmox.com/docs/installation.html#proxmox-backup-no-subscription-repository)

### Uninstallation

Run as root:

```shell
apt purge pve-fake-subscription
```

This will revert your system to a "no subscription key" status.

## Development Notes

### Building the Package

Install [nFPM](https://nfpm.goreleaser.com/install/), then:

```shell
./package.sh
```

### Compatibility for Old Proxmox VE Versions

#### PVE 4.x

PVE 4.x is supported with minor changes to the script.

Changes needed:
- License key needs to be changed from `pve8p` to `pve4p`

#### PVE 3.x

PVE 3.x is supported with minor changes to the script.

Changes needed:
- The script's hashbang need to be changed from `#!/usr/bin/env python3` to `#!/usr/bin/env python`
- License key needs to be changed from `pve8p` to `pve4p`

Installation with `dpkg -i` will not work. Use the following script to install manually:
```shell
mkdir -p /tmp/pve-fake-subscription
dpkg-deb -x pve-fake-subscription_*.deb /tmp/pve-fake-subscription
sed -i'' -e's/python3/python/g' -e's/pve8p/pve4p/g' /tmp/pve-fake-subscription/usr/bin/pve-fake-subscription
mv /tmp/pve-fake-subscription/usr/bin/pve-fake-subscription /usr/local/bin/
rm -rf /tmp/pve-fake-subscription
ln -sf /usr/local/bin/pve-fake-subscription /etc/cron.hourly/pve-fake-subscription
/usr/local/bin/pve-fake-subscription
```

Removal:
```shell
rm -f /usr/local/bin/pve-fake-subscription /etc/cron.hourly/pve-fake-subscription
```
