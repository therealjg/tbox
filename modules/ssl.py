#!/usr/bin/python

## required
import click
from lib.tbox import tbox
from lib import customTypes
## end required

import os

######################
######################
#### Functions    ####
######################
######################


@tbox.group()
def ssl():
    """ SSL T00ls """
    pass

@ssl.command()
@click.option('--string', type=customTypes.IPParamType(), default="127.0.0.1", help="some string")
@click.option('--repeat', default=1, help="repeat counter")
@click.argument('out', type=click.File('w'),default='-',required=False)
@click.pass_obj
def say(config,string,repeat, out):
    """ This scripts greets you"""
    for x in range(repeat):
        print("hello world %s" % string)


### ToDo: https://gist.github.com/gdamjan/55a8b9eec6cf7b771f92021d93b87b2c

@ssl.command()
@click.argument('host', type=customTypes.HostnameParamType())
@click.argument('origin', required=False)
@click.pass_obj
def get(config,host, origin):
    """ Get Certificate """
    if origin == None:
        # no SNI
        print("No SNI - %s" % host)
        os.system('openssl s_client -showcerts -connect %s:443   < /dev/null 2>&1 |  sed -n "/-----BEGIN/,/-----END/p" | openssl x509 -text -noout' % host)
        #
    else:
        # SNI
        print("SNI - %s via %s" % (host, origin))
        os.system('openssl s_client -showcerts -connect %s:443 -servername %s  < /dev/null 2>&1 |  sed -n "/-----BEGIN/,/-----END/p" | openssl x509 -text -noout' % (origin, host))



@ssl.command()
@click.option('--port', default=443, help="Port")
@click.argument('host')
@click.pass_obj
def security_scan(config, host, port):
    """ Do Scan via testssl """
    os.system(os.path.dirname(__file__) + '/ssl/testssl.sh/testssl.sh --sneaky %s:%d' % (host, port))

