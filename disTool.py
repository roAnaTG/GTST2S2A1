import socket
import ipaddress
import subprocess
import re


def get_local_ip():
    """Get local machine IP (LAN IP)."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def get_gateway():
    """Get default gateway IP."""
    try:
        result = subprocess.check_output("ip route", shell=True).decode()
        gateway = re.search(r"default via (\d+\.\d+\.\d+\.\d+)", result)
        if gateway:
            return gateway.group(1)
    except:
        pass
    return "Unknown"


def get_ip_class(ip):
    """Determine IP class (A, B, C, D, E)."""
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    else:
        return "Class E (Experimental)"


def main():
    print("\n=== HOST DISCOVERY TOOL ===\n")

    local_ip = get_local_ip()
    gateway = get_gateway()
    ip_class = get_ip_class(local_ip)

    print(f"Local IP Address : {local_ip}")
    print(f"Default Gateway  : {gateway}")
    print(f"IP Class         : {ip_class}")

    # Optional: network info
    network = ipaddress.ip_network(local_ip + "/24", strict=False)
    print(f"Network Range    : {network}")


if __name__ == "__main__":
    main()