import pygeoip
from os.path import abspath
from inspect import getsourcefile


def site_location(ip):
    try:
        p = abspath(getsourcefile(lambda: 0))
        gi = pygeoip.GeoIP(str(p)[:-6] + 'GeoIPCity.dat')
        city = gi.record_by_addr(ip)
        assert city
    except AssertionError:
        return f"Error: No information"
    except (pygeoip.GeoIPError, FileNotFoundError, OSError, TypeError) as error:
        return f"Error: {error}"
    else:
        output = ""
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            else:
                output += f"{key}: {city[key]}\n"
        return output

# 109.233.56.78
