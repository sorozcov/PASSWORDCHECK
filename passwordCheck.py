# Silvio Orozco Vizquerra 299537005
# Program for Checking you Password against Password Leaks

from getpass import getpass
import time
import math 
import progressbar

# First we ask user password to evaluate
while True:
    password = getpass("Enter Password to evaluate: ", "*")
    password_confirm = getpass("Confirm Password to evaluate: ", "*")
    if(password!=password_confirm):
        print("Passwords to check didn't match. Please try again.")
        continue
    break



print("We start the evaluation of your password. Please wait.")
found_password_in_dict = 0

# We take the time that it takes to check all password in the dictionary assuming
start = time.time()
filePasswords = open("rockyou2021.txt", "r")

password_found = ""
#We do the dictionary attack
#We assume in this case we have the plain text password already and not the hashes
i=0
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength) 
BUF_SIZE = 1024
TOTAL_SIZE = 0
tmp_lines = filePasswords.readlines(BUF_SIZE)
TOTAL_SIZE = TOTAL_SIZE + BUF_SIZE
# while TOTAL_SIZE<1000:
while tmp_lines:
    for line in filePasswords.read(1024):
        passw = line.rstrip()
        if(passw==password):
            found_password_in_dict = found_password_in_dict + 1
            password_found = x
        time.sleep(0.1)
        i=i+1
        bar.update(i)
    TOTAL_SIZE = TOTAL_SIZE + BUF_SIZE
    tmp_lines = filePasswords.readlines(BUF_SIZE)
print("\n")
if(found_password_in_dict>0):
    print("Password has ben found in leaked dictionary. {}".format(found_password_in_dict))
    print("Password Found was {} in {} entries".format(password_found,i))
else:
    print("Password was not found in dict and it will most likely pass a dictionary attack in a total of {} entries checked.".format(i))

end = time.time()
time_in_s = end - start
print("Total time in seconds to check {}".format(time_in_s))

# Characters available for a password
# Numbers (10 different: 0-9) 
# Letters (52 different: A-Z and a-z) 
# Special characters (32 different).
# Total 94

# m size of possible caracters 94
N = 94
# m size of password
m = len(password) 

# Entropy
entropy_of_password = math.log(N,2)*m
print("Entropy of password {}".format(entropy_of_password))
# Nist Guidelines entropy
entropy_nist = 0
entropy_nist = entropy_nist + 6 if m>0 else entropy_nist
entropy_nist= entropy_nist + (m-1)*2 if m>1 and m<=8 else (entropy_nist + 7*2 if m>8 else entropy_nist)
entropy_nist= entropy_nist + (m-8)*1.5 if m>8 else entropy_nist
ntropy_nist= entropy_nist + 3 if any(character.isupper() for character in password) else entropy_nist
entropy_nist= entropy_nist + 3 if not password.isalnum() else entropy_nist
entropy_nist= entropy_nist + 6 if not found_password_in_dict else entropy_nist
print("Entropy Nist of Password {}".format(entropy_nist))

# Calculate Effective L of Password, L is Good if its more than 14
L = m * math.log(N,10)
print("L value of password (safe if more than 14) {}".format(L))

