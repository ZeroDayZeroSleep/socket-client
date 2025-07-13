import socket
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simple HTTP client CLI tool")
    parser.add_argument("host", help="Target host to connect to")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default 80)")
    args = parser.parse_args()

    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to host and port
        client.connect((args.host, args.port))
        
        # Prepare and send HTTP GET request
        request = f"GET / HTTP/1.1\r\nHost: {args.host}\r\n\r\n"
        client.send(request.encode())
        
        # Receive response
        response = client.recv(4096)
        
        # Print response decoded
        print(response.decode())
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
