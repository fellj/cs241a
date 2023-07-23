fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)

def get_part1_list():
    """
    Filters a list to return even numbers greater than 33.
    """
numbers = [x for x in range(100)]

    # Write a line here that uses filter and a lambda function to filter
    # the list so that it only contains even numbers greater than 33.
over_33 = list(filter(lambda x: x % 2 == 0 and x > 33, numbers))
    
    


print(over_33)