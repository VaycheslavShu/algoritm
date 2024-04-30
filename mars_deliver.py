my_techic_array: list = list(map(int,(input().split(' '))))
tonnage: int = int(input())


def main(robot_array,limit_mass):
    cosmo_platform: int = 0
    left_index: int = 0
    right_index: int = len(robot_array)-1
    while left_index <= right_index:
        if (len(robot_array)- 1) == 0 or left_index == right_index:
            sum_mass: int = robot_array[left_index]
        else:
            sum_mass: int = robot_array[left_index]+ robot_array[left_index + 1]
            left_index += 1
        if sum_mass < limit_mass:
            if left_index == right_index or sum_mass > limit_mass :
                cosmo_platform += 1
            else:
                sum_mass: int = sum_mass + robot_array[left_index]
                cosmo_platform += 1
                left_index += 1
        else:
            cosmo_platform += 2
            
        
       
        
    print(str(cosmo_platform))



if __name__ in '__main__':
    main(my_techic_array, tonnage)
        
 