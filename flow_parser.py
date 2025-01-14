#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from collections import defaultdict


# In[2]:


# Common protocol number -> name mappings
# Extend if you expect other protocols
PROTO_MAP = {
    6: "tcp",
    17: "udp",
    1: "icmp",
}


# In[3]:


def load_lookup_table(lookup_csv_path):
    lookup = {}
    with open(lookup_csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # Each valid line should have at least 3 fields
            if len(row) < 3:
                continue
            dstport_str, proto_str, tag = row
            # Make it case-insensitive by lowercasing the keys
            key = (dstport_str.strip().lower(), proto_str.strip().lower())
            lookup[key] = tag.strip()
    return lookup

def parse_flow_log_line(line):
    parts = line.strip().split()
    # Check the number of fields to be a valid version 2 log line if not enough return None
    if len(parts) < 14:
        return None

    try:
        version = int(parts[0])
    except ValueError:
        # If the version is not an integer, skip
        return None
    # We only handle version 2 logs in this script
    if version != 2:       
        return None

    # Extract needed fields
    dst_port_str = parts[6]
    proto_num_str = parts[7]

    # Convert protocol number to text (tcp/udp/icmp) if known
    try:
        proto_num = int(proto_num_str)
        protocol_str = PROTO_MAP.get(proto_num, str(proto_num))
    except ValueError:
        protocol_str = proto_num_str  # fallback: raw string if not an integer

    return {
        "dstport": dst_port_str,
        "protocol": protocol_str,
    }


# In[4]:


def main(flow_log_path, lookup_csv_path):
    # 1. Load lookup table
    lookup_dict = load_lookup_table(lookup_csv_path)

    # 2. Prepare counters
    tag_counts = defaultdict(int)         # tag -> count
    port_proto_counts = defaultdict(int)  # (dstport, protocol) -> count

    # 3. Read and parse the flow logs
    with open(flow_log_path, "r", encoding="utf-8") as f:
        for line in f:
            # Skip empty lines
            if not line.strip():
                continue

            parsed = parse_flow_log_line(line)
            if not parsed:
                continue  # skip invalid lines or non-version-2 lines

            # Standardize and pull out fields
            dstport = parsed["dstport"].strip()
            protocol = parsed["protocol"].strip().lower()  # ensure case-insensitive

            # Keep track of (dstport, protocol) count
            port_proto_key = (dstport, protocol)
            port_proto_counts[port_proto_key] += 1

            # Look for a tag in the lookup dict
            lookup_key = (dstport.lower(), protocol.lower())
            if lookup_key in lookup_dict:
                tag = lookup_dict[lookup_key]
            else:
                tag = "Untagged"

            # Increment the tag count
            tag_counts[tag] += 1

    # 4. Print results

    # --- Tag Counts ---
    print("Tag Counts:")
    print("Tag,Count")
    for tag, cnt in sorted(tag_counts.items()):
        print(f"{tag},{cnt}")
    print()  # blank line between sections

    # --- Port/Protocol Combination Counts ---
    print("Port/Protocol Combination Counts:")
    print("Port,Protocol,Count")
    for (port, proto), cnt in sorted(port_proto_counts.items()):
        print(f"{port},{proto},{cnt}")


# In[5]:


if __name__ == "__main__":

    flow_log_file = 'flow_log.txt'
    lookup_csv_file = 'lookup.csv'
    main(flow_log_file, lookup_csv_file)

