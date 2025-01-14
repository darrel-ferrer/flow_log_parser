# README: VPC Flow Log Parser

## Overview

This project consists of three main components designed to generate and parse AWS-like VPC Flow Logs for analysis. The system supports tagging traffic based on destination ports and protocols using a lookup table and provides insights into tagged and untagged traffic.

### Main Components

1. **Flow Log File Generator** (`flow_log_file_generator.ipynb`)
   - Generates flow logs with a mix of tagged and untagged entries based on a controlled ratio.
   - Simulates realistic traffic using known service mappings (e.g., HTTP, SSH).

2. **Lookup File Generator** (`lookup_file_generator.ipynb`)
   - Creates a lookup table mapping `dstport` and `protocol` to `tag`.
   - Supports generating entries for common services (e.g., `web`, `ssh`) and random unknown mappings.

3. **Flow Log Parser** (`flow_parser.ipynb`)
   - Parses flow logs and maps them to tags based on the lookup table.
   - Outputs counts of tagged and untagged traffic and a breakdown of port/protocol usage.

---

## Assumptions

- **Flow Log Format**: Only supports AWS VPC Flow Log **version 2**.
- **Lookup Table**:
  - Generated with a mix of common services and random unknown mappings.
  - Format: `dstport,protocol,tag`.
- **Tagged/Untagged Ratio**:
  - Controlled during flow log generation via the `untagged_ratio` parameter.
- **Dependencies**:
  - No external libraries are required beyond Python's standard library.

---

## File Details

### 1. **Flow Log File Generator**
- **File**: `flow_log_file_generator.ipynb`
- **Purpose**: Generates synthetic flow logs with a configurable mix of tagged and untagged traffic.
- **Key Parameters**:
  - `num_entries`: Number of flow log entries to generate.
  - `untagged_ratio`: Proportion of untagged traffic (e.g., `0.3` for 30% untagged).
- **Output**:
  - A text file (`flow_log.txt`) with flow log entries.
- **Usage**:
  ```python
  generate_flow_logs(filename="flow_log.txt", num_entries=80000, untagged_ratio=0.3)
  ```

### 2. **Lookup File Generator**
- **File**: `lookup_file_generator.ipynb`
- **Purpose**: Generates a lookup table mapping `dstport` and `protocol` to `tag`.
- **Key Parameters**:
  - `num_tags`: Number of mappings to generate.
  - `known_port_ratio`: Ratio of known ports to total ports.
- **Output**:
  - A CSV file (`lookup.csv`) containing the lookup table.
- **Usage**:
  ```python
  generate_tags(num_tags=10000, output_file="lookup.csv", known_port_ratio=0.8)
  ```

### 3. **Flow Log Parser**
- **File**: `flow_parser.ipynb`
- **Purpose**: Parses flow logs and applies tags based on the lookup table.
- **Outputs**:
  - **Tag Counts**: Number of occurrences for each tag.
  - **Port/Protocol Counts**: Frequency of each destination port/protocol combination.
- **Usage**:
  - Update `flow_log_file` and `lookup_csv_file` variables in the script:
    ```python
    flow_log_file = 'flow_log.txt'
    lookup_csv_file = 'lookup.csv'
    main(flow_log_file, lookup_csv_file)
    ```

---

## Instructions

### Step 1: Generate the Lookup Table
1. Open `lookup_file_generator.ipynb`.
2. Run the script to create a lookup table:
   ```python
   generate_tags(num_tags=10000, output_file="lookup.csv", known_port_ratio=0.8)
   ```
3. Verify `lookup.csv` is created with the expected format:
   ```
   dstport,protocol,tag
   80,tcp,web
   443,tcp,web
   3306,tcp,mysql
   ```

### Step 2: Generate Flow Logs
1. Open `flow_log_file_generator.ipynb`.
2. Run the script to generate flow logs:
   ```python
   generate_flow_logs(filename="flow_log.txt", num_entries=100000, untagged_ratio=0.3)
   ```
3. Verify `flow_log.txt` is created with the expected format:
   ```
   2 123456789012 eni-1234 192.168.1.1 203.0.113.1 49152 80 tcp 25 12500 1673654487 1673654590 ACCEPT OK
   2 987654321098 eni-5678 10.0.0.5 198.51.100.10 32768 443 tcp 50 75000 1673654387 1673654430 REJECT OK
   ```

### Step 3: Parse Flow Logs
1. Open `flow_parser.ipynb`.
2. Run the script with the generated files:
   ```python
   flow_log_file = 'flow_log.txt'
   lookup_csv_file = 'lookup.csv'
   main(flow_log_file, lookup_csv_file)
   ```
3. Check the output in the terminal or notebook.

---

## Example Outputs

### Tag Counts
```
Tag,Count
Untagged,30000
web,25000
ssh,10000
dns,5000
mysql,10000
```

### Port/Protocol Counts
```
Port,Protocol,Count
22,tcp,10000
53,udp,5000
80,tcp,15000
443,tcp,10000
3306,tcp,10000
```

---

## Tests and Validation

1. **Lookup File**:
   - Verified known ports are tagged correctly.
   - Checked random mappings for realistic distribution.
2. **Flow Log File**:
   - Ensured tagged/untagged ratio matches `untagged_ratio`.
   - Checked logs for realistic port, protocol, and timestamp values.
3. **Parser**:
   - Validated tag and port/protocol counts against expected distribution.
