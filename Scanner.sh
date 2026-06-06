#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP> <NSE_SCRIPT>"
    echo "Example: $0 192.168.1.1 http-title"
    exit 1
fi

IP=$1
SCRIPT=$2

echo "===================================="
echo " Nmap NSE Scanner Tool"
echo " Target IP  : $IP"
echo " NSE Script : $SCRIPT"
echo "===================================="

nmap -sV --script=$SCRIPT $IP