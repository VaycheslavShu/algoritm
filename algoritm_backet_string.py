def bracket_check(text):
    str_stack = []
    all_ok = True
    for ch in text:
        if ch in '([{':
            str_stack.append(ch)
        elif ch in ')}]':
            backet_open = (str_stack.pop() if len(str_stack) > 0 else ' ')
            if backet_open == '(' and ch == ')':
                continue
            if backet_open == '[' and ch == ']':
                continue
            if backet_open == '{' and ch == '}':
                continue
            all_ok = False
            
    if all_ok and len(str_stack) == 0:
        return True
    else:
       return False

   

if __name__ in '__main__':
    str_text: str = input()
              
    print(bracket_check(str_text))