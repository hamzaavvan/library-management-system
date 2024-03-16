import hashlib, binascii
import timeago, datetime
import subprocess

salt=b'$#0x--.\'/\\98'
def hash(string):
    dk = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)
    return binascii.hexlify(dk).decode("utf-8")

def b_hash(string):
    dk = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)
    return binascii.hexlify(dk)
    
def ago(date):
    """
        Calculate a '3 hours ago' type string from a python datetime.
    """
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

    return (timeago.format(date, now)) # will print x secs/hours/minutes ago

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()