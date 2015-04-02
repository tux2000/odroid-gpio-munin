#!/bin/sh

#/usr/local/bin/gpio write 4 0
/usr/local/bin/gpio write 5 0
sleep 0.1
/usr/local/bin/gpio aread 1
/usr/local/bin/gpio write 5 1
#/usr/local/bin/gpio write 4 1

sleep 1

/usr/local/bin/gpio write 4 0
sleep 0.1
/usr/local/bin/gpio aread 1
/usr/local/bin/gpio write 4 1

