'''
Practical Test: Write a script that extracts email addresses from a block of text using
regex.
'''

import re

def extract_emails(s):

    email_pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+"

    emails = re.findall(email_pattern, s)
    
    return emails

def main():

    s = 'Hi my name is ABC and my email id is abc@gmail.com, alternatively my email is xyz@yahoo.in, @@abc@gmail.in'

    email = extract_emails(s)
    print(email)

if __name__ == '__main__':
    main()