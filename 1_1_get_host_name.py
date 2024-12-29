import socket


def get_host_name():
    """A function to get hostname and IP address of a local machine"""
    host_name = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(host_name)
        print(f'IP address of the host {host_name} is: {ip_address}')
    except socket.error as err_msg:
        print(f'{host_name} {err_msg}')


if __name__ == '__main__':
    get_host_name()