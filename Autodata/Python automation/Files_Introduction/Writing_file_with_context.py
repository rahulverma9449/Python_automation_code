
my_string = " I love my darling anjali"

# Example-1

with open('./sample2.txt', 'w') as my_f:
  my_f.write(my_string)

# ex-2
# my_l = ['user1', 'user2', 'user3']
# with open('./sample2.txt', 'w') as my_f:
#   for i in my_l:
#
#       my_f.write(i)
#       my_f.write('\n')
#       my_f.write('\t')


#example-3 (appending)

var2 = " Also love you too much"
with open('./sample2.txt', 'a') as f:
  f.write('\n')
  f.write(var2)


# ex-4

# my_lang = ['python','js','java','ruby']
#
# with open('./sample2.txt, 'w') as f:
#
#   f.writelines(my_lang)

#ex-5
my_lang = ['python','js','java','ruby']

with open('./sample2.csv', 'w') as f:
  str_my_lang = '\n'.join(my_lang)

  f.writelines(str_my_lang)
