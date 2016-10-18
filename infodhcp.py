# -*- coding: utf-8 -*-

import sys
import commands

if sys.argv[1] == "-l":
	concesiones_clientes = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep '{' |uniq |awk '{print $2}'")
	reservas_IP = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep 'fixed-address' |sort |uniq|awk '{print $2}'")
	print "Lista de concesiones servidor DHCP"
	print concesioness
	print "Lista IP reservadas"
	print reservas_IP