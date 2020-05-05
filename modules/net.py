## required
import click
from lib.tbox import tbox
from lib import customTypes
## end required

import socket
import subprocess
import dns.resolver as resolver

@tbox.group()
def net():
    pass

@net.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def blacklist(config, host):
    """ This scripts greets you"""
    reverse_ip=".".join(reversed(host.split('.')))

    try:
        myAnswers = resolver.Resolver().query("%s.bl.spamcop.net" % reverse_ip, "A")
        print("blacklisted")
    except resolver.NXDOMAIN:
        print("not found")
    except Exception:
        print("error")

@net.command()
@click.argument('host', type=click.STRING, required=True)
@click.pass_obj
def ping(config,host):
    """ Check if Host is alive """
    command = ['ping', '-c', '1', host]
    if subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
        print("success")
    else:
        print("failed")