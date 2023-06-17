from nslookup import Nslookup


def nslookup_site(domain):
    try:
        dns_query = Nslookup(dns_servers=dns_servers)
        ips_record = dns_query.dns_lookup(domain)
        assert ips_record.answer
    except (Exception, AssertionError) as error:
        return f"Error: {error}"
    else:
        output1 = "\n".join([i for i in ips_record.response_full])
        soa_record = dns_query.soa_lookup(domain)
        output2 = "\n".join(['\n'.join(i.split('. ')) for i in soa_record.response_full])
        return output1 + output2


dns_servers = [
    "8.8.8.8",
    "8.8.4.4",
    "9.9.9.9",
    "149.112.112.112",
    "208.67.220.220",
    "208.67.222.222"
]

# ctftime.org
