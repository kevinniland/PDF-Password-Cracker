import argparse
import re
from pikepdf import Pdf

# Logic
# def crack_password(digits, filename, pattern):
def crack_password(digits, filename):
    i = 1
    i_max = 9999999999999999999 % (10**digits)
    while i < i_max + 1:
        password_num = str(i).zfill(digits)

        # if pattern is None or pattern.match(password_num):
        try:
            Pdf.open(filename_or_stream = filename, password = password_num)
            print("SUCCESS: Password - " + password_num)

            return True
        except:
            # Incorrect password, keep trying
            print(i)
            pass
        
        i += 1
    
    return False

# Command line arguments
parser = argparse.ArgumentParser(description="PDF Numeric Password Cracker")
parser.add_argument('filename', help="Full path of the PDF file")
parser.add_argument('-min', '--min-digits', help="Minimum digits in password", type=int, default="1")
parser.add_argument('-max', '--max-digits', help="Maximum digits in password", type=int, default="-1")
parser.add_argument('-r', '--matching-regex', help="Skip passwords not matching regex", type=str, default=None)
args = parser.parse_args()

min_digits = args.min_digits
max_digits = args.max_digits
pattern = None

if max_digits < min_digits:
    max_digits = min_digits

# if args.matching_regex is not None:
#     pattern = re.compile(args.matching_regex)
#     print('Skipping passwords not matching:', args.matching_regex)

digits = min_digits
hacked = False
print("Attempting to crack password...")

while not hacked and digits <= max_digits:
    # hacked = crack_password(digits, args.filename, pattern)
    hacked = crack_password(digits, args.filename)
    digits += 1

if not hacked:
    print("FAIL: Unable to crack password for this file")