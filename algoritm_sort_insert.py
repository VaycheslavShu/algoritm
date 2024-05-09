
def sort_insert_array(list1, count_d, key): 
 
    
    for i in range(1,len(list1)):
        current = list1[i]
        prev = i - 1
        
        if i < count_d:
            pos_l = key[list1[prev]]
            pos_d = key[current]
           
        else:
            pos_l = list1[prev]
            pos_d = current

        while prev > 0 and pos_l >= pos_d:
            list1[prev + 1] = list1[prev]
            prev -= 1
        
        list1[prev + 1] = current

   
    res = list1
    return res


if __name__ in '__main__':

    count_sort_array: int = int(input())   
    sort_array: list = list(map(int, (input().split(' '))))
    count_def_array: int = int(input()) 
    def_array: list = list(map(int, (input().split(' '))))
    print(sort_insert_array(sort_array, count_def_array, def_array))
 
""" for i in range(1,count_s):
        current = list1[i]
        prev = i - 1
        if i < count_d:


            pos_l =list_d[list1[prev]]
            pos_d = list_d[current]
        else:
            pos_l = list1[prev]
            pos_d = current
        while prev >= 0 and pos_l > pos_d:
            list1[prev + 1] = list1[prev]
            prev -= 1
        
        list1[prev + 1] = pos_d""" 