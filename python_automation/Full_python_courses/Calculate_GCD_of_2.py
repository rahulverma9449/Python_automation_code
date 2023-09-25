# n1 = int(input("enter any number n1:\n"))
# n2 = int(input("enter any number n2:\n"))
def findGcd(x, y):
    if x > y:
        mn = x

    else:
        mn = y

for i in range(1, mn + 1):
    if x % i == 0 and y % i == 0:
        gcd = i

print(f"The gcd of these two numbers is {gcd}")

