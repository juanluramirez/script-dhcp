# -*- coding: utf-8 -*-

import sys
import commands

if sys.argv[1] == "-l":
	concesiones_clientes = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep '{' |uniq |awk '{print $2}'")
	reservas_IP = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep 'fixed-address' |sort |uniq|awk '{print $2}'")
	reservas_IP = reservas_IP.replace(";","")
	print "Las direcciones IP que ha concedido el servidor DHCP son: /n"
	print concesiones_clientes
	print "Las direcciones IP que se han reservador son: /n"
	print reservas_IP

else: 
	concesiones_clientes = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep 'hardware ethernet' |sort |uniq|awk '{print $3}'"
	concesion_clientes = concesion_clientes.replace(";", "");
	if len(concesion_clientes) > 0:
		print "IP;",sys.argv[1]
		print "MAC:",concesion
	else:
		print "No hay ninguna concesión con la ip %s " % sys.argv[1] 
