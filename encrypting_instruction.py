def encrypting(text:str, count = None):
    stack: list = []
    encript_str: list = []

    if len(text) <= 1 and len(stack) <= 0:
        return text
    else:
        i: int = 0
        for ch_str in  text:
            i += 1
            if ch_str in '1234567890':
               stack.append(ch_str)
               count = stack.pop()
               encrypting(text[i+1:-1], count)
            if ch_str not in'[]' and ch_str not in '1234567890':
               encript_str.append(ch_str)
            if ch_str in ']':
               str_count = encript_str.pop()
               #encript_str = []
               end_str: str = str_count * int(count)
               encript_str.append(end_str)
               end_total_str = "".join(encript_str)
               #encrypting(text[i:])
        return end_total_str

       # return "".join(cript_str) * int(count)
                
               

           

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))