import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from network_scanner import scan_network
from device_checker import get_online_devices
from bandwidth_calculator import calculate_bandwidth

ip_range = "192.168.1.1/24"
topology = scan_network(ip_range)
online_devices = get_online_devices(ip_range)
scan_network("192.168.1.1/24")
calculate_bandwidth()