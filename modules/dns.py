## required
import click
from lib.tbox import tbox
from lib import customTypes
## end required

import dns.resolver as resolver

@tbox.group()
def dns():
    pass

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def blacklist(config, host):
    """ This scripts greets you"""
    reverse_ip=".".join(reversed(host.split('.')))

    try:
        myAnswers = resolver.Resolver().query("%s.bl.spamcop.net" % reverse_ip, "A")
        #for rdata in myAnswers:
        #    print(rdata)
        print("blacklisted")
    except resolver.NXDOMAIN:
        print("not found")
    except Exception:
        print("error")


@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def a(config, host):
    """ Retrieve A Record """
    lookup(host,'A')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def aaaa(config, host):
    """ Retrieve AAAA Record """
    lookup(host,'AAAA')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def mx(config, host):
    """ Retrieve MX Record """
    lookup(host,'MX')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def spf(config, host):
    """ Retrieve SPF Record """
    try:
        myAnswers = resolver.Resolver().query(host, 'TXT')
        for rdata in myAnswers:
            if 'spf' in str(rdata):
                print(rdata) 

    except resolver.NXDOMAIN:
        print("not found")
    except Exception:
        print("error")

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def txt(config, host):
    """ Retrieve TXT Record """
    lookup(host,'TXT')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def cname(config, host):
    """ Retrieve CNAME Record """
    lookup(host,'CNAME')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def soa(config, host):
    """ Retrieve SOA Record """
    lookup(host,'SOA')

@dns.command()
@click.argument('ip', type=customTypes.IPParamType() ,required=True)
@click.pass_obj
def ptr(config, ip):
    """ Retrieve PTR Record """
    host = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
    lookup(host,'PTR')

@dns.command()
@click.argument('host', type=click.STRING ,required=True)
@click.pass_obj
def security(config, host):
    """ < Dummy > Run DNS Security Check """
    pass


######

def lookup(host, type='A'):
    try:
        myAnswers = resolver.Resolver().query(host, type.upper())
        for rdata in myAnswers:
            print(rdata)
    except resolver.NXDOMAIN:
        print("not found")
    except Exception:
        print("error")
