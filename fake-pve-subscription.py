#!/usr/bin/env python3
# Pollute Proxmox VE 5.x subscription cache so it won't alert you on dashboard login
# If you need to prevent it checking keys against a server, please block "shop.maurer-it.com"
import hashlib
import base64
import json
import time
import re
import sys
from typing import List

# a 8-socket fake key which should be good for all situations
key = "pve8p-1145141919"

# key format
# /usr/share/perl5/PVE/API2/Subscription.pm
subscription_pattern = r'pve([1248])([cbsp])-[0-9a-f]{10}'

# /usr/share/perl5/PVE/Subscription.pm
shared_key_data = "kjfdlskfhiuewhfk947368"

server_key_file = "/etc/ssh/ssh_host_rsa_key.pub"
subscription_file = "/etc/subscription"

def get_timestamp():
    return int(time.time())

# perl's md5_base64 implementation
def md5_base64(x: str) -> str: 
    return base64.b64encode(hashlib.md5(x.encode()).digest()).strip(b'=')

def generate_server_id(key: str) -> str:
    return hashlib.md5(key.encode()).hexdigest().upper()

def generate_subscription(key: str, server_ids: List[str]) -> str:
    localinfo = {
        "checktime": get_timestamp(),
        "status": "Active",
        "key": key,
        "validdirectory": ",".join(server_ids),
        "productname": "YajuuSenpai",
        "regdate": get_timestamp(),
        "nextduedate": 2147483647,
    }

    data = base64.standard_b64encode(json.dumps(localinfo).encode()).decode()
    cat = str(localinfo["checktime"]) + data + "\n" + shared_key_data
    csum = md5_base64(cat).decode()

    return key + "\n" + csum + "\n" + data + "\n"

if __name__ == "__main__":
    # check if the key format is correct
    pattern = re.compile(subscription_pattern)
    if not pattern.match(key):
        print("key format error", file=sys.stderr)
        sys.exit(1)

    # get machine ID
    server_id = ""
    with open(server_key_file, "r") as f:
        server_id = generate_server_id(f.read())

    # generate a license file
    subscription = generate_subscription(key, [server_id])

    # write license file
    with open(subscription_file, "w") as f:
        f.write(subscription)
