"""
Lets say we have the following list and we are asked to sort it in ascending order
[3, 5, 1, 9, 2, 0]

How would we do this?

For this lesson we will an alogorithm called Selection sort. 
The main idea of selection sort is to divide the list into two parts - sorted and unsorted. 
Then we find the smallest yet unsorted number and add it to the end of the sorted list. 
We keep doing this until there are no more unsorted numbers.

At the beginning, all the elements are unsorted. 

Let's mark all unsorted elements with "" marks

["3", "5", "1", "9", "2", "0"]

To begin, we find the smallest yet unsorted number which is 0. 
Then we swap 0 with the number at the end of the sorted list. 
Since nothing is sorted yet, "3" is the end of the sorted list. 
So we swap "0" with "3" and get [0, "5", "1", "9", "2", "3"]

*Note that I removed the "" sign from the zero because it's now sorted. 
Now the end of the sorted part is denoted by "5".

We again look for the smallest yet unsorted number. This time it's "1". 
We swap "1" with "5" and get [0, 1, "5", "9", "2", "3"].

We keep doing the same thing until there are no more unsorted numbers. 
[0, 1, 2, "9", "5", "3"]

[0, 1, 2, 3, "5", "9"]

[0, 1, 2, 3, 5, "9"]

[0, 1, 2, 3, 5, 9]

Our list is now sorted. The intuition behind selection is that 
since in each iteration we are looking for the "smallest" element, 
we are essentially picking elements in ascending order. 
And since the elements in the sorted part are smaller than all elements 
in the unsorted part we do not have to compare with them again. 
"""

def min_item(lst):
    """
    This function takes a list as input and
    returns the smallest element
    """
    minimum = 0                                 # We set the first element as minimum
    for index in range(1, len(lst)):            # We scan through the rest of the list
        if lst[index] < lst[minimum]:           # If we find a number that is smaller than our current minimum,
            minimum = index                     # We set this new number as our current minimum. 
                                                # We keep comparing and updating the current minimum as we go along.
    return minimum


def swap(lst, i, j):
    """
    This funtion takes a list and and 
    two index positions as input. Then it swaps
    the items in the two index positions. 
    """        
    temp = lst[i]                               # We store the item in position i in a temporary variable so that we don't lose it
    lst[i] = lst[j]                             # We change the item in position i to now point to the item in position j. 
                                                # Note: Doing this would make python forget the original item in position i. But since we stored in a temporary variable, we're good.
    lst[j] = temp                               # We change the item in position j to now point to the item in our temporary variable i.e. the item that was originally in position i. 


def selection_sort(the_list):
    """
    This is our selection_sort algorithm
    """
    n = len(the_list)
    for i in range(n):                         # We are using the variable i to keep track of the end of the sorted part. In each iteration it increases by one.
        min = i + min_item(the_list[i:])       # We find the smallest number in the unsorted part. the_list[i:] is a python trick called list slicing. 
                                               # We are essentially choosing to omit the sorted part and start finding the minimum in the unsorted part which starts from i.
        swap(the_list, i, min)                 # We swap the minimum with the item at the end of the sorted part. And go back to beginning of the loop.


if __name__ == "__main__":

    # Test case 1: A random list of numbers
    the_list = [3, 4, 1, 5, 9, 0]
    selection_sort(the_list)
    print(the_list)

    # Test case 2: A list with negative values
    the_list = [3, -4, 1, 5, -9, 0]
    selection_sort(the_list)
    print(the_list)

    # Test case 3: An empty list
    the_list = []
    selection_sort(the_list)
    print(the_list)

    # Test case 4: An already sorted list
    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    selection_sort(the_list)
    print(the_list)

    # Test case 5: A list with only one value
    the_list = [7]
    selection_sort(the_list)
    print(the_list)

    # Test case 6: A list with duplicate values
    the_list = [3, 4, 1, 5, 9, 0, -4, 5]
    selection_sort(the_list)
    print(the_list)

    # Test case 7: A list with all equal elements
    the_list = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    selection_sort(the_list)
    print(the_list)

    # Performance test: Used to demonstrate why selection_sort might not be the best choice

    import timeit
    import random

    list_1 = list(range(1, 1000+1))
    random.shuffle(list_1)

    list_2 = list(range(1000, 0, -1))

    list_3 = list(range(1, 1000+1))

    res1 = timeit.timeit(lambda: selection_sort(list_1), number=100)
    print(f"Time taken to sort a random list: {res1}")

    res2 = timeit.timeit(lambda: selection_sort(list_2), number=100)
    print(f"Time taken to sort an already sorted list: {res2}")

    res3 = timeit.timeit(lambda: selection_sort(list_3), number=100)
    print(f"Time taken to sort a list is decreasing order: {res3}")
