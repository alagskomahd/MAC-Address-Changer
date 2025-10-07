#!/usr/bin/env python

# Importing modules
import subprocess
import argparse
import re

# Writing a function to get arguments from the user
def get_arguments():
    parser = argparse.ArgumentParser(description="getting arguments from the user to change the MAC address of an interface")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="new MAC address")
    args = parser.parse_args()
    return args

# Writing a function to check the current MAC address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")
    return None

# Writing a function to change the MAC address of an interface
def mac_changer(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Calling the function for the argument parser
options = get_arguments()

# Calling the function for the MAC address search result
current_mac = get_current_mac(options.interface)
print(f"Current MAC address = {current_mac}")

# Calling the function for the MAC address changer
mac_changer(options.interface, options.new_mac)

# Performing checks to see if MAC address actually got changed
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac}")
else:
    print("[-] MAC address did not change")

