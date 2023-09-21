print('----------closure-----------------')

"""
Closure -> Functions inside a Function (recursive funct)
"""


def display_msg():
    def method():
        print('Hello World')
        print('I love Python')

    method()
    method()
    method()


display_msg()

print('-------------map() method------------')
"""
Python map() == Java map() * but more simplified *  
Pass a collection thru a lambda stream
Returns map obj -> can be wrapped in List, Tuple, etc 
        map():
            accepts 2 args ->
            map( function(lambda) , iterable(collection) )
"""


nums = [10, 20, 30, 40, 50, 60, 70, 80]
# divide each element by 10

nums = list(map(lambda p: int(p / 10), nums))
print(nums)
# -> [1, 2, 3, 4, 5, 6, 7, 8]

print('-------------filtering w/ comprehensions------------')
# Filter ODD #s from 'nums'

nums_filtered_by_comp = [x for x in nums if x % 2 == 0]
print(nums_filtered_by_comp)
# -> [2, 4, 6, 8]

print('-------------filtering w/ filter() method------------')
# Filter EVEN #s from 'nums'

nums = list(filter(lambda p: p % 2 == 1, nums))
print(nums)
# -> [1, 3, 5, 7]

