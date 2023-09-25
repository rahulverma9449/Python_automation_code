import random
import string
# import pdb;
# pdb.set_trace()

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length_of_emails = 10
total_number_of_emails = 100
output_file = 'out_generate_random_email_with_list_of_domans_v1.csv'
letters = string.ascii_lowercase

all_emails = []
for i in range(100):
    # Option-1
    random_domain = random.choice(list_of_domains)
    randon_string = ''.join(random.choice(letters) for i in range(length_of_emails))
    random_email = f"{randon_string} @ {random_domain}"    # random.sample(list_of_domains, 3)
    all_emails.append(random_email)

    # Option 2
    #print(all_emails)
    # print(len(all_emails))
    #all_emails.append(f"{''.join(random.choice(letters) for i in range(length_of_emails))}@{random.choice(list_of_domains)}")
with open(output_file, 'w') as f:
    f.write(',\n'.join(all_emails))