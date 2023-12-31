# Write a Python function to get the largest number, smallest num and sum
# of all from a list

def new_fun(in_list):
    sum = 0
    small_num = in_list[0]
    large_num = in_list[0]

    for i in in_list:
        if i > large_num:
            large_num = i
        if i < small_num:
            small_num = i
        sum +=i

    return sum,small_num,large_num

def sort_fun(in_list):
    return sum(in_list),min(in_list),max(in_list)

num_list = [37,2,13,53,6,43,65]
print("Sum of all Numbers: %d \nSmallest Number: %d\nLargest Number: %d"% (new_fun(num_list)))
print("Sum of all Numbers: {}\nSmallest Number: {}\nLargest Number: {}".format(*sort_fun(num_list)))