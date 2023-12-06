

def concatenate(x:str, y:str):
    if not isinstance(x, str) or not isinstance(y, str):
        raise ValueError('All arguments must be of type string.')
    result = x + y
    return f"Result of concatenation of '{x}'' and '{y}' is {result}"


def string_from_list(lst:list):
    if not isinstance(lst, list):
        raise ValueError('Argument must be of type string.')
    result = ''.join(lst)
    return f"Result of creating string from list '{lst}' is {result}"


def check_numeric_string_at_least_one(txt):
    if not isinstance(txt, str):
        raise ValueError('Arguments must be of type string.')
    count = 0
    for i in txt:
        if i.isnumeric():
            count += 1
    result = bool(count)
    if count:
        return f"There is a digit in your string!\nResult of checking digits in the string '{txt}' is {result}"
    else:
        return result


