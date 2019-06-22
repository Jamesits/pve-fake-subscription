#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

fpm -s dir -t deb \
	-n pve-fake-subscription \
	--description "Pollute Proxmox VE 5.x subscription cache so it won't alert you on dashboard login" \
	--url "https://github.com/Jamesits/pve-fake-subscription" \
	-v 0.0.2 \
	--license "GLWTS(Good Luck With That Shit) Public License" \
	--depends "python3" \
	--architecture all \
	--deb-dist "unstable" \
	--deb-priority "optional" \
	--deb-systemd "usr/lib/systemd/system/pve-fake-subscription.timer" \
	./usr

