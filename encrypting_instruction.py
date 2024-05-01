def encrypting(text:str, count = None):
    stack: list = []
    cript_str: list = []

    if len(text) <= 1:
        return text
    else:
        i = 0
        for ch_str in text:
            i += 1

            if ch_str in '1234567890':
                stack.append(ch_str)
                count = "".join(stack)
                encrypting(text[i:],count)
            if ch_str not in '[]' and ch_str not in '[]'and ch_str not in '1234567890':
                cript_str.append(ch_str)
                
            #encript_str = cript_str.pop()
            #end_str = "".join(cript_str) * int(count)
        return "".join(cript_str) * int(count)
                
               

           

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))