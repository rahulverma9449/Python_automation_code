import pdb

# sample_file ='./programming_language_wikipedia.txt'
#
# with open(sample_file, 'r') as f:
#     content = f.read()
#
# print(content)

# Example-2
countries_file = './country_list.txt'
with open(countries_file, 'r')as my_f:
    # countries = my_f.read()
    countries = my_f.readlines()
    # countries = my_f.readlines()
list_of_c = [i.strip() for i in countries]
pdb.set_trace()