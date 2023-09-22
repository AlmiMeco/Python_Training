"""
1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list: [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]
"""


def move_zeros(l1: list) -> list:
    list_of_zeros = [x for x in l1 if x == 0]
    for x in range(0, len(list_of_zeros)):
        l1.remove(0)

    l1.extend(list_of_zeros)
    return l1


nums = [1, 0, 2, 0, 3, 0, 4, 0]

print(move_zeros(nums))
