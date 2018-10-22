import bcrypt
from getpass import getpass
master_secret_key = getpass('Master secret: ')
raw_password = input('Pass: ')
salt = bcrypt.gensalt()
combo_password = raw_password + salt + master_secret_key
hashed_password = bcrypt.hashpw(combo_password, salt)