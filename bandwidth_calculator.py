import psutil
import time

def get_total_bytes():
    total_bytes = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    return total_bytes

def calculate_bandwidth():
    prev_bytes = get_total_bytes()
    prev_time = time.time()
    time.sleep(1)
    current_bytes = get_total_bytes()
    current_time = time.time()
    bandwidth = (current_bytes - prev_bytes) / (current_time - prev_time)
    print(f"Current bandwidth usage: {bandwidth} bytes/sec")
