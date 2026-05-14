
#!/bin/bash

# This script performs basic apt mantainance:
# It removes unused dependencies
# Updates the package database
# Upgrades all installed packages

# Check whether the script is being run as root.

if [ "$EUID" -ne 0 ]; then
	echo "Please run this script with sudo as root."
	exit 1
fi

echo "Removing unused dependencies..."
apt autoremove -y

echo "Updating package database..."
apt update

echo "Upgarding installed package..."
apt upgrade -y

echo "System maintanaince complete."
