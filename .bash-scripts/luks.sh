#!/bin/bash

# ---------------------------------------------------------------------------
# A simple shell to mount/unmount luks encrypted partitions disk under Linux.
# Tested on Arch Linux.
# ---------------------------------------------------------------------------
# Written by: Arthur de O. Pereira <https://github.com/Arthoruis/>
# (c) 2019 Arthur de O. Pereira under GNU GPL v.2.0+
# ---------------------------------------------------------------------------
# Last updated: 16/04/2019
# ---------------------------------------------------------------------------

## Commands ##
_crypt="sudo cryptsetup"
_mount="udisksctl mount -b"
_unmount="udisksctl unmount -b"

## Naming the partitions ##
_name="Backup2"
_device1="/dev/sdc2"
_device2="/dev/mapper/Backup2"
_device3="/dev/dm-0"

## Mounting & unmouting the partitins ##
set -e

if grep -qs ${_device2} /proc/mounts; then  ## If is already mounted will search and unmount.
	echo "Unmounting Partition"
	${_unmount} ${_device2}                   ## Unmounting the partition /dev/dm-0.
	echo "Closing Encrypted Backup"
	${_crypt} luksClose ${_name}              ## Closing the encrypted partition /dev/mapper/Backup2
	echo "Encrypted Backup Closed"
	sleep 1
else                                        ## If is not mounted, then will mount.
	echo "Open Encrypted Partition"
	${_crypt} luksOpen ${_device1} ${_name}   ## Open luks encrypted partition.
	echo "Mounting Partition"
	${_mount} ${_device3}                     ## Monting the partition.
	echo "Encrypted Backup Mounted"
	sleep 1
fi
