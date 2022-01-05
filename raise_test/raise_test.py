"""
https://stackoverflow.com/questions/59038339/deliberately-raise-and-throw-an-exception-in-python
https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
"""


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self) -> str:
        return f'ERROR!!! : {self.msg}'


def run_sth():
    print('run when value error')


###


def raise1():
    """
    - 출력메시지
    run when value error
    """
    try:
        raise ValueError
    except ValueError:
        run_sth()

def raise2_1():
    """
    - 출력메시지
    Traceback (most recent call last):
    File "raise_test.py", line 48, in <module>
        raise2_1()
    File "raise_test.py", line 28, in raise2_1
        integer = int('num')
    ValueError: invalid literal for int() with base 10: 'num'
    """    
    try:
        integer = int('num')
    except ValueError as err:
        # print(err)
        raise

def raise2_2():
    """
    - from None을 이용해서 Exception(ValueError) chaining을 차단
    - 출력메시지
    Traceback (most recent call last):
    File "raise_test.py", line 58, in <module>
        raise2_2()
    File "raise_test.py", line 45, in raise2_2
        raise MyException('not int type') from None
    __main__.MyException: ERROR!!! : not int type    
    """
    try:
        integer = int('num')
    except ValueError:
        # raise MyException('not int type') from None
        raise MyException('not int type')

def raise3():
    """
    - 출력메시지
    Traceback (most recent call last):
    File "raise_test.py", line 77, in <module>
        raise3()
    File "raise_test.py", line 61, in raise3
        raise MyException('4 not found')
    __main__.MyException: ERROR!!! : 4 not found
    """
    ls = [1, 2, 3]
    result = [ele for ele in ls if ele == 4]

    if not result:
        raise MyException('4 not found')
    else:
        print('success')

def raise4():
    """
    - 출력메시지
    check given list
    """
    ls = [1, 2, 3]
    result = [ele for ele in ls if ele == 4]
    try:
        if not result:
            raise MyException('4 not found')
    except MyException:
        print('check given list')

# raise1()
raise2_1()
# raise2_2()
# raise3()
# raise4()
