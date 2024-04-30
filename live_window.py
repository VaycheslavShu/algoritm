my_str_array = input()

def main(my_array):
    max_count_simvol = 0
    count_0 = 0
    not_repeat = set()

    for item in range(len(my_array)):
        while my_array[item] in not_repeat:
            not_repeat.remove(my_array[count_0])
            count_0 += 1 
        not_repeat.add(my_array[item])
        max_count_simvol = max(max_count_simvol, item - count_0 + 1)          

    print (str(max_count_simvol))
    
   
if __name__ == '__main__':
    main(my_str_array)
   