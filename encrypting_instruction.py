def encrypting(text:str, pos = 0):
    count: str = ''
    encript_str: list = []
    res: str = ''
    temp_str: list= []
    

    if text.isalpha():
        return text
    else:
        i = 0
        while i < len(text):
        
            if text[i] in '1234567890':
                count += text[i]                
            if text[i] == '[':
                temp_str = encrypting(text[i+1:]) * int(count)
                i += len(temp_str) + 1
                #i = pos
                res += temp_str 
                count = ''
                continue  # написать сдвиг вправа
            if text[i] in ']':
                count = ''
                return res
            if text[i] not in '1234567890[]':
                res += text[i]
                         
            i += 1  
           
        return res      
    

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))        
