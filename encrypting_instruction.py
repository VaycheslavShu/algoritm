def encrypting(text:str, number = None):
    count: str = ''
    encript_str: list = []
    res: str = ''
    temp_str: list= []

    if text.isalpha():
        return text
    else:
       
        for left in range(len(text)):
            if text[left] in '1234567890':
                count += text[left]                
            if text[left] == '[':
                i = text.find(']')
                res += encrypting(text[left+1:i]) * int(count)  
                left =i+1          
            if text[left] in ']':
               
                #res += text[left] 
                count = ''
                return res
            if text[left] not in '1234567890[]':
                res += text[left]
             
           
        return res      
    

if __name__ in '__main__':
    str_array: str = input()
    print(str(encrypting(str_array)))        
