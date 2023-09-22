"""
1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list: [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]

1.2 write a program that can multiply each odd number by 2
		            ex:
		            	list = [1,2,3,4,5];

		                output: [2,2,6,4,10]
"""


# 1.1
def move_zeros(l1: list) -> list:
    list_of_zeros = [x for x in l1 if x == 0]
    for x in range(0, len(list_of_zeros)):
        l1.remove(0)

    l1.extend(list_of_zeros)
    return l1


nums = [1, 0, 2, 0, 3, 0, 4, 0]

print(move_zeros(nums))

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 1.2
def mult_odd_numbs(l1: list) -> list:
    # Iterating over whole list (l1)
    for x in range(0, len(l1)):

        # if elem is odd
        if l1[x] % 2 == 1:
            # pop() : remove elem and assign it to 'odds'
            odd_nums = l1.pop(x)
            # insert new elem (prevElem * 2) to the given index # (the index that was popped)
            l1.insert(x,odd_nums * 2)

    return l1

print('---------------1.2--------------')
nums2 = [1, 2, 3, 4, 5]
print(mult_odd_numbs(nums2))
#-> [2, 2, 6, 4, 10]
