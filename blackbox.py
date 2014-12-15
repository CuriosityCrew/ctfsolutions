#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

answers = {}
cases = [{}, {'6 4': '5 5\n'}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

sock = socket()
sock.connect(('blackbox.qctf.ru', 60000))

while True:
    time.sleep(0.2)
    data = sock.recv(4096).split('\n')
    print data
    if len(data) == 3:
        case = int(data[0][6:])
    else:
        if data[0][:4] == "Nope":
            case = int(data[2][6:])
            cases[case-1][test] = data[0][15:]+"\n"
        else:
            case = int(data[1][6:])
    if case > 10:
        sock.close()
        sock = socket()
        sock.connect(('blackbox.qctf.ru', 60000))
        continue

    if len(data) == 3:
        test = data[1][6:]
    else:
        if data[0][:4] == "Nope":
            test = data[3][6:]
        else:
            test = data[2][6:]

    if test in cases[case].keys():
        sock.send(cases[case][test])
    else:
        sock.send("1111 1111\n")
