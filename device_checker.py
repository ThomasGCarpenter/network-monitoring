import ping3
import ipaddress
from network_scanner import scan_network

def get_online_devices(ip_range):
    topology = scan_network(ip_range)
    online_devices = []
    for mac, device in topology.items():
        ip = device['ip']
        hostname = device['name']
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print(f"Invalid IP address: {ip}")
            continue
        response_time = ping3.ping(ip, timeout=1)
        if response_time is not None:
            online_devices.append((ip, hostname, response_time))
            print(f"Device {ip} ({hostname}) is online (response time: {response_time} ms)")
    if not online_devices:
        print("No devices are currently online.")
    return online_devices
