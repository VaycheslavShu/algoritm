def encrypting(text:str):
    stack: int = 0
    encript_str: list = []

    if text == '':
        return text
    else:
        i: int = 0
        for ch_str in  text:
            i += 1
            if ch_str in '1234567890':
               stack =int(ch_str)
            if ch_str not in'[]' and ch_str not in '1234567890':
               encript_str.append(ch_str)
            if ch_str in ']':
                str_count = "".join(encript_str)
                encript_str = []
                end_str: str = str_count *  stack
                return end_str + encrypting(text[i:])


if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))