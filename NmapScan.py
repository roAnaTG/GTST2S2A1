import nmap
import time
import socket
from datetime import datetime


def validate_target(target):
    try:
        socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False


def run_scan(target):
    scanner = nmap.PortScanner()

    print("\n" + "=" * 70)
    print("NMAP SCANNER")
    print("=" * 70)

    print(f"Target      : {target}")
    print(f"Started At  : {datetime.now()}")
    print("-" * 70)

    start_time = time.perf_counter()

    scanner.scan(
        hosts=target,
        ports="1-65535",
        arguments="-T4 -sV -O"
    )

    scan_time = time.perf_counter() - start_time

    return scanner, scan_time


def display_results(scanner, scan_time):

    if not scanner.all_hosts():
        print("No hosts discovered.")
        return

    for host in scanner.all_hosts():

        print("\n" + "=" * 70)
        print(f"Host       : {host}")
        print(f"Hostname   : {scanner[host].hostname()}")
        print(f"Status     : {scanner[host].state()}")

        if 'osmatch' in scanner[host]:
            try:
                os_name = scanner[host]['osmatch'][0]['name']
                print(f"Operating System : {os_name}")
            except:
                pass

        print("=" * 70)

        for proto in scanner[host].all_protocols():

            print(f"\nProtocol: {proto.upper()}")
            print("-" * 70)

            print(
                f"{'PORT':<10}"
                f"{'STATE':<10}"
                f"{'SERVICE':<20}"
                f"{'PRODUCT'}"
            )

            print("-" * 70)

            ports = sorted(scanner[host][proto].keys())

            for port in ports:

                info = scanner[host][proto][port]

                state = info.get("state", "")
                service = info.get("name", "")
                product = info.get("product", "")
                version = info.get("version", "")

                print(
                    f"{port:<10}"
                    f"{state:<10}"
                    f"{service:<20}"
                    f"{product} {version}"
                )

    print("\n" + "=" * 70)
    print(f"Scan completed in {scan_time:.2f} seconds")
    print("=" * 70)


def main():

    target = input("Enter Target IP or Hostname: ").strip()

    if not validate_target(target):
        print("Invalid hostname or IP address.")
        return

    try:
        scanner, scan_time = run_scan(target)
        display_results(scanner, scan_time)

    except KeyboardInterrupt:
        print("\nScan cancelled by user.")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()