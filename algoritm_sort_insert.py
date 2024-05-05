def sort_insert_array(count_s, list1, count_d, list_d): 
 
    result = []
    for i in range(count_s):
        # Находим позицию элемента шаблона в исходном массиве
        if i < int(count_d):
            pos = list1.index(list_d[i])
        # Добавляем элемент в результат
            result.append(list1[pos])
        # Удаляем элемент из исходного массива, чтобы он не был добавлен повторно
            del list1[pos]
        else:
            current = list1[i]
            prev = i - 1
        
            while prev >= 0 and list1[prev] > current:
                list1[prev + 1] = list1[prev]
                prev -= 1
        # Вставляем current в отсортированную часть массива на нужное место.
            list1[prev + 1] = current 
        #del list1[pos]

    return result


if __name__ in '__main__':

    count_sort_array: int = int(input())   
    sort_array: list = list(map(int, (input().split(' '))))
    count_def_array: int = int(input()) 
    def_array: list = list(map(int, (input().split(' '))))
    print(str(sort_insert_array(count_sort_array, sort_array, count_def_array, def_array)))
 
