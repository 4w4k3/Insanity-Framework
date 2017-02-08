#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import urllib2
import subprocess


def update_client_version(version):
    """ Update the client version with the latest git version """
    with open("version.txt", "r") as vnum:
        if vnum.read() != version:
            print("[*] Updating to latest version..")
            subprocess.call(["git", "pull", "master"])
        else:
            print("[*] You already have the latest version.")


def main():
    """ Main function that calls the update function """
    update_client_version(
        urllib2.urlopen("https://raw.githubusercontent.com/4w4k3/Insanity-Framework/master/version.txt").read()
    )


if __name__ == '__main__':
    main()
