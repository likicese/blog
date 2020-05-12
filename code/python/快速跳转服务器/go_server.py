#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import sys

ser = {
    "dev": {
        "1": {"name": "ser1", "ip": "192.168.1.1", "port": "22", "user": "root"}
        , "20": {"name": "ser2", "ip": "192.168.1.2", "port": "22", "user": "root"}
    }

    , "prod": {
        "1": {"name": "h1", "ip": "10.1.1.1", "port": "22", "user": "root"}
        , "2": {"name": "h2", "ip": "10.1.1.2", "port": "22", "user": "root"}
    }
}

id_key = "~/.ssh/id_rsa"


def server_list_print(sl):
    for s in sl:
        t = "{0:<5}{1:<10}\t{2:<}"
        print(t.format(s, sl[s]["name"], sl[s]["ip"]))


def go_server(server_list):
    while 1:
        server_list_print(server_list)
        server_id = input("please input server ID\n")
        if server_id == "q":
            break
        try:
            s = server_list[server_id]
            str = "ssh -o stricthostkeychecking=no -i " + id_key + " " + s["user"] + "@" + s["ip"] + " -p " + s["port"]
            print(str)
            ms = os.system(str)
            print(ms)
        except KeyError:
            continue


def go():
    try:
        print(sys.argv[1])
        if len(sys.argv) == 0:
            raise KeyError
        else:
            go_server(ser[sys.argv[1]])
    except KeyError:
        g_list = list(ser.keys())
        str = ""
        if len(g_list) > 0:
            str = str + g_list[0]
        if len(g_list) > 1:
            for i in g_list[1:]:
                str = str + " || " + i
        print(str)


if __name__ == "__main__":
    go()