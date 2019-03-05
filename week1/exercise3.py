#! /usr/bin/env python

from __future__ import unicode_literals

ipv6_ll = "fe80::1"
IPV6_MC = "ff00::5"
ipv6_global = "2001::1"

print("are ipv6_ll and IPV6_MC equal?")
print(ipv6_ll == IPV6_MC)
print("is ipv6_ll NOT equal to ipv6_global?")
print("ipv6_ll" != "ipv6_global") 
