import sys

def print_size_in_bytes(data):
    size = sys.getsizeof(data)
    print(f"The size of the data in bytes is: {size} bytes")

def main():
    user_input = input("Enter the data: ")
    print_size_in_bytes(user_input)

if __name__ == "__main__":
    main()