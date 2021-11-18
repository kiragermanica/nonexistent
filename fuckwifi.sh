#!/bin/bash
echo "[+] Choose mode(Monitor,Manage):"
read mode
if [[ "$mode" == "Monitor" ]]
then
	sudo mv /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin.manage
	sudo mv /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin.monitor /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin
	sudo service NetworkManager stop
	sudo modprobe -r ath10k_pci
        sudo modprobe -r ath10k_core
	sudo modprobe ath10k_core rawmode=1 cryptmode=1
	sudo modprobe ath10k_pci
	sleep 2
	sudo airmon-ng start wlan0
else
	sudo airmon-ng stop wlan0mon
	sudo mv /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin.monitor
	sudo mv /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin.manage /lib/firmware/ath10k/QCA6174/hw3.0/firmware-6.bin
	sudo service NetworkManager stop
	sudo modprobe -r ath10k_pci
        sudo modprobe -r ath10k_core
	sudo modprobe ath10k_core rawmode=0 cryptmode=0
	sudo modprobe ath10k_pci
	sudo service NetworkManager start
fi
echo "[+] Done! Mode: $mode"
