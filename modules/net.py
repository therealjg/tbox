## required
import click
from lib.tbox import tbox
from lib import customTypes
## end required

import socket


@tbox.group()
def net():
    pass

@net.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def blacklist(config, host):
    """ This scripts greets you"""
    reverse_ip=".".join(reversed(host.split('.')))
    print(reverse_ip + ".bl.spamcop.net")
    try:
        socket.gethostbyname(reverse_ip + ".bl.spamcop.net")  # buggy approach but PoC
        print("blacklisted")
    except socket.gaierror:
        print("not found")
    except Exception:
        print("error")
