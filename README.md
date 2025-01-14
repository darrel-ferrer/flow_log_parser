# flow_log_parser
## 1. Overview
This program parses AWS VPC Flow Logs (version 2 only) in the default log format and applies tags to each log entry based on a provided lookup CSV. The output consists of:
* A summary of tag counts.
* A summary of port/protocol combination counts.
## 2. Assumptions
* Generated txt files with data randomly generated based on the examples given. 
* Only supports AWS VPC Flow Logs version 2. Any other version lines are ignored.
* Default log format (fields are space-separated in the order: version, account-id, eni-id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, log-status).
* Protocol is a numeric field in the log (e.g., 6 for TCP, 17 for UDP, 1 for ICMP). If the numeric protocol is unknown, it’s treated as a string.
* The lookup txt contains three columns: dstport, protocol, tag. This is case-insensitive when matching (dstport, protocol) to a tag.
* Entries not found in the lookup table get tagged as "Untagged".
* The file size limit for flow logs is up to 10 MB (based on the requirement), but we do not explicitly check the file size—this is simply a stated assumption for typical usage.
* The lookup file can have up to 10,000 mappings, which we handle in-memory as a Python dictionary.
## 3. Requirements and Dependencies
* Python 3 (tested with Python 3.6+).
* No external libraries. We rely only on built-in Python modules (csv, collections).
## 4. How to Use
Make sure to have both txt and CSV file downloaded and in the same location.
If doing through command prompt navigate to the file location of the python and txt files you downloaded.
* Through command prompt: python flow_parser.py
* Within Jupyter Notebook: Type "!python flow_parser.py" into a a cell and run. Can also run the notebook that is provided in the repository in Jupyter Notebooks.
## 5. Tests Performed
Tested with the sample flow logs with entries such as 
* 2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
* 25,tcp,sv_P1
