"""
https://stackoverflow.com/questions/25854380/enforce-arguments-to-a-specific-list-of-values
"""

def argument_check(arg: int):
    """argument check
    @apiName check argument
    @apiDescription alksjdflaskq
    """
    valid_arguments = [1, 10, 100]
    if arg not in valid_arguments:
        raise ValueError(f'argument must be one of valid_arguments: {valid_arguments}')

argument_check(2)
