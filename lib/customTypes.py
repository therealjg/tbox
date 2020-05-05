import click
import re
import socket

##
# ToDo
# - IP / Hostname
# - IPv6
# - convert to safe string
##

# Check for valid IP address - Custom Type
class IPParamType(click.ParamType):
    name = "IP"

    def convert(self, value, param, ctx):
        try:
            socket.inet_aton(value)
            return value
        except Exception:
            self.fail(
                "expected value is not a valid IPv4 address, got '%s'" % value,
                param,
                ctx,
            )
# Check for valid IP address - Custom Type
class HostnameParamType(click.ParamType):
    name = "IP"

    def convert(self, value, param, ctx):
        try:
            if len(value) > 255:
                throw(Exception)
            if value[-1] == ".":
                value = value[:-1] # strip exactly one dot from the right, if present
            allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
            if all(allowed.match(x) for x in value.split(".")):
                return value
            else:
                throw(Exception)
        except Exception:
            self.fail(
                "expected value is not a valid hostname, got '%s'" % value,
                param,
                ctx,
            )
