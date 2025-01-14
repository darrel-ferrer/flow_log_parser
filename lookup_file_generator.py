#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import csv

def generate_tags(num_tags=10000, output_file="lookup.csv", known_port_ratio=0.8):
  """
  Generates a list of tags based on dstport and protocol, 
  mapping common ports to their associated services with a specified ratio 
  of known to unknown port combinations.

  Args:
    num_tags: The number of tags to generate.
    output_file: The name of the output CSV file.
    known_port_ratio: The desired ratio of known ports to total ports (between 0 and 1).

  Returns:
    None
  """

  tags = set()
  protocols = ["tcp", "udp", "icmp"]
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
      "telnet": [(23, "tcp")], 
      "ftp": [(20, "tcp"), (21, "tcp")], 
      "tftp": [(69, "udp")], 
      "ssh": [(22, "tcp")], 
      "scp": [(22, "tcp")], 
      "rsync": [(873, "tcp")], 
      "sftp": [(22, "tcp")], 
      "http": [(80, "tcp"), (8080, "tcp")], 
      "https": [(443, "tcp"), (8443, "tcp")], 
      "dns": [(53, "udp"), (53, "tcp")], 
      "ntp": [(123, "udp")], 
      "snmp": [(161, "udp"), (162, "udp")], 
      "ldap": [(389, "tcp"), (636, "tcp")], 
      "imap": [(143, "tcp"), (993, "tcp")], 
      "pop3": [(110, "tcp"), (995, "tcp")], 
      "smtp": [(25, "tcp"), (587, "tcp"), (465, "tcp")], 
      "xmpp": [(5222, "tcp")], 
      "sip": [(5060, "udp"), (5061, "udp")], 
      "rdp": [(3389, "tcp")], 
      "vnc": [(5900, "tcp")], 
      "mysql": [(3306, "tcp")], 
      "postgresql": [(5432, "tcp")], 
      "mongodb": [(27017, "tcp")], 
      "redis": [(6379, "tcp")], 
      "elasticsearch": [(9200, "tcp")], 
      "kafka": [(9092, "tcp")], 
      "zookeeper": [(2181, "tcp")], 
      "etcd": [(2379, "tcp")], 
      "kubernetes": [(6443, "tcp")], 
      "docker": [(2375, "tcp")], 
      "jenkins": [(8080, "tcp")], 
      "gitlab": [(80, "tcp"), (443, "tcp")], 
      "prometheus": [(9090, "tcp")], 
      "grafana": [(3000, "tcp")], 
      "influxdb": [(8086, "tcp")], 
      "syslog": [(514, "udp")], 
      "nfs": [(2049, "tcp")], 
      "samba": [(139, "tcp"), (445, "tcp")], 
      "teamviewer": [(5938, "tcp")], 
      "x11": [(6000, "tcp")], 
  }

  known_port_count = int(num_tags * known_port_ratio)
  unknown_port_count = num_tags - known_port_count
  print(known_port_count)
  print(unknown_port_count)

  with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['dstport', 'protocol', 'tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate known port tags
    i=1
    while i < known_port_count:
      service = random.choice(list(service_mappings.keys()))
      port_protocol = random.choice(service_mappings[service]) 
      dstport, protocol = port_protocol
      tag = f"{service}"
      writer.writerow({'dstport': dstport, 'protocol': protocol, 'tag': tag})
      i = i+1


    # Generate unknown port tags
    while i < num_tags:
      dstport = random.randint(1, 65535)  # Generate any random port
      protocol = random.choice(protocols)
      tag = f"unknown_{dstport}_{protocol}"
      tags.add(tag)
      writer.writerow({'dstport': dstport, 'protocol': protocol, 'tag': tag})
      i = i+1


if __name__ == "__main__":
   generate_tags()
   print(f"Generated tags written to lookup.csv")       


# In[ ]:




