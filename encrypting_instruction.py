def encrypting(text:str, count = None):
    stack: list = []
    encript_str: list = []

    if len(text) <= 1:
        return text
    else:
        i: int = 0
        for ch_str in  text:
            i += 1
            if ch_str in '1234567890':
               stack.append(ch_str)
            if ch_str not in'[]' and ch_str not in '1234567890':
               encript_str.append(ch_str)
            else:
               str_count = encript_str.pop()
               #encript_str = []
               end_str: str = str_count * int("".join(stack) if len(stack) == 1 else stack.pop())
               encript_str.append(end_str)
               end_total_str = "".join(encript_str)
               return encrypting(text[i:])

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))