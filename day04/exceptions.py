
"""
ZeroDivisionError needs to be caught (10/0)
Try && Except same as Java Try && Catch
If we expect exceptions to arise we should encase the code in try/except
Try && Except -> Mandatory : everything else is optional
** PYTHON HAS NO CHECKED EXCEPTIONS, ONLY RUNTIME EXCEPTIONS -> SINCE PYTHON USES 'INTERPRETER' NOT 'COMPILER' **
'raise' keyword in Python == 'throw' keyword in Java
"""
try:
    num = 10/0
    print(num)
except:
    print('OOPS... Something went wrong')





