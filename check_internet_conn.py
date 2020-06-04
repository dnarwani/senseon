import socket

def main():
    """
        Main function to call
    """
    test_connection()
    check_port_80()

def test_connection(host="8.8.8.8", port=53, timeout=5):
    """
        This function checks if an internet connection can be established from your host with a fixed timeout=5.
        If not it will report an error and a fix.
    """
    try: 
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        
        print("Internet is connected")
        return True
    except socket.error as e:
        print(e)
        print("Please allow outbound traffic from your host")
        return False

def check_port_80(host="www.google.com", port=80, timeout=5):
    """
        This function checks if your host can connect to port 80 with a fixed timeout=5.
        If not it will report an error and a fix.
    """
    try: 
        s = socket.create_connection((host, port), timeout)
        s.close()

        print("Port 80 is Open")
        return True
    except socket.error as e:
        print(e)
        print("Please allow outbound port 80 from your host")
        return False


main()
