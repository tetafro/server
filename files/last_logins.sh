#!/bin/bash

echo -e "\nLast logins:"
last | \
    grep -v "reboot" | \
    tail -n +2 | \
    head -n 3 | \
    awk '{printf " \033[1;31m%s\033[0m from %s on %s %s at %s\n", $1, $3, $6, $5, $7}'

echo -e -n "\nTotal server uptime: "
server_uptime=$(uptime | cut -d ',' -f 1 | cut -d ' ' -f 4,5)
echo -e "\033[1;31m$server_uptime\033[0m\n"
