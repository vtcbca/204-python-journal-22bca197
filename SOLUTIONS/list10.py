#wriate a script to check if the list contains three consecutive common numbers in Python using udf.

def check_consecutive_common_numbers(lst):
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            return lst[i]
    return None

lst = [4, 5, 5, 5, 3, 8]
common_num = check_consecutive_common_numbers(lst)
print(common_num)

