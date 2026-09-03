number_list = [1, 2, 3, 4, 5]

def sum_of_list(number_list):
    calculation = 0
    for n in number_list:
        calculation += n
    return calculation

 
print(f"The sum of the numbers in the list is: {sum_of_list(number_list)}")