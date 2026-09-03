original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_even_numbers(original_list):
    filtered_list  = []
    for n in original_list:
        if n % 2 == 0:
            filtered_list .append(n)
    return filtered_list 


print(f"Original list: {original_list}")
print(f"List with even numbers only: {filter_even_numbers(original_list)}")