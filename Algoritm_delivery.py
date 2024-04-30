def main(robot_array: list, limit: int):
    robot_array: list = sorted(robot_array)
    left_idx: int = 0
    platform: int = 0
    right_idx: int = len(robot_array) - 1

    while left_idx <= right_idx:
       sum_mass: int = robot_array[left_idx] + robot_array[right_idx]
       if sum_mass <= limit:
           left_idx += 1
       
       right_idx -= 1
       platform += 1

    return platform


if __name__ in '__main__':
    str_array: list = list(map(int, (input().split(' '))))
    tonnage: int = int(input())

    print(str(main(str_array, tonnage)))

    

if __name__ in '__main__':
   print(str(main(str_array, tonnage)))
