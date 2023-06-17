import socket


def host_ip(host):
    if "://" in host:
        host = host.split('://')[1]
    host = host.replace('/', '')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.error as error:
        return f"Error: {error}\nMaybe you wrong, Try again!"
    else:
        return f"{'IP Address of '}{host}{' is '}{remote_ip}"
