# tbox


Python3 required


## Install ##

```
$ git submodule init
$ virtualenv env
$ source env/bin/activate
$ pip install --editable .
```

## Available Commands ##
### IP Network Info - NET ###
```
net.blacklist:  Check IP or host for reputation
net.ping:       Perform a standard ICMP ping
```

### DNS ###
```
dns.mx: 	  	DNS MX records for domain
dns.a: 	  		DNS A record IP address for host name
dns.aaaa:		DNS AAAA record IP address for host name
dns.spf: 	  	Check SPF records on a domain
dns.txt: 	  	Check TXT records on a domain
dns.ptr: 	  	DNS PTR record for host name
dns.cname: 	  	DNS canonical host name to IP address
dns.soa: 		Get Start of Authority record for a domain
```

### SSL ###
```
ssl.get:			Retrieve SSL certificate (with & without SNI)
ssl.security:       Check for ssl security
```


## Backlog ##
### IP Network Info - NET ###
```
net.whois:          Get domain registration information
net.arin: 			Get IP address block information
net.trace: 			Perform a standard ICMP trace route
```

### DNS ###
```
dns.security: 	Check your DNS Servers for possible problems
```


### Email Settings ###
```
mail.security: 	  	Test mail server SMTP (port 25)
mail.dkim:
mail.dmarc:
```


### HTTP Test ###
```
http:			Verify URL allows http connections (Advanced <host>;<ip>)
http.ssl:		Verify a URL allows secure http connections (Advanced <host>;<ip>)
http.headers:	Check for security headers (Advanced <host>;<ip>)
```

### Port ###
```
port.tcp:		Verify an IP Address allows tcp connections <host>;<port>
port.http:		Verify a URL allows tcp port 80  
port.https:		Verify a URL allows tcp 443 incl ssl
```

### SSL ###
```
ssl:			Retrieve SSL certificate (using SNI)
ssl.noSNI:		Retrieve SSL certificate (without SNI)
ssl.security: 	Check for ssl security
```

### Alias ###
```
security.dns: 		dns.security - Check your DNS Servers for possible problems
security.testssl:	ssl.security - Check for ssl security
security.smtp:		smtp.security - Test mail server SMTP
```

```
== Advanced ==
port.nmap:		Do quick nmap assesment
security.burp?:	Do Burp Scan

= Monitor =
monitor:		<interval/2s, 20m> <command>
monitor.list:	Lists all monitors
monitor.delete: ID of monitor.list
monitor.hook:	add mail or web
monitor.hooks:	List all hooks
```
