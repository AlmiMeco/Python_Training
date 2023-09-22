"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""


# 1.1
def eligible_to_vote(age: int, country: str) -> bool:
    if age >= 18 and country.upper() == 'USA':
        print("You Are Eligible")
        return True

    else:
        print('You Are Not Eligible')
        return False


eligible_to_vote(21, 'USA')  # -> You Are Eligible
eligible_to_vote(11, 'USA')  # -> You Are Not Eligible
eligible_to_vote(21, 'Albania')  # -> You Are Not Eligible

print('-------------------------------------------------------------------------')


def is_palindrome(s: str) -> bool:
    reverse_s = s[::-1]
    reverse_s.isalnum()
    if s.upper() == reverse_s.upper():
        print('Is Palindrome')
        return True
    else:
        print('Is Not Palindrome')
        return False


is_palindrome('Racecar')                            # -> Is Palindrome
is_palindrome('saippuakivikauppias')                # -> Is Palindrome
is_palindrome('A man, a plan, a canal – Panama')    # -> Is Not Palindrome
is_palindrome('diana')                              # -> Is Not Palindrome

