#!/usr/bin/python3
import dis
def magic_calculation(one,two):
    return (98 + (one ** two))
dis.dis(magic_calculation)
