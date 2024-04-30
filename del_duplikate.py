len_array = int(input())
my_array = input()
my_str_array = list(my_array.split(' '))
#my_int_array = list(map(int,my_str_array))

def main(my_array,number):
    search_item = 0
    end_array = []

    for item in range(number-1):
        for j  in range(search_item,number-1):
            if my_array[item] == my_array[j+1]:
                my_array[j+1] = '_'
                
                search_item +=1
            elif my_array[item] != my_array[j]:
                my_array[item] = my_array[item]
                search_item +=1          
    my_array.sort()       
    print (" ".join(my_array))
    
   
if __name__ == '__main__':
    main(my_str_array,len_array)
   