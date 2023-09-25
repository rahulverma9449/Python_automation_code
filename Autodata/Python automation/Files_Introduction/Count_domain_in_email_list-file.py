"""
-- input file: count-domains_in_email_list_file_exercise_input.csv
-- output file: count_domains_in_email_list_file_exercise_output.json
Example output;
{ 'yahoo.com':19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""
import pdb
import random
import json
input_file = " count_domains_in_email_list_input.csv"
output_file = " count_domians_in_email_list_file_output.json"

def get_email_form_file(file_path):

     with open(file_path, 'r') as f:
      email_raw = f.readlines()
     emails_clean = [i.strip('\n') for i in email_raw]
     return emails_clean

list_of_email = { 'yahoo.com':19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}
# Solution option 1
def count_domains_option_1(list_of_emails):
     print("Doing counts options 1")
     email_counts = dict()
     for email in email_list:
          domain = email.split('@')[-1]
          if domain not in email_counts.keys():
               email_counts[domain] = 1
          else:
               email_counts[domain] = email_counts[domain] + 1
     return email_counts

     # email_list = get_email_form_file(input_file)
     # counts_1 = count_domains_option_1(email_list)
     # print(counts_1)

def count_domains_optionS_2(list_of_emails):
     print("Doing count options 2")
     domains_list = []
     for email in list_of_emails:
          domain = email.split('@')[-1]
          domains_list.append(domain)
          unique_domains = set(domains_list)
          # print(domains_list)
          # print(unique_domains)
          email_count = dict()
          for domain in unique_domains:
               email_count[domain] = domains_list.count(domain)

          return  email_count
def save_output_in_json_file(counts_dict,json_file_path):
     print(f"Saving file: {json_file_path}")

     with open(json_file_path, 'w') as f:
          json_obj = json.dumps(counts_dict)
          f.write(json_obj)



          email_list = get_email_form_file(input_file)
     #counts_1 = count_domains_option_1(email_list)
#pdb.set_trace()



          counts2 = count_domains_optionS_2(email_list)
          save_output_in_json_file(counts2, output_file)
          print(counts2)
## solution options_2

          count_domains_optionS_2(email_list)