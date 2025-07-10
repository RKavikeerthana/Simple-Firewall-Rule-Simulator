# 🔒 Simple Firewall Rule Simulator
This is a Python-based beginner-level project that simulates a basic firewall. It allows or blocks incoming "packets" based on predefined IP addresses and port number rules, helping users understand how basic firewall filtering works.

## 📁 Project Structure
```
firewall_simulator.py        # Main Python script
README.md                    # Project documentation
```
## 📌 What the Project Does
This project simulates a simple firewall system. It does not connect to the internet or handle real packets, but instead asks the user to input:

An IP address

A port number

Based on rules defined in the script, it decides whether the packet is:

✅ Allowed

❌ Blocked

⚠️ Unknown (no matching rule)

Every action is recorded in a log file.

## 🛠️ Steps I Implemented
### 1. Defined Firewall Rules
In the script, I used Python lists to define:

allowed_ips – IP addresses that are permitted

blocked_ips – IPs that should be denied access

allowed_ports – safe ports like 80 (HTTP), 443 (HTTPS)

blocked_ports – insecure ports like 21 (FTP), 23 (Telnet)

### 2. Created the simulate_packet() Function
This function checks whether a given IP or port is in the allowed or blocked lists and returns the appropriate result.

### 3. Added Logging
I used file handling in Python to write each result into a file called firewall_log.txt for audit and tracking.

### 4. Developed an Interactive Menu
To make the program user-friendly, I added a loop with menu options like:

Check packet status

Add allowed IP or port

Add blocked IP or port

View current rules

Exit the firewall

### 5. Improved Code Structure
I organized everything into separate functions like:

add_allowed()

add_blocked()

show_rules()

check_packet()



## Output:
### 1. Check Packet Status
Displays whether an incoming IP and port combination is allowed, blocked, or unknown based on the firewall's predefined rules.


![option 1](https://github.com/user-attachments/assets/330f83ee-cbff-416d-96ca-0bedb2fc48dd)


### 2. Add Allowed IP or Port
Lets the user add new trusted IP addresses or ports to the allowed list. Once added, traffic from those IPs or to those ports will be accepted by the firewall.


![option 2](https://github.com/user-attachments/assets/43e67c0c-769b-4c3e-ab2d-8aa8d33819bf)

### 3. Add Blocked IP or Port
Allows the user to block specific IP addresses or ports by adding them to the blocked list. After blocking, any matching incoming traffic will be denied

![option 3](https://github.com/user-attachments/assets/f82115a8-b7c6-4395-9c16-f5acb4db0bbe)


### 4. Show Current Rules
Displays the current configuration of the firewall, including all allowed and blocked IP addresses and ports. This helps users review and manage the active rule sets.

![option 4](https://github.com/user-attachments/assets/cee6fbc9-6ef0-4c6a-8648-d680f29e8fbb)


### 5. Exit the Firewall
Safely terminates the program and exits the firewall simulator interface.


![option 5](https://github.com/user-attachments/assets/2522cb3d-ac03-4edc-9ac3-acd8b60016f7)


## 🧠 What I Learned
How firewall filtering rules work using IPs and ports

Python basics: input/output, lists, functions, file handling

Logging activity just like in real firewall systems

Interactive command-line application development
