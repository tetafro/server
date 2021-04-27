#!/usr/bin/env python3
# Script encrypts password with random salt according to ansible docs:
# https://github.com/ansible/ansible-examples/blob/master/language_features/user_commands.yml#L9-L10

import crypt
import string
import sys
import random

if len(sys.argv) != 2:
    print('Usage: ./passwd.py plain-text-password', file=sys.stderr)
    sys.exit(1)

pwd = sys.argv[1]
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
salt = ''.join(random.choice(chars) for _ in range(6))
print(crypt.crypt(pwd, f'$1${salt}$'))
