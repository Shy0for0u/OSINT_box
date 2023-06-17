import whois


def whois_add(add):
    try:
        domain = whois.whois(add)
        assert domain['domain_name']
    except AssertionError:
        return f"Error: No information"
    except whois.Exception as error:
        return f"Error: {error}"
    else:
        res = domain.__dict__
        return '\n'.join([f"{i}: {res[i]}" for i in res])

# pip install python-whois
# ctftime.org
