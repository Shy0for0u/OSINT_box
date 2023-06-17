import dns


def dns_mx_record(address):
    try:
        my_resolver = dns.resolver.Resolver(configure=False)
        my_resolver.nameservers = [
                    "8.8.8.8",
                    "8.8.4.4",
                    "9.9.9.9",
                    "149.112.112.112",
                    "208.67.220.220",
                    "208.67.222.222"
                    ]
        answers = my_resolver.resolve(address, 'MX')
    except (dns.exception.DNSException, dns.resolver.NXDOMAIN) as error:
        return f"Error: {error}"
    else:
        return "\n".join([f"MX Record:{rdata.exchange}" for rdata in answers])

# ctftime.org
