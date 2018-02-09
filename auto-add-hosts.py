
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima - http://blog.conectsys.com.br

from zabbix_api import ZabbixAPI
import csv

zapi = ZabbixAPI(server="http://zabuv01.fortebank.com/zabbix/")
zapi.login("Admin", "Rty7nbhjgkm")

f = csv.reader(open('/home/sd/hosts.csv'), delimiter=';')
for [name,hostname,model,alias,loc,lat,lon,ip,type,tid,gid] in f:
    print "Host succesful added ", f.line_num
    hostcriado = zapi.host.create({
        "host": hostname,
        "status": 0,
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
                "groupid": gid
            }
        ],
        "templates": [
            {
                "templateid": tid
            }
        ],
        "inventory_mode": 0,
        "inventory":
            {
                "location_lat": lat,
                "location_lon": lon,
                "location": loc,
                "name": name,
                "type": type,
                "alias": alias,
"model": model
            }

   })
