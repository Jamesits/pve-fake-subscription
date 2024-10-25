# pve-fake-subscription

![JavaScript free](https://img.shields.io/badge/JavaScript-free-%09%23f7df1e "No JavaScript is involved in this project. ")

Disables the "No valid subscription" dialog on all Proxmox products.

> I am really poor and I can't afford a license. I just want to get rid of the annoying dialog.

## Features

Works for:

- Proxmox VE (5.x or later; 3.x and 4.x [require some manual actions](#compatibility-information-for-old-proxmox-ve-versions))
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

### Compatibility Information for Old Proxmox VE Versions

#### PVE 4.x

PVE 4.x is supported with minor changes to the script.

After installation or updates, run:
```shell
sed -i'' -e's/pve8p/pve4p/g' /usr/bin/pve-fake-subscription
```

#### PVE 3.x

PVE 3.x is supported with minor changes to the script.

Installation with `dpkg -i` will not work because of missing dependencies. Use the following script to install manually:
```shell
# extract the deb package
mkdir -p /tmp/pve-fake-subscription
dpkg-deb -x pve-fake-subscription_*.deb /tmp/pve-fake-subscription

# patch and install the script
sed -i'' -e's/python3/python/g' -e's/pve8p/pve4p/g' /tmp/pve-fake-subscription/usr/bin/pve-fake-subscription
mv /tmp/pve-fake-subscription/usr/bin/pve-fake-subscription /usr/local/bin/

# install the timer
ln -sf /usr/local/bin/pve-fake-subscription /etc/cron.hourly/pve-fake-subscription

# invoke it once
/usr/local/bin/pve-fake-subscription

# remove temporary files
rm -rf /tmp/pve-fake-subscription
```

Removal:
```shell
rm -f /usr/local/bin/pve-fake-subscription /etc/cron.hourly/pve-fake-subscription
```
