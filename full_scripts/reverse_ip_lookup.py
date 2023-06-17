import requests
import socket
import ipaddress


def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def get_domain(host):
    try:
        ip = socket.gethostbyname(host)
        if validate_ip_address(host):
            host = socket.gethostbyaddr(host)[0]
    except (Exception, socket.herror):
        return host, host
    else:
        return host, ip


def reverse_ip_lookup(ip_or_domain):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}

    if "://" in ip_or_domain:
        ip_or_domain = ip_or_domain.split('://')[1]
    ip_or_domain = ip_or_domain.replace('/', '')

    api_link = f"https://api.hackertarget.com/reverseiplookup/?q={ip_or_domain}"
    try:
        page = requests.get(api_link, headers=head)
        page.raise_for_status()
        assert page.status_code == 200
    except (AssertionError, requests.exceptions.RequestException) as error:
        return f"Error: {error}"
    else:
        domain, ip = get_domain(ip_or_domain)
        return f"Found domain hosted on the same web server as {domain} ({ip})\n" + page.text


# reverse_ip_lookup()

# luxdevices.com
# 77.88.55.55

# https://hackertarget.com/
# https://whoisxmlapi.com/
# https://viewdns.info/reverseip/

