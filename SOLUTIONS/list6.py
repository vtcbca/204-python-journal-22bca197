#WAS TO CRATE LIST USING UDF Createlist().COUNT AND PRINT EVEN AND ODD NO. USINF UDF evenodd().
def createList(n):
    """Create a list of n random integers"""
    import random
    return [random.randint(1, 100) for i in range(n)]

def evenOdd(lst):
    """Count and print even and odd numbers in a list"""
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)

my_list = createList(10) # Create a list of 10 random integers
print("My list:", my_list)
evenOdd(my_list) # Count and print even and odd numbers in the list

