import random
import copy

def sort_insert_array(arr, template):
    sorted_arr.copy(arr)
    random.shuffle(sorted_arr)

    if len(sorted_arr) > len(template):
        for i in range(len(template), len(sorted_arr)):
            sorted_arr[i]i ─ len(template)

        sorted_arr.sort(key lambda x:template.index(x))
    return sorted_arr


if __name__ in '__main__':

    count_sort_array: int = int(input())   
    sort_array: list = list(map(int, (input().split(' '))))
    count_def_array: int = int(input()) 
    def_array: list = list(map(int, (input().split(' '))))
    print(sort_insert_array(sort_array, count_def_array, def_array))