import argparse
import sys
# import pikepdf
import re
from tqdm import tqdm

password = 123456
starting_num = 0
i = 0

# Issues
# ======
# How to deal with a password such as 00001? 000234? Python doesn't consider 00001 a valid int. When converting the string "00001"
# to an int, it will simply be 1. This can pose a problem when the password is of length 6, for example - program won't get a hit
# on the correct password as it will remove any leading 0's (currently)
# Based on research, look into zfill - adds zero to start of string until it reaches specified length

# Logic
def crack_password(digits, file):
    while i < sys.maxsize:
        password = str(i).zfill(digits)

        try:
            Pdf.open(filname_or_stream = file, password = password)
            print("Password: " + password)

            return True
        except:
            pass
        
        i += 1
    
    return False

parser = argparse.ArgumentParser(description="PDF Numeric Password Cracker")
parser.add_argument('filename', help="Full path of the PDF file")
args = parser.parse_args()

print("Attempting to crack password...")
crack_password(6)