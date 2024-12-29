import socket
from binascii import hexlify


def convert_ip4_address():
    ip_addresses = ['127.0.0.1', '192.168.0.1']
    for ip_addr in ip_addresses:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        print(f'IP Address: {ip_addr} => \n'
              f'\t\t\tpacked: {hexlify(packed_ip_addr)}\n'
              f'\t\t\tunpacked: {unpacked_ip_addr}')



if __name__ == '__main__':
    convert_ip4_address()