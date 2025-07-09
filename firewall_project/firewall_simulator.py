# -------------------------------
# Interactive Firewall Simulator
# -------------------------------

allowed_ips = ['192.168.1.1', '10.0.0.2']
blocked_ips = ['192.168.0.10', '172.16.0.5']
allowed_ports = [80, 443]
blocked_ports = [21, 23]

log_file = "firewall_log.txt"

def simulate_packet(ip, port):
    if ip in blocked_ips:
        return f"Blocked: IP {ip} is blacklisted"
    elif port in blocked_ports:
        return f"Blocked: Port {port} is blacklisted"
    elif ip in allowed_ips or port in allowed_ports:
        return f"Allowed: IP {ip}, Port {port}"
    else:
        return f"Unknown: No rule for IP {ip}, Port {port}"

def log_result(ip, port, result):
    with open(log_file, "a") as log:
        log.write(f"{ip}:{port} - {result}\n")

def show_rules():
    print("\n--- Current Firewall Rules ---")
    print("Allowed IPs   :", allowed_ips)
    print("Blocked IPs   :", blocked_ips)
    print("Allowed Ports :", allowed_ports)
    print("Blocked Ports :", blocked_ports)

def add_allowed():
    choice = input("Add (1) IP or (2) Port to Allowed list? ")
    if choice == '1':
        ip = input("Enter IP to allow: ")
        if ip not in allowed_ips:
            allowed_ips.append(ip)
            print(f"IP {ip} added to allowed list.")
    elif choice == '2':
        try:
            port = int(input("Enter Port to allow: "))
            if port not in allowed_ports:
                allowed_ports.append(port)
                print(f"Port {port} added to allowed list.")
        except ValueError:
            print("Invalid port number.")

def add_blocked():
    choice = input("Add (1) IP or (2) Port to Blocked list? ")
    if choice == '1':
        ip = input("Enter IP to block: ")
        if ip not in blocked_ips:
            blocked_ips.append(ip)
            print(f"IP {ip} added to blocked list.")
    elif choice == '2':
        try:
            port = int(input("Enter Port to block: "))
            if port not in blocked_ports:
                blocked_ports.append(port)
                print(f"Port {port} added to blocked list.")
        except ValueError:
            print("Invalid port number.")

def check_packet():
    ip = input("Enter incoming IP address: ")
    try:
        port = int(input("Enter incoming port: "))
        result = simulate_packet(ip, port)
        print(result)
        log_result(ip, port, result)
    except ValueError:
        print("Invalid port number.")

def start_firewall():
    while True:
        print("\n=== Firewall Menu ===")
        print("1. Check Packet")
        print("2. Add Allowed IP/Port")
        print("3. Add Blocked IP/Port")
        print("4. Show Current Rules")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            check_packet()
        elif choice == '2':
            add_allowed()
        elif choice == '3':
            add_blocked()
        elif choice == '4':
            show_rules()
        elif choice == '5':
            print("Exiting Firewall Simulator. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Start the simulator
start_firewall()
