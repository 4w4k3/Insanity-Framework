#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import sys
import urllib2
import os

def one():
	response = urllib2.urlopen('https://raw.githubusercontent.com/4w4k3/Insanity-Framework/master/version.txt')
	data = response.read()
	fileup = open("version2.txt", 'w')
	fileup.write(data)
	fileup.close()
one()

def two():
	updatechk = open('version2.txt', 'r')
	xd2 = updatechk.read()
	print updatechk.read()
	version = open('version.txt', 'r')
	xd = version.read()
	version.close()
	updatechk.close()
	if xd2 != xd:
            print '[*] New Version is available =D Visit: https://github.com/4w4k3/Insanity-Framework'.format(GREEN, END)
        else:
            print '[*] You Already have the latest version =D'

two()
