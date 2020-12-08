from pikepdf import Pdf
import argparse
import re

def crack_password(digits, filename, pattern):
    i = 1
    i_max = 9999999999999999999 % (10**digits)
    while i < i_max + 1:
        password_num = str(i).zfill(digits)
        if pattern is None or pattern.match(password_num):
            try:
                Pdf.open(filname_or_stream = filename, password = password_num)
                print("SUCCESS: Password - " + password_num)

                return True
            except:
                # incorrect password
                pass
        i += 1
    return False

# Command line arguments
parser = argparse.ArgumentParser(description="PDF Numeric Password Cracker")
parser.add_argument('filename', help="Full path of the PDF file")
parser.add_argument('-m', '--min-digits', help="Minimum digits in password", type=int, default="1")
parser.add_argument('-n', '--max-digits', help="Maximum digits in password", type=int, default="-1")
parser.add_argument('-r', '--matching-regex', help="Skip passwords not matching regex", type=str, default=None)
args = parser.parse_args()

min_digits = args.min_digits
max_digits = args.max_digits
pattern = None

if max_digits < min_digits:
    max_digits = min_digits

if args.matching_regex is not None:
    pattern = re.compile(args.matching_regex)
    print('Skipping passwords not matching:', args.matching_regex)

# Iterate
# digits = min_digits
# found_password = False
# print("Cracking. Please wait...")
# while not found_password and digits <= max_digits:
#     print("Trying to crack using " + str(digits) + " digit passwords")
#     found_password = crack_password(digits, args.filename, pattern)
#     digits += 1
# if not found_password:
#     print("Could not crack the password")

digits = min_digits
hacked = False
print("Attempting to crack password...")

while not hacked and digits <= max_digits:
    hacked = crack_password(digits, args.filename, pattern)
    digits += 1

if not hacked:
    print("FAIL: Unable to crack password for this file")