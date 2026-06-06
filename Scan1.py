import socket
import threading
import time
from queue import Queue

DEFAULT_THREADS = 100
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024


def scan_port(target, port, open_ports, lock):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) != 0:
                return

            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            with lock:
                open_ports.append((port, service))
    except OSError:
        pass


def worker(target, port_queue, open_ports, lock):
    while True:
        port = port_queue.get()
        if port is None:
            port_queue.task_done()
            break

        scan_port(target, port, open_ports, lock)
        port_queue.task_done()


def main():
    target = input("Enter Target IP/Host: ")
    start_port = DEFAULT_START_PORT
    end_port = DEFAULT_END_PORT

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Unable to resolve hostname.")
        return

    port_queue = Queue()
    open_ports = []
    lock = threading.Lock()

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    threads = []
    for _ in range(DEFAULT_THREADS):
        thread = threading.Thread(
            target=worker,
            args=(target_ip, port_queue, open_ports, lock),
            daemon=True,
        )
        thread.start()
        threads.append(thread)

    # signal workers to exit after the queue is empty
    for _ in threads:
        port_queue.put(None)

    start_time = time.time()
    print(f"\nScanning {target} ({target_ip}) from port {start_port} to {end_port}")
    print("-" * 50)

    port_queue.join()

    open_ports.sort()

    print("\nOpen Ports:")
    print("-" * 50)
    if open_ports:
        for port, service in open_ports:
            print(f"{port:<6} {service}")
    else:
        print("No open ports found.")

    print("-" * 50)
    print(f"Open Ports Found: {len(open_ports)}")
    print(f"Scan Time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
