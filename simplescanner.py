import socket
import sys
import subprocess
import argparse
import time


def banner():
	print("""
	____ ____ ____ ____ ____ ____ ____ 
	||s |||c |||a |||n |||n |||e |||r ||
	||__|||__|||__|||__|||__|||__|||__||
	|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
		""") 
	return 0

def tcp_scan(target_IP, target_start_port, target_end_port):
    print("--------------------------------------------")
    print("Please wait, TCP scanning IP address:", target_IP)
    print("- - - - - - - - - - - - - - - - - - - - - - -")

    startTime = time.time()

    try:
        for port in range(target_start_port, target_end_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target_IP, port))
            if result == 0:
                print("[+]Port {}:/tcp Open".format(port))
                sock.close()

    except socket.errno.ECONNREFUSED:
        print("Connection refused")
        sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    endTime = time.time()
    difftime = endTime - startTime
    print('Completed in : ', '%.3f' % difftime + ' seconds')

    return 0


def udp_scan(target_IP, target_start_port, target_end_port):
    print("--------------------------------------------")
    print("Please wait, UDP scanning IP address:", target_IP)
    print("- - - - - - - - - - - - - - - - - - - - - - -")

    startTime = time.time()

    try:
        for port in range(target_start_port, target_end_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            result = sock.connect_ex((target_IP, port))
            if result == 0:
                print("[+] Port {}:/udp Open".format(port))
                sock.close()

    except socket.errno.ECONNREFUSED:
        print("Connection refused")
        sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    endTime = time.time()
    difftime = endTime - startTime
    print("Completed in : ", '%.3f' % difftime + " seconds")

    return 0


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    required = parser.add_argument_group("Required arguments")
    required.add_argument('-u', '--url', action='store',
                          dest='url', help='FQDN for scan', required=True)

    optional = parser.add_argument_group("Optional arguments")
    optional.add_argument('-p', '--port', action='store', dest='port',
                          default='1-1000', help='Range of ports to scan (default [1-1000])')

    optional.add_argument('-m', '--mode', action='store', dest='s_mode', choices={'sT', 'sU'}, 
                          default='sT', help='Scan type: -sT (TCP Scan), -sU (UDP Scan); (Default[-sT])')

    args = parser.parse_args()

    target = args.url
    targetIP = socket.gethostbyname(target)
    targetRange = args.port.split('-')

    # Convert range to int
    targetRange = [int(item) for item in targetRange]

    ##banner()

    if (args.s_mode == "sT"):
    	tcp_scan(targetIP, targetRange[0], targetRange[1])

    elif(args.s_mode == "sU"):
    	udp_scan(targetIP, targetRange[0], targetRange[1])
