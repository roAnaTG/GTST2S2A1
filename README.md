# GTST2S2A1

Last updated: June 6, 2026

Welcome! This repository includes four small tools for the assignment, each written to match one of the tasks below.

1. `Scan1.py` - A Python port scanner built without using the `nmap` module.
2. `NmapScan.py` - A port scanner that uses the `python-nmap` module.
3. `disTool.py` - A host discovery helper that finds the gateway IP and IP class.
4. `Scanner.sh` - A Bash script that takes an IP address and an NSE script name, then runs an `nmap` scan.

## What each file does

### `Scan1.py`
This is the simple port scanner built with Python sockets and threads.
- Scans ports from `1` to `1024`.
- Resolves the target name to an IP address.
- Tries TCP connections and reports which ports are open.
- Looks up common service names for open ports when available.

### `NmapScan.py`
This version uses the `python-nmap` library.
- Asks for a target IP or hostname.
- Validates the target before scanning.
- Runs an Nmap scan on all ports (`1-65535`) with service/version detection and OS detection.
- Prints the host status, open ports, and service details.

### `disTool.py`
A host discovery tool written in Python.
- Finds your local machine IP address.
- Determines the default gateway IP.
- Identifies the IP class (A, B, C, D, or E).
- Shows the local network range.

### `Scanner.sh`
A Bash helper for running Nmap NSE scripts.
- Accepts two arguments: `IP` and `NSE_SCRIPT`.
- Runs `nmap -sV --script=<NSE_SCRIPT> <IP>`.
- Example: `./Scanner.sh 192.168.1.1 http-title`

## Assignment mapping

- Question 1: `Scan1.py` — port scanner without `nmap`.
- Question 2: `NmapScan.py` — port scanner using `nmap`.
- Question 3: This `README.md` explains the tools and their `nmap` usage.
- Question 4: `disTool.py` — host discovery, gateway IP, and IP class.
- Question 5: `Scanner.sh` — Bash tool for running an NSE script with `nmap`.
