import nmap
import logging

logger = logging.getLogger(__name__)

def scan_network(ip_range):
    try:
        #instance of nmap.PortScanner is created to perform network scan
        nm = nmap.PortScanner()
        # Calls scan method of PortScanner object, -sP arg performs ping scan and -n disables reverse DNS resolution.
        nm.scan(hosts=ip_range, arguments='-sP -n')
        topology = {}
        # all_hosts  retrieves list of all hosts that were discovered during the scan.
        # loop over each host, and check if host has MAC address.
        for host in nm.all_hosts():
            if 'mac' in nm[host]['addresses']:
                mac = nm[host]['addresses']['mac']
                #  If yes, MAC address becomes key in topology dict
                topology[mac] = {
                    'ip': nm[host]['addresses']['ipv4'],
                    'name': nm[host]['hostnames'][0]['name'] if 'hostnames' in nm[host] and len(nm[host]['hostnames']) > 0 else '',
                    'vendor': nm[host]['vendor'][mac] if 'vendor' in nm[host] and mac in nm[host]['vendor'] else ''
                }
        logger.info("Network Topology:")
        logger.info(topology)
        return topology
    except Exception as e:
        logger.error("Error occurred during network scanning: %s", e)
        return None
