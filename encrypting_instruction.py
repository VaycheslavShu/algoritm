def encrypting(text:str):
    count: str = ''
    res: str = ''
    bracket: int = 0

    if text.isalpha():
        return text
    else:
        i: int = 0
        while i < len(text):
            if text[i] in '1234567890':
                count += text[i]                
            if text[i] not in '1234567890[]':
                res += text[i]
            if text[i] == '[':
                bracket += 1
                k: int = i
                while k < len(text):
                    #нахождение индекса закрывающей скобки
                    if text[k] in ']':
                        bracket -= 1
                        if bracket < 0:
                            j: int = k + 1
                            break
                        elif  bracket == 0:
                            j: int = k
                            break
                    else:
                        j = k + 1 
                    k += 1   
                   #вырезка текста в скобках и вызов рекурсии
                res += encrypting(text[i+1:j]) * int(count)
                i = j + 1
                j = 0
                count = ''
                continue 
            if text[i] in ']':
                count = ''
            i += 1  
        return res      
    

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))        
