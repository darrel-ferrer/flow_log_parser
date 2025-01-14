#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import time

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_flow_log_file(filename="flow_log.txt", num_entries=100000):
    actions = ["ACCEPT", "REJECT"]
    log_statuses = ["OK", "NODATA", "SKIPDATA"]
    protocols = [1, 6, 17]  # ICMP(1), TCP(6), UDP(17)

    with open(filename, "w", encoding="ascii") as f:
        for _ in range(num_entries):
            version = 2
            account_id = str(random.randint(100000000000, 999999999999))
            eni_id = f"eni-{random.randint(1000, 9999):04x}"
            srcaddr = random_ip()
            dstaddr = random_ip()
            srcport = random.randint(1, 65535)
            dstport = random.randint(1, 65535)
            protocol = random.choice(protocols)
            packets = random.randint(1, 1000)
            bytes_ = packets * random.randint(50, 1500)
            now = int(time.time())
            start = now - random.randint(0, 3600)
            end = start + random.randint(0, 300)
            action = random.choice(actions)
            log_status = random.choice(log_statuses)

            line = (
                f"{version} {account_id} {eni_id} "
                f"{srcaddr} {dstaddr} {srcport} {dstport} {protocol} "
                f"{packets} {bytes_} {start} {end} {action} {log_status}\n"
            )
            f.write(line)
    print(f"Generated {filename} with {num_entries} entries.")
# Generate the flow log file
generate_flow_log_file("flow_log.txt", num_entries=100000)


# In[ ]:




