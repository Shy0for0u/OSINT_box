import dns


def reverse_dns(ip):
    try:
        rev_name = dns.reversename.from_address(ip)
        reversed_dns = str(dns.resolver.resolve(rev_name, "PTR")[0])
    except (Exception, dns.exception.SyntaxError) as error:
        return f"Error: {error}"
    else:
        return reversed_dns


# 77.88.55.55
