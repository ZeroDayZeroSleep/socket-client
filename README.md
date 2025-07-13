httpclient  
A simple command-line HTTP client tool built in Python for sending HTTP GET and POST requests.

# Features
  Send HTTP GET and POST requests from the command line
  Specify target hostname and port
  Add custom HTTP headers
  Send data with POST requests
  Save server responses to a file
  Simple, intuitive commands and options

# Installation
Make sure you have Python 3 installed.
Clone this repository or download the simple_http_client.py script.
(Optional) Add the script to your PATH or create an alias for easy use.

# Usage
bash
python simple_http_client.py [command] hostname [options]

# Commands
 get (default): Send an HTTP GET request
 post: Send an HTTP POST request (requires --data)

# Options
 -p, --port: Target port (default: 80)
 -H, --header: Add HTTP headers (can be used multiple times)
 -d, --data: Data to send with POST requests
 -o, --output: Save response to a file instead of printing

# Examples

- Send a GET request to www.google.com on port 80:
bash
  python simple_http_client.py get www.google.com

- Send a GET request with a custom User-Agent header:
bash
  python simple_http_client.py get www.google.com -H "User-Agent: CustomClient/1.0"

Send a POST request with JSON data:
bash
  python simple_http_client.py post api.example.com -d '{"name":"ChatGPT"}' -H "Content-Type: application/json"

Save the response to a file:
bash
  python simple_http_client.py get www.google.com -o response.html

  
# Notes
POST requests require the --data (-d) option.

Multiple headers can be added by specifying -H multiple times.

The tool currently supports basic HTTP/1.1 requests.

License
This project is based on code from Hacking with Python by Justin Seitz with written permission.

BASIC CODE FROM "HACKING WITH PYTHON" BY JUSTIN SEITZ:

        import socket
        #Zielhost und Port
        target_host = "www.google.com"
        target_port = 80
        
        #Socket-Objekt erzeugen (AF_INET = IPv4, SOCK_STREAM = TCP)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Verbindung mit dem Zielserver herstellen
        client.connect((target_host, target_port))
        
        #HTTP GET-Anfrage senden
        client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        
        #Antwort vom Server empfangen
        response = client.recv(4096)
        
        #Antwort ausgeben
        print(response.decode())


