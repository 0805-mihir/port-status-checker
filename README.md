# Port Status Checker

**A Python-Based TCP Port Scanning Utility**

## Project Overview

Port Status Checker is a Python-based network utility developed as part of the **Workora Internship Project**.

The application uses Python socket programming to check the status of TCP ports on a target host. It attempts to establish TCP connections and displays whether each port is OPEN, CLOSED, or FILTERED based on the connection response.

## Project Objective

The main objective of this project is to develop a simple network utility that helps users understand TCP port scanning and socket programming.

The project aims to:

- Check the availability of TCP ports.
- Identify open and closed ports.
- Detect connection timeouts.
- Display port numbers, service names, and their statuses.
- Understand basic network communication using Python sockets.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming Language |
| Socket Library | TCP Connection |
| Sys Library | Program Termination |
| Visual Studio Code | Development Environment |
| TCP Protocol | Network Communication |

## Key Features

- Accepts a target IPv4 address.
- Accepts a starting and ending port number.
- Validates IP address and port range inputs.
- Attempts TCP connections using socket programming.
- Uses a 1-second connection timeout.
- Identifies registered TCP service names.
- Displays port status in a structured table.
- Handles common input and socket errors.

## Working Process

1. The program asks the user to enter a target IP address.
2. It validates the entered IP address.
3. The user enters the starting and ending port numbers.
4. A TCP socket is created for each port.
5. The program attempts to connect to the specified port.
6. The connection response is used to determine the port status.
7. The result is displayed with the port number, service name, and status.
8. The process continues until all specified ports are checked.

## Installation and Execution

### Prerequisites

- Python 3.12 or later
- Visual Studio Code (optional)

### Steps to Run

**1. Clone the repository**

```bash
git clone https://github.com/0805-mihir/port-status-checker.git
```

**2. Open the project directory**

```bash
cd port-status-checker
```

**3. Run the Python program**

```bash
python port_status_checker.py
```

**4. Enter the required inputs**

- Target IP Address
- Starting Port
- Ending Port

## Testing and Results

The application was tested locally using the loopback IP address `127.0.0.1`.

| Port | Service | Status |
|---|---|---|
| 80 | http | CLOSED |
| 8000 | Unknown | OPEN |
| 8001 | Unknown | CLOSED |

### Testing Details

- **Port 80:** Tested when no service was listening on the port.
- **Port 8000:** Tested by starting a temporary Python HTTP server.
- **Port 8001:** Tested when no service was listening on the port.

These tests demonstrate the program's ability to identify different TCP connection responses in a local testing environment.

## Output Screenshots

### 1. Port 80 – CLOSED

![Port 80 CLOSED](Port%2080%20CLOSED.png)

### 2. Port 8000 – OPEN

![Port 8000 OPEN](Port%208000%20OPEN.png)

## Project Structure

```text
port-status-checker/
│
├── port_status_checker.py
├── Port Status Checker Report.pdf
├── Port 80 CLOSED.png
├── Port 8000 OPEN.png
├── Port 8001 CLOSED.png
└── README.md
```

## Limitations

- Supports TCP port scanning only.
- Scans one target IP address at a time.
- Uses a fixed connection timeout of one second.
- Port status detection depends on network and firewall responses.
- Service names are identified using registered TCP port information.

## Future Enhancements

- Add UDP port scanning functionality.
- Support scanning multiple target hosts.
- Allow users to customize connection timeout.
- Generate automatic scan reports.
- Improve filtered-port detection.
- Develop a graphical user interface.

## References

1. [Python Official Documentation](https://docs.python.org/3/)
2. [Python Socket Programming](https://docs.python.org/3/library/socket.html)
3. [Python HTTP Server Documentation](https://docs.python.org/3/library/http.server.html)
4. [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
5. Workora – Project 2: Port Status Checker Guidelines.

## Disclaimer

This project is developed for educational purposes and authorized network testing only. Always obtain proper permission before scanning any network or system.

---

**Developed By:** Mihir Koshti  
**Project Name:** Port Status Checker  
**Internship Platform:** Workora  
**Programming Language:** Python 3.12  
**Year:** 2026
