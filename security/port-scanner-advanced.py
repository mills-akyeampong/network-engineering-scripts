#!/usr/bin/env python3
"""
Advanced Port Scanner (threaded)
Usage:
    python3 security/port_scanner_advanced.py --target 192.168.1.1 --start 1 --end 1024 --threads 200 --timeout 0.5
"""

import socket
import argparse
import concurrent.futures
import ipaddress
from datetime import datetime

def scan_port(target, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((target, port))
            return port if result == 0 else None
        except Exception:
            return None

def scan_host(target, start, end, threads, timeout, output_file=None):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, target, p, timeout): p for p in range(start, end + 1)}
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)
                print(f"✅ Port {port} is OPEN on {target}")
    open_ports.sort()

    if output_file:
        with open(output_file, "w") as f:
            f.write(f"Scan report for {target} - {datetime.utcnow().isoformat()}Z\n")
            for p in open_ports:
                f.write(f"{p}\n")
    return open_ports

def parse_target(target_str):
    # Accept single IP or CIDR; return list of IPs (strings)
    try:
        if "/" in target_str:
            net = ipaddress.ip_network(target_str, strict=False)
            return [str(ip) for ip in net.hosts()]
        else:
            # Single IP
            ipaddress.ip_address(target_str)
            return [target_str]
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid target: {e}")

def main():
    parser = argparse.ArgumentParser(description="Threaded Advanced Port Scanner (ports 1-1024 by default)")
    parser.add_argument("--target", required=True, help="Target IP or CIDR (e.g., 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("--start", type=int, default=1, help="Start port (default 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default 1024)")
    parser.add_argument("--threads", type=int, default=200, help="Number of threads (default 200)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Socket timeout in seconds (default 0.5)")
    parser.add_argument("--output", help="Optional output file to save open ports")
    args = parser.parse_args()

    targets = parse_target(args.target)
    for tgt in targets:
        print(f"\nScanning {tgt} (ports {args.start}-{args.end}) with {args.threads} threads...")
        open_ports = scan_host(tgt, args.start, args.end, args.threads, args.timeout, args.output)
        if not open_ports:
            print(f"❌ No open ports found on {tgt}")
        else:
            print(f"\nSummary for {tgt}: {len(open_ports)} open ports -> {open_ports}")

if __name__ == "__main__":
    main()
