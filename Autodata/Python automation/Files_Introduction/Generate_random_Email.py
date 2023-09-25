"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the given list of domains.

*  Domain list is provided as variable 'list_of-domains.

HINT:
 To generate random string with all lower case you can use this code
 import random
 import string
 letters = string.ascii_lowercase
 random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each ending with a comma.
- output file name: out_generate_random_email_with_list_of_domans_v1.csv

"""
import random
import string
list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length_of_email = 20
letters = string.ascii_lowercase

output_path ='out_generate_random_email_with_list_of_domans_v1.csv'
all_emails = []
# letters = string.ascii_lowercase
# random_string = ''.join(random.choice(letters) for i in range(length))

for domain in list_of_domains:
    #print(domain)
    for i in range(20):
    #     print(domain)

        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        #print(random_string)
    #email = random_string + '@' + domain
    email = f"{random_string}@{domain}"
    #email = "{}@{}".format(random_string,domain)
all_emails.append(email)
#print(email)
# import  pdb; pdb.set_trace()

with open(output_path, 'w') as f:
    # for email in list_of_domains:
    #     f.write(email)
    #     f.write(',\n')

    all_emails_str = '.\r'.join(all_emails)
    f.write((all_emails_str))