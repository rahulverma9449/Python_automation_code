#  Example: Function to add two number

# def my_adder(a, b):
#     total = a + b
#     # print(total)
#     return total
# my_total = my_adder(4, 15)
# print(my_total)

# Example: function to determine if given state has no sales tax


def has_no_sales_tax(state):
    state_with_no_sales_tax = ['AK', 'DE', 'MT','NH', 'or']

    if state.upper() in state_with_no_sales_tax:
        return True
    else:
        return False

    # return no_tax

user_state = "DE"
has_tax = has_no_sales_tax(user_state)
print(has_tax)












