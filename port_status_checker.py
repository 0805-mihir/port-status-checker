
import socket
import sys

print("===================================")
print("       PORT STATUS CHECKER")
print("===================================")

# Step 1: Take and validate target IP address
target = input("Enter Target IP Address: ")

try:
    socket.inet_aton(target)
except OSError:
    print("Invalid IP Address!")
    sys.exit()

# Step 2: Take port range
try:
    start_port = int(input("Enter Starting Port: "))
    end_port = int(input("Enter Ending Port: "))
except ValueError:
    print("Please enter valid port numbers!")
    sys.exit()

# Step 3: Validate port range
if start_port < 1 or end_port > 65535:
    print("Port numbers must be between 1 and 65535!")
    sys.exit()

if start_port > end_port:
    print("Starting port cannot be greater than ending port!")
    sys.exit()

print("\nScanning Started...\n")

print("{:<12} {:<20} {}".format("PORT", "SERVICE", "STATUS"))
print("------------------------------------------")

# Step 4: Scan each port
for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        result = s.connect_ex((target, port))

        # Get service name
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        if result == 0:
            status = "OPEN"

        elif result == 10060:
            status = "FILTERED"

        else:
            status = "CLOSED"

        print("{:<12} {:<20} {}".format(port, service, status))

    except socket.timeout:
        print("{:<12} {:<20} {}".format(port, "Unknown", "FILTERED"))

    except OSError:
        print("{:<12} {:<20} {}".format(port, "Unknown", "FILTERED"))

    finally:
        s.close()

print("\nScanning Completed!")
print("===================================")
