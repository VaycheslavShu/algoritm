#113753590 successful package
def encrypting(text: str):
    count: str = ''
    res: str = ''
    stack: list = []
    temp: tuple = ()
    
    for ch in text:
        acum_value: str = ''
        count_value: str = ''
        if ch in '1234567890':
            count += ch
        elif ch not in '1234567890[]':
            res += ch
        elif ch == '[':
            temp = count, res
            stack.append(temp)
            count = ''
            res = ''
        else:
            count_value, acum_value = stack.pop()
            res = acum_value + res * int(count_value)

    return res


if __name__ in '__main__':
    str_array: str = input()

    print(str(encrypting(str_array)))