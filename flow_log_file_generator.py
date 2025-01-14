#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

def random_ip():
    """Generate a random IPv4 address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_flow_logs(filename="flow_log.txt", num_entries=100000, untagged_ratio=0.3):
    """
    Generate a flow log file with a controlled distribution of tagged and untagged entries.

    :param filename: Output file name (default is 'flow_log.txt').
    :param num_entries: Number of flow log entries to generate (default is 100,000).
    :param untagged_ratio: Proportion of entries that should be untagged (default is 30%).
    """
    # Provided protocols and service mappings
    service_mappings = {
        "web": [(80, "tcp"), (443, "tcp"), (8080, "tcp"), (8443, "tcp"), (8000, "tcp")],
        "ftp": [(20, "tcp"), (21, "tcp")],
        "ssh": [(22, "tcp")],
        "dns": [(53, "udp"), (53, "tcp")],
        "smtp": [(25, "tcp"), (587, "tcp"), (465, "tcp")],
        "http": [(80, "tcp"), (8080, "tcp")],
        "https": [(443, "tcp"), (8443, "tcp")],
        "mysql": [(3306, "tcp")],
        "postgresql": [(5432, "tcp")],
        "redis": [(6379, "tcp")],
        "ldap": [(389, "tcp"), (636, "tcp")],
        "sip": [(5060, "udp"), (5061, "udp")],
        "rdp": [(3389, "tcp")],
        "telnet": [(23, "tcp")],
        "snmp": [(161, "udp"), (162, "udp")],
        "ntp": [(123, "udp")],
        "tftp": [(69, "udp")],
        "dhcp": [(67, "udp"), (68, "udp")],
        "radius": [(1812, "udp")],
        "irc": [(194, "tcp")],
        "xmpp": [(5222, "tcp")],
        "pop3": [(110, "tcp"), (995, "tcp")],
        "imap": [(143, "tcp"), (993, "tcp")],
        "cassandra": [(9042, "tcp")],
        "elasticsearch": [(9200, "tcp")],
        "mongodb": [(27017, "tcp")],
        "memcached": [(11211, "tcp")],
        "zookeeper": [(2181, "tcp")],
        "kafka": [(9092, "tcp")],
        "etcd": [(2379, "tcp")],
        "kubernetes": [(6443, "tcp")],
        "docker": [(2375, "tcp")],
        "jenkins": [(8080, "tcp")],
        "gitlab": [(80, "tcp"), (443, "tcp")],
        "prometheus": [(9090, "tcp")],
        "grafana": [(3000, "tcp")],
        "influxdb": [(8086, "tcp")],
        "syslog": [(514, "udp")],
        "rsync": [(873, "tcp")],
        "nfs": [(2049, "tcp")],
        "samba": [(139, "tcp"), (445, "tcp")],
        "vnc": [(5900, "tcp")],
        "teamviewer": [(5938, "tcp")],
        "x11": [(6000, "tcp")],
    }

    # Extract all known tagged combinations
    tagged_combinations = [
        (dstport, protocol) for ports in service_mappings.values() for dstport, protocol in ports
    ]

    with open(filename, "w", encoding="ascii") as f:
        for _ in range(num_entries):
            version = 2
            account_id = str(random.randint(100000000000, 999999999999))  # 12-digit random account ID
            eni_id = f"eni-{random.randint(1000, 9999):04x}"  # Example ENI ID
            srcaddr = random_ip()
            dstaddr = random_ip()

            # Determine if the entry will be tagged or untagged
            if random.random() < untagged_ratio:
                # Generate an untagged entry (random dstport and protocol)
                dstport = random.randint(1024, 65535)  # Unlikely to match known mappings
                protocol = random.choice(["tcp", "udp", "icmp"])
            else:
                # Generate a tagged entry (from known mappings)
                dstport, protocol = random.choice(tagged_combinations)

            srcport = random.randint(1, 65535)  # Random source port
            packets = random.randint(1, 1000)
            bytes_ = packets * random.randint(50, 1500)  # Rough bytes calculation
            now = int(time.time())
            start = now - random.randint(0, 3600)  # Random time within the last hour
            end = start + random.randint(1, 300)  # Random duration up to 5 minutes
            action = random.choice(["ACCEPT", "REJECT"])  # Random action
            log_status = random.choice(["OK", "NODATA", "SKIPDATA"])  # Random log status

            # Write the flow log entry
            line = (
                f"{version} {account_id} {eni_id} "
                f"{srcaddr} {dstaddr} {srcport} {dstport} {protocol} "
                f"{packets} {bytes_} {start} {end} {action} {log_status}\n"
            )
            f.write(line)

    print(f"Generated {filename} with {num_entries} entries. Untagged ratio: {untagged_ratio*100:.1f}%.")

if __name__ == "__main__":
    # Example: Generate 100,000 flow log entries with 30% untagged
    generate_flow_logs("flow_log.txt", num_entries=80000, untagged_ratio=0.3)


# In[ ]:




