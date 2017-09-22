#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima - http://blog.conectsys.com.br

from zabbix_api import ZabbixAPI
import csv

zapi = ZabbixAPI(server="http://IP/zabbix/")
zapi.login("Admin", "zabbix")

f = csv.reader(open('/home/sd/hosts.csv'), delimiter=';')
for [hostname,ip,lat,lon,loc,name] in f:
    print "Host succesful added ", f.line_num
    hostcriado = zapi.host.create({
        "host": hostname,
        "status": 1,
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": 10050
            }
        ],
        "groups": [
            {
                "groupid": 2
            }
        ],
        "templates": [
            {
                "templateid": 10001
            }
        ],
"inventory_mode": 0,
        "inventory":
           {
"location_lat": lat,
"location_lon": lon,
"location": loc,
"name": name,
}

   })
