"""
If statements in Python work very similarly to Java

"""

"""
A score of a student is given, write a program that can calculate the grade of the student

    Possible grades are:
        1. A ( 90 ~ 100)
        2. B ( 80 ~ 90 )
        3. C ( 70 ~ 80 )
        4. D ( 60 ~ 70 )
        5. F ( less than 60)
"""
score = 642

if 0<= score <= 100:    # Outer Loop
    if score >= 90:         # Inner Loop
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else: print('F')
else:
    print("Incorrect Grade Range")