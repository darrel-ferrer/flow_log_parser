#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def generate_random_lookup_table(filename="lookup_random.txt", num_entries=100):
    # Pool of realistic and additional tags
    tags_pool = [
        "SSH", "HTTP", "HTTPS", "SMTP", "POP3", "IMAP", "DNS", "RDP", "TELNET", "TFTP",
        "SNMP", "ICMP", "sv_P1", "sv_P2", "sv_P3", "sv_P4", "sv_P5", "email"
    ]

    with open(filename, "w", encoding="ascii") as f:
        for _ in range(num_entries):
            # Generate random values for dstport, protocol, and tag
            dstport = random.randint(1, 65535)  # Random port between 1 and 65535
            protocol = random.choice(["tcp", "udp", "icmp"])  # Random protocol
            tag = random.choice(tags_pool)  # Random tag from the pool
            f.write(f"{dstport},{protocol},{tag}\n")

    print(f"Generated {filename} with {num_entries} random entries.")

if __name__ == "__main__":
    # Example: Generate a lookup table with 100 entries
    generate_random_lookup_table("lookup.txt", num_entries=10000)


# In[ ]:




