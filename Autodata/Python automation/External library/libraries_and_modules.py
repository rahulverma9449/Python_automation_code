import random
my_num = random.randint(100,200)
my_num = random.randrange(3)

my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
random.shuffle(my_list)
random.choice(my_list)
data = random.uniform(12.4,34.5)
print(data)
data1 = random.triangular(23,45,56)
print(data1)
time = random.betavariate(12,34)
print(time)
gym = random.gammavariate(13.2,34.5)
print(gym)


